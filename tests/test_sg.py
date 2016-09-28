from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.sg.forms import SGNRIC_FINField, SGPhoneNumberField, SGPostCodeField


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
            'e23fee': error_format,
        }
        self.assertFieldOutput(SGPostCodeField, valid, invalid)

    def test_SGPhoneNumberField(self):
        error_format = ['Phone numbers must contain 8 digits and start with '
                        'either 6, or 8, or 9.']
        valid = {
            '6880 4321 ': '68804321',
            '  9123 3132': '91233132',
            '83234441': '83234441',
        }
        invalid = {
            '65 4234 4234': error_format,
            '(+65) 1230 0180': error_format,
            '(65)1432 2424': error_format,
            '32344569': error_format,
        }
        self.assertFieldOutput(SGPhoneNumberField, valid, invalid)

    def test_SGNRIC_FINField(self):
        error_format = ['Invalid NRIC/FIN.']
        valid = {
            's8675985c': 'S8675985C',
            'S8776318H': 'S8776318H',
            ' G0746467W': 'G0746467W',
            'T1399266A': 'T1399266A',
            'F5401671U ': 'F5401671U',
        }
        invalid = {
            'S5777125G': error_format,
            'T4461323J': error_format,
            'A2119569M': error_format,
            'F8155379N': error_format,
            'G1087200K': error_format,
        }
        self.assertFieldOutput(SGNRIC_FINField, valid, invalid)
