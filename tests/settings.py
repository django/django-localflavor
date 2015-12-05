# -*- coding: utf-8 -*-

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'localflavor',
    'tests.test_br',
    'tests.test_au',
    'tests.test_ec',
    'tests.test_mk',
    'tests.test_mx',
    'tests.test_us',
    'tests.test_pk',
]

SECRET_KEY = 'spam-spam-spam-spam'

SILENCED_SYSTEM_CHECKS = ('1_7.W001',)
