# Django settings for product env.

from common import *

# Debug settings
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nitrate',
        'USER': 'nitrate',
        'PASSWORD': 'nitrate',
        'HOST': '',
        'PORT': '',
    },
    'slave_1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nitrate',
        'USER': 'nitrate',
        'PASSWORD': 'nitrate',
        'HOST': '',
        'PORT': '',
    },
}

# add RemoteUserMiddleWare if kerberos authentication is enabled
MIDDLEWARE_CLASSES += (
#    'django.contrib.auth.middleware.RemoteUserMiddleware',
)

# Remote kerberos authentication backends
#AUTHENTICATION_BACKENDS = (
#    'tcms.core.contrib.auth.backends.ModAuthKerbBackend',
#)

DATABASE_ROUTERS = ['tcms.core.utils.tcms_router.RWRouter']

# Kerberos realm
#KRB5_REALM = 'EXAMPLE.COM'

# Bugzilla integration setttings
# Config following settings if your want to integrate with bugzilla
BUGZILLA3_RPC_SERVER = ''
BUGZILLA_URL = ''
BUGZILLA_USER = ''
BUGZILLA_PASSWORD = ''

# JIRA integration setttings
# Config following settings if your want to integrate with JIRA
JIRA_URL = ''

# Set the default send mail address
EMAIL_HOST = 'smtp.example.com'
EMAIL_FROM = 'noreply@example.com'

# Site-specific messages

# First run - to detemine need port user or not.
FIRST_RUN = False

# You can add a help link on the footer of home page as following format:
# ('http://foo.com', 'foo')
FOOTER_LINKS = (
 ('/xmlrpc/', 'XML-RPC service'),
)

# added for nitrate3.4 compatibility
DEFAULT_GROUPS = ['default']
TESTOPIA_XML_VERSION = '1.0'

# admin settings
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

# user guide URL
USER_GUIDE_URL = ""

DEFAULT_PAGE_SIZE = 100
