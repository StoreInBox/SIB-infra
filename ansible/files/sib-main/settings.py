from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x*m*9+#t04u3*80t@phqqh)&q9=do)ot1fjz^s#h5r5wweag8b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ['http://127.0.0.1:80']

TEMPLATE_DEBUG = DEBUG

LANGUAGE_CODE = 'en'

ALLOWED_HOSTS = ['128.199.63.47']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ db_name }}',
        'USER': '{{ db_username }}',
        'PASSWORD': '{{ db_password }}',
        'HOST': '{{ db_host }}',
        'PORT': '',
    }
}

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'frontend', 'templates'),
    os.path.join(PROJECT_DIR, 'frontend', 'templates-examples'),
)
