# -*- coding: utf-8 -*-

import os
# PROJECT_PATH = os.path.dirname(__file__)
# DEBUG_LOCAL = True

# if DEBUG_LOCAL:
#     MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')
# else:
#     MEDIA_ROOT = '/opt/django-projects/alive/media/'

# # Make this unique, and don't share it with anybody.
SECRET_KEY = '*bu^*vhx2do)5zskd6)yee42o7y9q+3$x7k02**q6x=v-qm-sa'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'matmotos2016@gmail.com'
# EMAIL_HOST_PASSWORD = '_12345678A'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
         # DESARROLLO LOCAL
        'NAME': 'projectbase',
        'USER': 'adhoc',
        'PASSWORD': 'devtest',
        'HOST': 'localhost',
        'PORT': '5432',     
    }
}