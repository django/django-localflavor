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
    'tests.test_md',
    'tests.test_mk',
    'tests.test_mx',
    'tests.test_ua',
    'tests.test_us',
    'tests.test_pk',
    'tests.test_cu',
    'tests.test_generic',
]

SECRET_KEY = 'spam-spam-spam-spam'

SILENCED_SYSTEM_CHECKS = ('1_7.W001', 'models.W042')
