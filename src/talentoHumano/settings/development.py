from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-zzt8y0+8uw1#ovm!zcje$s4x)n=z3ntr8oy_2abmbwmccd6=q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'