from django.test import TestCase

from localflavor.ua.forms import UAPostalCodeField, UARegionSelect, UAVatNumberField
from localflavor.ua.ua_regions import UA_REGION_CHOICES

from .forms import UAFlavorTestForm


class UALocalFlavorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form = UAFlavorTestForm({
            'postal_code': '76000',
            'region': 'UA-26',
            'vat_number': '0000000000'
        })

    def test_get_display_methods(self):
        flavor = self.form.save()
        self.assertEqual(flavor.get_region_display(), 'Ivano-Frankivsk Oblast')

    def test_errors(self):
        form = UAFlavorTestForm({
            'postal_code': False,
            'region': False,
            'vat_number': False
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['postal_code'], ['Enter a valid postal code.'])
        self.assertEqual(
            form.errors['region'], ['Select a valid choice. False is not one of the available choices.']
        )
        self.assertEqual(form.errors['vat_number'], ['Enter a valid VAT number.'])

    def test_UARegionSelect(self):
        out = '<select name="region">\n'
        for choice in UA_REGION_CHOICES:
            out += '<option value="{}">{}</option>\n'.format(choice[0], choice[1])
        out += '</select>'
        self.assertHTMLEqual(UARegionSelect().render('region', None), out)

    def test_UAVatNumberField(self):
        error_format = ['Enter a valid VAT number.']
        valid = {
            '1111111111': '1111111111',
            1234567890: '1234567890',
            ' 0987654321 ': '0987654321'
        }
        invalid = {
            'abcdefghij': error_format,
            '123': ['Ensure this value has at least 10 characters (it has 3).'] + error_format,
            '98765432100': ['Ensure this value has at most 10 characters (it has 11).'] + error_format
        }
        self.assertFieldOutput(UAVatNumberField, valid, invalid)

    def test_UAPostalCodeField(self):
        error_format = ['Enter a valid postal code.']
        valid = {
            '76000': '76000',
            10101: '10101',
            ' 09876 ': '09876'
        }
        invalid = {
            'abcde': error_format,
            '00000': error_format,
            '123': ['Ensure this value has at least 5 characters (it has 3).'] + error_format,
            '987654': ['Ensure this value has at most 5 characters (it has 6).'] + error_format
        }
        self.assertFieldOutput(UAPostalCodeField, valid, invalid)
