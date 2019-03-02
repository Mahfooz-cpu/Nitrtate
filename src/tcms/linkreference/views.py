# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from .forms import AddLinkReferenceForm, BasicValidationForm
from .models import create_link, LinkReference
from tcms.core.responses import JsonResponseBadRequest
from tcms.core.responses import JsonResponseServerError

__all__ = ('add', 'get', 'remove', )


@require_POST
@permission_required('testruns.change_testcaserun')
def add(request):
    """Add new link to a specific target

    The target should be a valid model within TCMS, which are documented in
    ``LINKREF_TARGET``.

    Incoming request should be a POST request, and contains following
    arguments:

    - target: To which the new link will link to. The avialable target names
      are documented in the ``LINKREF_TARGET``.
    - target_id: the ID used to construct the concrete target instance, to
      which the new link will be linked.
    - name: a short description to this new link, and accept 64 characters at
      most.
    - url: the actual URL.
    """

    form = AddLinkReferenceForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        url = form.cleaned_data['url']
        target_id = form.cleaned_data['target_id']
        model_class = form.cleaned_data['target']

        model_instance = model_class.objects.get(pk=target_id)
        create_link(name=name, url=url, link_to=model_instance)

        return JsonResponse({
            'rc': 0,
            'response': 'ok',
            'data': {'name': name, 'url': url}
        })

    else:
        return JsonResponseBadRequest({
            'rc': 1,
            'response': form.errors.as_text()
        })


@require_GET
def get(request):
    """Get links of specific instance of content type

    - target: The model name of the instance being searched
    - target_id: The ID of the instance

    Only accept GET request from client.
    """

    form = BasicValidationForm(request.GET)

    if form.is_valid():
        model_class = form.clean_data['target']
        target_id = form.clean_data['target_id']

        try:
            model_instance = model_class.objects.get(pk=target_id)
            links = LinkReference.get_from(model_instance)
        except Exception as err:
            return JsonResponseServerError({'rc': 1, 'response': str(err)})

        jd = []
        for link in links:
            jd.append({'name': link.name, 'url': link.url})
        return JsonResponse(jd, safe=False)

    else:
        return JsonResponseBadRequest({
            'rc': 1,
            'response': form.errors.as_text()
        })


@require_GET
@permission_required('testruns.change_testcaserun')
def remove(request, link_id):
    """Remove a specific link with ID ``link_id``"""

    from django.forms import IntegerField
    from django.forms import ValidationError

    field = IntegerField(min_value=1)
    try:
        value = field.clean(link_id)
    except ValidationError as err:
        return JsonResponseBadRequest({
            'rc': 1,
            'response': '\n'.join(err.messages)
        })

    try:
        LinkReference.unlink(value)
    except Exception as err:
        return JsonResponseBadRequest({'rc': 1, 'response': str(err)})

    return JsonResponse({
        'rc': 0,
        'response': 'Link has been removed successfully.'
    })
