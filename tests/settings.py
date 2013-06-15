# -*- coding: utf-8 -*-
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'localflavor',
    'localflavor.au.tests',
    'localflavor.mk.tests',
    'localflavor.mx.tests',
    'localflavor.us.tests',
]

if 'EXTERNAL_DISCOVER_RUNNER' in os.environ:
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
    INSTALLED_APPS += ['discover_runner']

SECRET_KEY = 'spam-spam-spam-spam'
