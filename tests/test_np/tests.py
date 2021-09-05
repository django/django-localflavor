from django.test import SimpleTestCase
from localflavor.np.forms import NPDistrictSelect , NPProvinceSelect, NPZoneSelect, NPPostalCodeFormField
from .selectfields_html import  all_districts_select, provinces_select, zones_select

class NepalDetails(SimpleTestCase):
    """
        This Test class tests all the selectbox
        fields and Postal Code Fields.
    """
    def test_NPDistrictSelect(self):
        field = NPDistrictSelect()
        self.assertHTMLEqual(field.render('district', 'achham'), all_districts_select)

    def test_NPProvinceSelect(self):
        field = NPProvinceSelect()
        self.assertHTMLEqual(field.render('province','bagmati'), provinces_select)

    def test_NPZoneSelect(self):
        field = NPZoneSelect()
        self.assertHTMLEqual(field.render('zone','mahakali'), zones_select)

    def test_NPPostalCodeFieldTest(self):
        error_format = ['Enter a postal code in format XXXXX']
        valid = {
            '12345': '12345',
            '00000':'00000',
            '23476': '23476'
        }
        invalid = {
            '12345_123': error_format,
            '1234-123': error_format,
            'abcde-abc': error_format,
            '12345-': error_format,
            '-123': error_format,
        }
        self.assertFieldOutput(NPPostalCodeFormField, valid, invalid)
