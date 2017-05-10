import sys

from hacker_news_scraper.settings.base import *  # noqa

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1', )

#: Don't send emails, just print them on stdout
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#: Run celery tasks synchronously
CELERY_ALWAYS_EAGER = True

#: Tell us when a synchronous celery task fails
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

SECRET_KEY = os.environ.get('SECRET_KEY', '9f69b6-f62n5)%y83sjw(wyoaq8j#a)=27xunvawf6-(r20k(n')

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Special test settings
if 'test' in sys.argv:
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )

    LOGGING['root']['handlers'] = []
