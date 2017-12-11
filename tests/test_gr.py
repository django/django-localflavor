from django.test import SimpleTestCase

from localflavor.gr.forms import GRPostalCodeField, GRTaxNumberCodeField


class GRLocalFlavorTests(SimpleTestCase):

    def test_GRTaxNumberField(self):
        """The valid tests are from greek tax numbers (AFMs) found on the internet with a google search."""
        error = ['Enter a valid greek tax number (9 digits).']
        valid = {
            '090051291': '090051291',
            '997881842': '997881842',
            '090220804': '090220804',
            '090000045': '090000045',
            '099757704': '099757704',

        }
        invalid = {
            '123456789': error,
            '123 32 12 3213': error,
            '32 123 5345': error,
            '0': error,
            'abc': error,
            '00000': error,
            '000000000': error,
            '1111111': error,
            '3123123': error,
            '312312334534': error,
            '999999999': error,
            '123123123': error,
            '321000123': error,
            'd21000123': error,
        }
        self.assertFieldOutput(GRTaxNumberCodeField, valid, invalid)

    def test_GRPostalCodeField(self):
        error = ['Enter a valid 5-digit greek postal code.']
        valid = {
            '51642': '51642',
            '21742': '21742',
            '75006': '75006',
            '85017': '85017',
        }
        invalid = {
            '12 34': error,
            '124567': error,
            '04567': error,
            '94567': error,
            '1345': error,
            '134115': error,
            'b231a': error,
        }
        self.assertFieldOutput(GRPostalCodeField, valid, invalid)
