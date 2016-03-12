# {{ ansible_managed }}
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x*m*9+#t04u3*80t@phqqh)&q9=do)ot1fjz^s#h5r5wweag8b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ db_name }}',               # Or path to database file if using sqlite3.
        'USER': '{{ db_username }}',           # Not used with sqlite3.
        'PASSWORD': '{{ db_password }}',       # Not used with sqlite3.
        'HOST': '{{ db_host }}',               # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',               # Set to empty string for default. Not used with sqlite3.
    }
}
