import os
from _base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
) #specifies all the folders on your system where Django should look for static files

STATIC_ROOT = (os.path.join(BASE_DIR, 'compiled_static'))
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Allow all host headers
ALLOWED_HOSTS = ['*']
