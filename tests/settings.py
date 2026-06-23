DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'localflavor',
    'tests.test_ae',
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
    'tests.test_qa',
    'tests.test_ua',
    'tests.test_us',
]

SECRET_KEY = 'spam-spam-spam-spam'

SILENCED_SYSTEM_CHECKS = ('1_7.W001', 'models.W042')

# Django 6.1 changed the blank choice to "- Select an option -" which breaks our tests.
#
# USE_BLANK_CHOICE_DASH only works for Django 6.x. For Django >= 7.0 we'll need to set
# django.db.models.fields.BLANK_CHOICE_LABEL in a test app's ready() method if a global setting for this isn't added.
#
# https://github.com/django/django/commit/63c56cda133a85a158502891c40465bc0331d3d9
USE_BLANK_CHOICE_DASH = True
