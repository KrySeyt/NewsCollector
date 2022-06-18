import os

import django


def setup():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoORM.settings')
    django.setup()
