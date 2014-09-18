from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.sg.forms import SGPostCodeField, SGPhoneNumberField


class SGLocalFlavorTests(SimpleTestCase):
    def test_SGPostCodeField(self):
        error_format = ['Enter a 6-digit postal code.']
        valid = {
            '247964': '247964',
            '050335': '050335',
            '520110': '520110',
            '521110': '521110',
        }
        invalid = {
            '0000': error_format,
            '0123': error_format,
            'eeffee': error_format,
        }
        self.assertFieldOutput(SGPostCodeField, valid, invalid)

    def test_SGPhoneNumberField(self):
        error_format = ['Phone numbers must contain 8 digits and start with '
                        'either 6, or 8, or 9.']
        valid = {
            '6880 4321 ': '68804321',
            '91233132': '91233132',
            '83234441': '83234441',
        }
        invalid = {
            '1237 010181': error_format,
            '12370 010180': error_format,
            '32344569': error_format,
        }
        self.assertFieldOutput(SGPhoneNumberField, valid, invalid)
