import os
from _base import *

DEBUG = False

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

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
