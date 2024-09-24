
from core.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pp1ntcn6ibeq5=cta^+btdifr)5!)rik(5$as2#_ahne)$-rt0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
COMINGSOON = False
ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
COMPRESS_ROOT = os.path.join(BASE_DIR, 'media')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')