from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.mt.forms import MTPostalCodeField


class MTLocalFlavorTests(SimpleTestCase):
    def test_MTPostalCodeField(self):
        error_format = ['Enter a valid postal code in format AAA 0000.']
        valid = {
            'AAA 0000': 'AAA 0000',
            'VLT 1117': 'VLT 1117',
        }
        invalid = {
            'AAA0000': error_format,
            'VLT1117': error_format,
        }
        self.assertFieldOutput(MTPostalCodeField, valid, invalid)
