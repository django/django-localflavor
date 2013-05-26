from django.utils import six

if six.PY3:
    _assertRaisesRegex = "assertRaisesRegex"
else:
    _assertRaisesRegex = "assertRaisesRegexp"


def assertRaisesRegex(self, *args, **kwargs):
    return getattr(self, _assertRaisesRegex)(*args, **kwargs)
