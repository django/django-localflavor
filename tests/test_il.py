from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.il.forms import ILIDNumberField, ILMobilePhoneNumberField, ILPostalCodeField


class ILLocalFlavorTests(SimpleTestCase):
    def test_ILPostalCodeField(self):
        error_format = ['Enter a postal code in the format XXXXXXX (or XXXXX) - digits only']
        valid = {
            '69973': '69973',
            '699 73': '69973',
            '12345': '12345',
            '6665557': '6665557',
        }
        invalid = {
            '84545x': error_format,
            '123456': error_format,
            '1234': error_format,
            '123 4': error_format,
            '44455522': error_format,
        }
        self.assertFieldOutput(ILPostalCodeField, valid, invalid)

    def test_ILIDNumberField(self):
        error_invalid = ['Enter a valid ID number.']
        valid = {
            '3933742-3': '39337423',
            '39337423': '39337423',
            '039337423': '039337423',
            '03933742-3': '039337423',
            '0091': '0091',
        }
        invalid = {
            '123456789': error_invalid,
            '12345678-9': error_invalid,
            '012346578': error_invalid,
            '012346578-': error_invalid,
            '0001': error_invalid,
        }
        self.assertFieldOutput(ILIDNumberField, valid, invalid)

    def test_ILMobilePhoneNumber(self):
        error_invalid = ['Enter a valid Mobile Number.']
        valid = {
            '0500000000': '0500000000',
            '0522222222': '0522222222',
            '0533333333': '0533333333',
            '0544444444': '0544444444',
            '0555555555': '0555555555',
            '0566666666': '0566666666',
            '0577777777': '0577777777',
            '0588888888': '0588888888',
            '0599999999': '0599999999',
            '052-2222222': '052-2222222',
            '52-2222222': '52-2222222',
            '525555555': '525555555',
            '(050)-1111111': '(050)-1111111',
            '(050)1111111': '(050)1111111'
        }
        invalid = {
            '05556': error_invalid,
            '0605555555': error_invalid,
            '050)1111111': error_invalid,
            '55--2222222': error_invalid,
            '0511111111': error_invalid,
            '05777777': error_invalid,
            '05555555555': error_invalid,
            '0054673446': error_invalid,
        }
        self.assertFieldOutput(ILMobilePhoneNumberField, valid, invalid)
