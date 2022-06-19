import os


INSTALLED_APPS = [
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
