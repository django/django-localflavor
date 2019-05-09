import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.test import TestCase

from localflavor.bg.models import BGEGNField, BGEIKField
from localflavor.bg.utils import get_egn_birth_date
from localflavor.bg.validators import EGNValidator, EIKValidator

VALID_EGNS = (
    '7523169263',
    '8032056031',
    '8001010008',
    '7501020018',
    '7552010005',
    '7542011030',
    '0010100100'
)
VALID_EIKS = (
    '831919536',
    '121887948',
    '175015558',
    '175223064',
    '000565359',
    '0005653590079',
    '176040023',
    '1760400230151',
    '121817309',
    '1218173090603',
    '104453698',
    '1044536985268',
)
INVALID_EGNS = (
    '0010100101'
    '1111111111',
    '1234567890',
    '2222222222',
    '3333333333',
    '4444444444',
    '5555555555',
    '6666666666',
    '7777777777',
    '8888888888',
    '9999999999',
    '0000000000',
    'aaaaaaaaaa',
)
INVALID_EIKS = (
    '111111111',
    '1111111111111',
    '123456789',
    '1234567890123',
    '176040024',  # Invalid cheksum
    '1760400230152',  # Valid first checksum invalid second checksum
    'aaaaaaaaaa',
)

eik_validator = EIKValidator()
egn_validator = EGNValidator()


class BGLocalFlavorValidatorsTests(TestCase):

    def test_egn_validator_with_valid_egns(self):
        for egn in VALID_EGNS:
            try:
                egn_validator(egn)
            except ValidationError:
                self.fail('egn_validator said that valid EGN %s is invalid' % egn)

    def test_egn_validator_with_invalid_egns(self):
        for egn in INVALID_EGNS:
            self.assertRaises(ValidationError, egn_validator, egn)

    def test_eik_validator_with_valid_eiks(self):
        for eik in VALID_EIKS:
            try:
                eik_validator(eik)
            except ValidationError:
                self.fail('eik_validator fails for %s' % eik)

    def test_eik_validator_with_invalid_eiks(self):
        for eik in INVALID_EIKS:
            self.assertRaises(ValidationError, eik_validator, eik)


class BGLocalFlavorEGNFieldTests(TestCase):

    class EGNModel(models.Model):
        egn = BGEGNField()

        class Meta:
            app_label = 'test_bg'

    def setUp(self):

        class EGNForm(forms.ModelForm):
            class Meta:
                model = self.EGNModel
                fields = 'egn',

        self.EGNForm = EGNForm

    def test_egn_form_with_valid_egns(self):
        for egn in VALID_EGNS:
            form = self.EGNForm({'egn': egn})
            self.assertTrue(form.is_valid())

    def test_egn_form_with_invalid_egns(self):
        for egn in INVALID_EGNS:
            form = self.EGNForm({'egn': egn})
            self.assertFalse(form.is_valid())


class BGLocalFlavorEIKFieldTest(TestCase):

    class EIKModel(models.Model):
        eik = BGEIKField()

        class Meta:
            app_label = 'test_bg'

    def setUp(self):

        class EIKForm(forms.ModelForm):
            class Meta:
                model = self.EIKModel
                fields = 'eik',

        self.EIKForm = EIKForm

    def test_eik_form_with_valid_eiks(self):
        for eik in VALID_EIKS:
            form = self.EIKForm({'eik': eik})
            self.assertTrue(form.is_valid())

    def test_eik_form_with_invalid_eiks(self):
        for eik in INVALID_EIKS:
            form = self.EIKForm({'eik': eik})
            self.assertFalse(form.is_valid())


class BGLocaFlavorUtilsTest(TestCase):

    def test_get_egn_birth_date_with_valid_date_from_1800_to_1900(self):
        self.assertEqual(get_egn_birth_date('002101'), datetime.date(1800, 1, 1))
        self.assertEqual(get_egn_birth_date('993231'), datetime.date(1899, 12, 31))

    def test_get_egn_birth_date_with_valid_date_from_1900_to_2000(self):
        self.assertEqual(get_egn_birth_date('000101'), datetime.date(1900, 1, 1))
        self.assertEqual(get_egn_birth_date('991231'), datetime.date(1999, 12, 31))

    def test_get_egn_birth_date_with_valid_date_from_2000_to_2100(self):
        self.assertEqual(get_egn_birth_date('004101'), datetime.date(2000, 1, 1))
        self.assertEqual(get_egn_birth_date('995231'), datetime.date(2099, 12, 31))

    def test_get_egn_birth_date_with_invalid_dates(self):
        # Wrong month in year 1800
        self.assertRaises(ValueError, get_egn_birth_date, '003301')

        # Wrong day in January 1800
        self.assertRaises(ValueError, get_egn_birth_date, '002132')

        # Wrong month in year 1900
        self.assertRaises(ValueError, get_egn_birth_date, '001301')

        # Wrong day in January 1900
        self.assertRaises(ValueError, get_egn_birth_date, '000132')

        # Wrong month in year 2000
        self.assertRaises(ValueError, get_egn_birth_date, '005301')

        # Wrong day in January 2000
        self.assertRaises(ValueError, get_egn_birth_date, '004132')

        # Not enough characters characters
        self.assertRaises(ValueError, get_egn_birth_date, '0001')

        # Not numbers
        self.assertRaises(ValueError, get_egn_birth_date, 'aaaaaa')
