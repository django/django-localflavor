from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.kz.forms import (KZIndividualIDField,
                                  KZCivilPassportNumberField,
                                  KZZipCodeField)


class KZLocalFlavorTests(SimpleTestCase):
    def test_KZIndividualIDField(self):
        error_invalid = ['Enter a valid Kazakhstani Individual ID number']
        valid = {
            '890203300296': '890203300296',
            '950406786295': '950406786295',
        }
        invalid = {
            '0000': error_invalid,
            '891303300296': error_invalid,
            '951232300296': error_invalid,
        }
        self.assertFieldOutput(KZIndividualIDField, valid, invalid)

    def test_KZPassportNumberField(self):
        error_invalid = ['Enter valid Kazakhstani Passport number. Format NXXXXXXXX']
        valid = {
            'N95667788': 'N95667788',
            'n95667788': 'N95667788',
            ' n95667788': 'N95667788',
            ' n95667788 ': 'N95667788',
            'n95667788 ': 'N95667788',
        }
        invalid = {
            '0000': error_invalid,
            '891303300296': error_invalid,
            '951232300296': error_invalid,
            'NNNNNNNNNNNNN': error_invalid,
            'NW9034902830': error_invalid,
            'N0959741305': error_invalid,
        }
        self.assertFieldOutput(KZCivilPassportNumberField, valid, invalid)

    def test_KZZipCodeField(self):
        error_invalid = ['Enter a zip code in the format XXXXX']
        valid = {
            '050014': '050014',
            ' 050014': '050014',
            '050014 ': '050014',
            ' 050014 ': '050014',
        }
        invalid = {
            '0000': error_invalid,
            '891303300296': error_invalid,
            '951232300296': error_invalid,
            'NNNNNNNNNNNNN': error_invalid,
            'NW9034902830': error_invalid,
        }
        self.assertFieldOutput(KZZipCodeField, valid, invalid)
