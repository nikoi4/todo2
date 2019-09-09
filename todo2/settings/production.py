import dj_database_url
from .base import *

ENVIRONMENT = 'production'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo_list',
        'USER': 'name',
        'PASSWORD': '',
        'PORT': '',
    }
}

DB_FROM_ENV = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(DB_FROM_ENV)

ALLOWED_HOSTS = [
    'django2do.herokuapp.com',
    '0.0.0.0'
]