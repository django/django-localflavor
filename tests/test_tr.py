from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import six

from localflavor.tr.forms import TRIdentificationNumberField, TRPostalCodeField

if six.PY3:
    _assertRaisesRegex = "assertRaisesRegex"
else:
    _assertRaisesRegex = "assertRaisesRegexp"


def assertRaisesRegex(self, *args, **kwargs):
    return getattr(self, _assertRaisesRegex)(*args, **kwargs)


class TRLocalFlavorTests(TestCase):
    def test_TRPostalCodeField(self):
        f = TRPostalCodeField()
        self.assertEqual(f.clean("06531"), "06531")
        self.assertEqual(f.clean("12345"), "12345")
        assertRaisesRegex(self, ValidationError,
                          "Enter a postal code in the format XXXXX.",
                          f.clean, "a1234")
        assertRaisesRegex(self, ValidationError,
                          "Enter a postal code in the format XXXXX.",
                          f.clean, "1234")
        assertRaisesRegex(self, ValidationError,
                          "Enter a postal code in the format XXXXX.",
                          f.clean, "82123")
        assertRaisesRegex(self, ValidationError,
                          "Enter a postal code in the format XXXXX.",
                          f.clean, "00123")
        assertRaisesRegex(self, ValidationError,
                          "Enter a postal code in the format XXXXX.",
                          f.clean, "123456")
        assertRaisesRegex(self, ValidationError,
                          "Enter a postal code in the format XXXXX.",
                          f.clean, "12 34")
        self.assertRaises(ValidationError, f.clean, None)

    def test_TRIdentificationNumberField(self):
        f = TRIdentificationNumberField()
        self.assertEqual(f.clean("10000000146"), "10000000146")
        assertRaisesRegex(self, ValidationError,
                          'Enter a valid Turkish Identification number.',
                          f.clean, "10000000136")
        assertRaisesRegex(self, ValidationError,
                          'Enter a valid Turkish Identification number.',
                          f.clean, "10000000147")
        assertRaisesRegex(self, ValidationError,
                          'Turkish Identification number must be 11 digits.',
                          f.clean, "123456789")
        assertRaisesRegex(self, ValidationError,
                          'Enter a valid Turkish Identification number.',
                          f.clean, "1000000014x")
        assertRaisesRegex(self, ValidationError,
                          'Enter a valid Turkish Identification number.',
                          f.clean, "x0000000146")
