SITE_ID = 1
SECRET_KEY = "my-top-secret-key"

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
