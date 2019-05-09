from django.core.exceptions import ValidationError
from django.test import TestCase

from localflavor.tr.forms import TRIdentificationNumberField, TRPostalCodeField


class TRLocalFlavorTests(TestCase):
    def test_TRPostalCodeField(self):
        f = TRPostalCodeField()
        self.assertEqual(f.clean("06531"), "06531")
        self.assertEqual(f.clean("12345"), "12345")
        err_msg = "Enter a postal code in the format XXXXX."
        self.assertRaisesRegex(ValidationError, err_msg, f.clean, "a1234")
        self.assertRaisesRegex(ValidationError, err_msg, f.clean, "1234")
        self.assertRaisesRegex(ValidationError, err_msg, f.clean, "82123")
        self.assertRaisesRegex(ValidationError, err_msg, f.clean, "00123")
        self.assertRaisesRegex(ValidationError, err_msg, f.clean, "123456")
        self.assertRaisesRegex(ValidationError, err_msg, f.clean, "12 34")
        self.assertRaises(ValidationError, f.clean, None)

    def test_TRIdentificationNumberField(self):
        f = TRIdentificationNumberField()
        self.assertEqual(f.clean("10000000146"), "10000000146")
        self.assertRaisesRegex(ValidationError,
                               'Enter a valid Turkish Identification number.',
                               f.clean, "10000000136")
        self.assertRaisesRegex(ValidationError,
                               'Enter a valid Turkish Identification number.',
                               f.clean, "10000000147")
        self.assertRaisesRegex(ValidationError,
                               'Turkish Identification number must be 11 digits.',
                               f.clean, "123456789")
        self.assertRaisesRegex(ValidationError,
                               'Enter a valid Turkish Identification number.',
                               f.clean, "1000000014x")
        self.assertRaisesRegex(ValidationError,
                               'Enter a valid Turkish Identification number.',
                               f.clean, "x0000000146")
