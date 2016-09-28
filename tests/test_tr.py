from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import six

from localflavor.tr.forms import TRIdentificationNumberField, TRPhoneNumberField, TRPostalCodeField

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

    def test_TRPhoneNumberField(self):
        f = TRPhoneNumberField()
        self.assertEqual(f.clean("312 455 56 78"), "3124555678")
        self.assertEqual(f.clean("312 4555678"), "3124555678")
        self.assertEqual(f.clean("3124555678"), "3124555678")
        self.assertEqual(f.clean("0312 455 5678"), "3124555678")
        self.assertEqual(f.clean("0 312 455 5678"), "3124555678")
        self.assertEqual(f.clean("0 (312) 455 5678"), "3124555678")
        self.assertEqual(f.clean("+90 312 455 4567"), "3124554567")
        self.assertEqual(f.clean("+90 312 455 45 67"), "3124554567")
        self.assertEqual(f.clean("+90 (312) 4554567"), "3124554567")
        assertRaisesRegex(self, ValidationError,
                          'Phone numbers must be in 0XXX XXX XXXX format.',
                          f.clean, "1234 233 1234")
        assertRaisesRegex(self, ValidationError,
                          'Phone numbers must be in 0XXX XXX XXXX format.',
                          f.clean, "0312 233 12345")
        assertRaisesRegex(self, ValidationError,
                          'Phone numbers must be in 0XXX XXX XXXX format.',
                          f.clean, "0312 233 123")
        assertRaisesRegex(self, ValidationError,
                          'Phone numbers must be in 0XXX XXX XXXX format.',
                          f.clean, "0312 233 xxxx")

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
