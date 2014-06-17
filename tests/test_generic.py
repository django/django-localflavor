# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.test import SimpleTestCase, TestCase
from django.utils import formats

from localflavor.generic.models import IBANField
from localflavor.generic.validators import IBANValidator
from localflavor.generic.forms import (DateField, DateTimeField,
                                       SplitDateTimeField, IBANFormField)


class DateTimeFieldTestCase(SimpleTestCase):

    default_date_input_formats = (
        '%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y', '%b %d %Y', '%b %d, %Y',
        '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y',
        '%d %B, %Y',
    )

    default_datetime_input_formats = (
        '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%d/%m/%Y %H:%M:%S',
        '%d/%m/%Y %H:%M', '%d/%m/%Y', '%d/%m/%y %H:%M:%S', '%d/%m/%y %H:%M',
        '%d/%m/%y',
    )

    def assertInputFormats(self, field, formats):
        self.assertSequenceEqual(field.input_formats, formats)


class DateFieldTests(DateTimeFieldTestCase):

    def setUp(self):
        self.default_input_formats = self.default_date_input_formats

    def test_init_no_input_formats(self):
        field = DateField()
        self.assertInputFormats(field, self.default_input_formats)

    def test_init_empty_input_formats(self):
        field = DateField(input_formats=())
        self.assertInputFormats(field, self.default_input_formats)

    def test_init_custom_input_formats(self):
        input_formats = ('%m/%d/%Y', '%m/%d/%y')
        field = DateField(input_formats=input_formats)
        self.assertInputFormats(field, input_formats)


class DateTimeFieldTests(DateTimeFieldTestCase):

    def setUp(self):
        self.default_input_formats = self.default_datetime_input_formats

    def test_init_no_input_formats(self):
        field = DateTimeField()
        self.assertInputFormats(field, self.default_input_formats)

    def test_init_empty_input_formats(self):
        field = DateTimeField(input_formats=())
        self.assertInputFormats(field, self.default_input_formats)

    def test_init_custom_input_formats(self):
        input_formats = ('%m/%d/%Y %H:%M', '%m/%d/%y %H:%M')
        field = DateTimeField(input_formats=input_formats)
        self.assertInputFormats(field, input_formats)


class SplitDateTimeFieldTests(DateTimeFieldTestCase):

    default_time_input_formats = formats.get_format_lazy('TIME_INPUT_FORMATS')

    def test_init_no_input_formats(self):
        field = SplitDateTimeField()
        date_field, time_field = field.fields
        self.assertInputFormats(date_field, self.default_date_input_formats)
        self.assertInputFormats(time_field, self.default_time_input_formats)

    def test_init_empty_input_formats(self):
        field = SplitDateTimeField(input_date_formats=(),
                                   input_time_formats=())
        date_field, time_field = field.fields
        self.assertInputFormats(date_field, self.default_date_input_formats)
        self.assertInputFormats(time_field, ())

    def test_init_custom_input_formats(self):
        date_input_formats = ('%m/%d/%Y', '%m/%d/%y')
        time_input_formats = ('%H:%M', '%H:%M:%S')
        field = SplitDateTimeField(input_date_formats=date_input_formats,
                                   input_time_formats=time_input_formats)
        date_field, time_field = field.fields
        self.assertInputFormats(date_field, date_input_formats)
        self.assertInputFormats(time_field, time_input_formats)


