# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase

from localflavor.generic.forms import IBANFormField
from localflavor.generic.models import IBANField
from localflavor.generic.validators import IBANValidator


class IBANTests(TestCase):
    def test_iban_validator(self):
        valid = [
            'GB82WEST12345698765432',
            'GR1601101250000000012300695',
            'GB29NWBK60161331926819',
            'SA0380000000608010167519',
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
            'NL91ABNA0417164300': 'NL91ABNA0417164300',
            'MU17BOMM0101101030300200000MUR': 'MU17BOMM0101101030300200000MUR',
            'BE68539007547034': 'BE68539007547034',
        }

        invalid = {
            'NL02ABNA012345678999': ['NL IBANs must contain 18 characters.'],
            'NL91ABNB0417164300': ['Not a valid IBAN.'],
            'MU17BOMM0101101030300200000MUR12345': [
                'MU IBANs must contain 30 characters.',
                'Ensure this value has at most 34 characters (it has 35).'],

            # This IBAN should only be valid only if the Nordea extensions are turned on.
            'EG1100006001880800100014553': ['EG is not a valid country code for IBAN.']
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
        iban_validator('EG1100006001880800100014553')
