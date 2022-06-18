INSTALLED_APPS = [
    'orm',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': None,
        'USER': None,
        'NAME': None,
        'PORT': None,
        'PASSWORD': None,
        'ATOMIC_REQUESTS': True,
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
