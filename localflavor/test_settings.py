# -*- coding: utf-8 -*-
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'discover_runner',
    'localflavor',
    'localflavor.au.tests',
    'localflavor.mk.tests',
    'localflavor.mx.tests',
    'localflavor.us.tests',
]

SECRET_KEY = 'spam-spam-spam-spam'

TEST_RUNNER = 'discover_runner.DiscoverRunner'
