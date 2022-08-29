import os


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'DjangoORM.orm',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('HerokuPostgresHost'),
        'USER': os.getenv('HerokuPostgresUser'),
        'NAME': os.getenv('HerokuPostgresDatabase'),
        'PORT': os.getenv('HerokuPostgresPort'),
        'PASSWORD': os.getenv('HerokuPostgresPassword'),
        'ATOMIC_REQUESTS': True,
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'orm.CybersportUser'
