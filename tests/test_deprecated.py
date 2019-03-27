import warnings

from django.test import SimpleTestCase

from localflavor.deprecation import RemovedInLocalflavor30Warning
from localflavor.generic.checksums import luhn, ean

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class DeprecatedFieldsTests(SimpleTestCase):
    @patch('localflavor.generic.checksums.stdnum_luhn')
    def test_luhn_deprecated(self, stdnum_luhn):
        with warnings.catch_warnings(record=True) as recorded:
            warnings.simplefilter('always')
            luhn('1234')

        self.assertTrue(all(w.category is RemovedInLocalflavor30Warning for w in recorded))
        stdnum_luhn.asert_called_once_with('1234')

    @patch('localflavor.generic.checksums.stdnum_ean')
    def test_ean_deprecated(self, stdnum_ean):
        with warnings.catch_warnings(record=True) as recorded:
            warnings.simplefilter('always')
            ean('1234')

        self.assertTrue(all(w.category is RemovedInLocalflavor30Warning for w in recorded))
        stdnum_ean.asert_called_once_with('1234')
