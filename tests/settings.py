DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'localflavor',
    'tests.test_au',
    'tests.test_br',
    'tests.test_by',
    'tests.test_ca',
    'tests.test_cu',
    'tests.test_ec',
    'tests.test_fr',
    'tests.test_generic',
    'tests.test_gh',
    'tests.test_lk',
    'tests.test_md',
    'tests.test_mk',
    'tests.test_mx',
    'tests.test_np',
    'tests.test_pk',
    'tests.test_ua',
    'tests.test_us',
]

SECRET_KEY = 'spam-spam-spam-spam'

SILENCED_SYSTEM_CHECKS = ('1_7.W001', 'models.W042')