class IBANTests(TestCase):
    def test_iban_validator(self):
        valid = [
            'GB82WeST12345698765432',
            'GB82 WEST 1234 5698 7654 32',

            'GR1601101250000000012300695',
            'GR16-0110-1250-0000-0001-2300-695',

            'GB29NWBK60161331926819',
            'GB29N-WB K6016-13319-26819',

            'SA0380000000608010167519',
            'SA0380 0 0000 06 0 8 0 1 0 1 6 7 519 ',

            'CH9300762011623852957',
            'IL620108000000099999999'
        ]

        invalid = {
            'GB82WEST1234569876543': 'GB IBANs must contain 22 characters.',
            'CA34CIBC123425345': 'CA is not a valid country code for IBAN.',
            'GB29ÉWBK60161331926819': 'is not a valid character for IBAN.',
            'SA0380000000608019167519': 'Not a valid IBAN.',
        }

        for iban in valid:
            IBANValidator(iban)

        for iban in invalid:
            self.assertRaisesMessage(ValidationError,  invalid[iban], IBANValidator(), iban)

    def test_iban_fields(self):
        """ Test the IBAN model and form field. """
        valid = {
            'NL02ABNA0123456789': 'NL02ABNA0123456789',
            'Nl02aBNa0123456789': 'NL02ABNA0123456789',
            'NL02 ABNA 0123 4567 89': 'NL02ABNA0123456789',
            'NL02-ABNA-0123-4567-89': 'NL02ABNA0123456789',

            'NL91ABNA0417164300': 'NL91ABNA0417164300',
            'NL91 ABNA 0417 1643 00': 'NL91ABNA0417164300',
            'NL91-ABNA-0417-1643-00': 'NL91ABNA0417164300',

            'MU17BOMM0101101030300200000MUR': 'MU17BOMM0101101030300200000MUR',
            'MU17 BOMM 0101 1010 3030 0200 000M UR': 'MU17BOMM0101101030300200000MUR',
            'MU 17BO MM01011010 3030-02 000-00M UR': 'MU17BOMM0101101030300200000MUR',

            'BE68539007547034': 'BE68539007547034',
            'BE68 5390 0754 7034': 'BE68539007547034',
            'BE-685390075470 34': 'BE68539007547034',
        }

        invalid = {
            'NL02ABNA012345678999': ['NL IBANs must contain 18 characters.'],
            'NL02 ABNA 0123 4567 8999': ['NL IBANs must contain 18 characters.'],

            'NL91ABNB0417164300': ['Not a valid IBAN.'],
            'NL91 ABNB 0417 1643 00': ['Not a valid IBAN.'],

            'MU17BOMM0101101030300200000MUR12345': [
                'MU IBANs must contain 30 characters.',
                'Ensure this value has at most 34 characters (it has 35).'],
            'MU17 BOMM 0101 1010 3030 0200 000M UR12 345': [
                'MU IBANs must contain 30 characters.',
                'Ensure this value has at most 34 characters (it has 35).'],

            # This IBAN should only be valid only if the Nordea extensions are turned on.
            'EG1100006001880800100014553': ['EG is not a valid country code for IBAN.'],
            'EG11 0000 6001 8808 0010 0014 553': ['EG is not a valid country code for IBAN.']
        }

        self.assertFieldOutput(IBANFormField, valid=valid, invalid=invalid)

        # Test valid inputs for model field.
        iban_model_field = IBANField()
        for input, output in valid.items():
            self.assertEqual(iban_model_field.clean(input, None), output)

        # Invalid inputs for model field.
        for input, errors in invalid.items():
            with self.assertRaises(ValidationError) as context_manager:
                iban_model_field.clean(input, None)
            # The error messages for models are in a different order.
            errors.reverse()
            self.assertEqual(context_manager.exception.messages, errors)

    def test_nordea_extensions(self):
        """ Test a valid IBAN in the Nordea extensions. """
        iban_validator = IBANValidator(use_nordea_extensions=True)
        # Run the validator to ensure there are no ValidationErrors raised.
        iban_validator('Eg1100006001880800100014553')

    def test_form_field_formatting(self):
        iban_form_field = IBANFormField()
        self.assertEqual(iban_form_field.prepare_value('NL02ABNA0123456789'), 'NL02 ABNA 0123 4567 89')
        self.assertEqual(iban_form_field.prepare_value('NL02 ABNA 0123 4567 89'), 'NL02 ABNA 0123 4567 89')
        self.assertIsNone(iban_form_field.prepare_value(None))

    def test_include_countries(self):
        """ Test the IBAN model and form include_countries feature. """
        include_countries = ('NL', 'BE', 'LU')

        valid = {
            'NL02ABNA0123456789': 'NL02ABNA0123456789',
            'BE68539007547034': 'BE68539007547034',
            'LU280019400644750000': 'LU280019400644750000'
        }

        invalid = {
            # This IBAN is valid but not for the configured countries.
            'GB82WEST12345698765432': ['GB IBANs are not allowed in this field.']
        }

        self.assertFieldOutput(IBANFormField, field_kwargs={'include_countries': include_countries},
                               valid=valid, invalid=invalid)

        # Test valid inputs for model field.
        iban_model_field = IBANField(include_countries=include_countries)
        for input, output in valid.items():
            self.assertEqual(iban_model_field.clean(input, None), output)

        # Invalid inputs for model field.
        for input, errors in invalid.items():
            with self.assertRaises(ValidationError) as context_manager:
                iban_model_field.clean(input, None)
            # The error messages for models are in a different order.
            errors.reverse()
            self.assertEqual(context_manager.exception.messages, errors)

    def test_misconfigured_include_countries(self):
        """ Test that an IBAN field or model raises an error when asked to validate a country not part of IBAN.
        """
        # Test an unassigned ISO 3166-1 country code so that the tests will work even if a country joins IBAN.
        self.assertRaises(ImproperlyConfigured, IBANValidator, include_countries=('JJ',))
        self.assertRaises(ImproperlyConfigured, IBANValidator, use_nordea_extensions=True, include_countries=('JJ',))

        # Test a Nordea IBAN when Nordea extensions are turned off.
        self.assertRaises(ImproperlyConfigured, IBANValidator, include_countries=('AO',))
