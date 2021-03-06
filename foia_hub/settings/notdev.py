from .base import *
import os

# There are common settings between staging and production. This puts them
# all in one place.

DEBUG = False
TEMPLATE_DEBUG = False

# Flag to determine whether the FOIA request form gets shown.
SHOW_WEBFORM = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.getenv('TMPDIR', '/tmp'),
        'TIMEOUT': 1440,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        },
    }
}

AWS_STORAGE_BUCKET_NAME = os.getenv('FOIA_S3_STATIC_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Don't add complex authentication related query parameters for requests
AWS_QUERYSTRING_AUTH = False
