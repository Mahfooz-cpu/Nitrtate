# Django settings for devel env.

from __future__ import absolute_import

from .common import *

# Debug settings
DEBUG = True

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nitrate',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# django-debug-toolbar settings
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

# For local development
ENABLE_ASYNC_EMAIL = False

FILE_UPLOAD_DIR = os.path.join(TCMS_ROOT_PATH, '..', 'uploads')
