import unittest

from django.core.exceptions import ValidationError

from localflavor.generic import validators


class TestVATINValidator(unittest.TestCase):
    validator = validators.VATINValidator()

    VALID_VATIN = 'DE284754038'

    def test_valid_vatin(self):
        self.validator(self.VALID_VATIN)

    def test_invalid_vatin(self):
        with self.assertRaises(ValidationError) as cm:
            self.validator('DE99999999')
        e = cm.exception
        self.assertIn("DE99999999 is not a valid VAT identification number.",  e.messages)

    def test_invalid_country_code(self):
        with self.assertRaises(ValidationError) as cm:
            self.validator('XX99999999')
        e = cm.exception
        self.assertIn("XX is not a valid country code.", e.messages)
