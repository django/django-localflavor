# -*- coding: utf-8 -*-

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'localflavor',
    'tests.test_au',
    'tests.test_ec',
    'tests.test_mk',
    'tests.test_mx',
    'tests.test_us',
    'tests.test_pk',
    'tests.test_generic',
    'tests.test_deprecated',
]

SECRET_KEY = 'spam-spam-spam-spam'

SILENCED_SYSTEM_CHECKS = ('1_7.W001',)
