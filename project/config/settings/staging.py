import os
from _base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'randomtemppassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
