from django.test import TransactionTestCase
from localflavor.lk.forms import LKDistrictSelect, LKPostalCodeFormField, LKProvinceSelect

from .selectfields_html import districts_select, provinces_select
from .models import LKPlace


class SriLanakDetailsTests(TransactionTestCase):
    """
        This Test class tests all the selectbox
        fields and Postal Code Fields.
    """
    maxDiff = None

    def test_LKDistrictSelect(self):
        field = LKDistrictSelect()
        self.assertHTMLEqual(field.render('district', 'kandy'), districts_select)

    def test_LKProvinceSelect(self):
        field = LKProvinceSelect()
        self.assertHTMLEqual(field.render('province', 'central'), provinces_select)

    def test_LKPostalCodeFieldTest(self):
        error_format = ['Enter a postal code in format NNNNN']
        valid = {
            '12345': '12345',
            '00000': '00000',
            '11111': '11111'
        }
        invalid = {
            '12345_123': error_format,
            '1234-123': error_format,
            '-232': error_format,
            'abc_den': error_format,
            '2345-': error_format,
        }
        self.assertFieldOutput(LKPostalCodeFormField, valid, invalid)

    def test_LKDistrictField(self):
        place = LKPlace()
        place.district = 'kandy'
        place.clean_fields()
        place.save()
        self.assertEqual(place.get_district_display(), 'Kandy')

    def test_LKProvinceField(self):
        place = LKPlace()
        place.province = 'central'
        place.clean_fields()
        place.save()
        self.assertEqual(place.get_province_display(), 'Central')
