from django.conf import settings

SITE_ID = 1
SECRET_KEY = "KEKERIKEK"
MAX_ATTEMPTS = getattr(settings, 'LOCKOUT_MAX_ATTEMPTS', 5)
LOCKOUT_TIME = getattr(settings, 'LOCKOUT_TIME', 60 * 10) # 10 minutes
ENFORCEMENT_WINDOW = getattr(settings, 'LOCKOUT_ENFORCEMENT_WINDOW', 60 * 5) # 5 minutes
USE_USER_AGENT = getattr(settings, 'LOCKOUT_USE_USER_AGENT', False)
CACHE_PREFIX = getattr(settings, 'LOCKOUT_CACHE_PREFIX', 'lockout')


INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'lockout'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django-lockout',
    }
}
