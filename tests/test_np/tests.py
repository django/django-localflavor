from django.test import TransactionTestCase

from localflavor.np.forms import NPDistrictSelect, NPPostalCodeFormField, NPProvinceSelect, NPZoneSelect

from .selectfields_html import districts_select, provinces_select, zones_select

from .models import NepalianPlace


class NepalDetails(TransactionTestCase):
    """
        This Test class tests all the selectbox
        fields and Postal Code Fields.
    """
    def test_NPDistrictSelect(self):
        field = NPDistrictSelect()
        self.assertHTMLEqual(field.render('district', 'achham'), districts_select)

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


    def test_NPDistrictField(self):
        place = NepalianPlace()
        place.district = 'achham'
        place.clean_fields()
        place.save()
        self.assertEqual(place.get_district_display(), 'Achham')

    def test_NPZoneField(self):
        place = NepalianPlace()
        place.zone = 'mahakali'
        place.clean_fields()
        place.save()
        self.assertEqual(place.get_zone_display(), 'Mahakali')

    def test_NPProvinceField(self):
        place = NepalianPlace()
        place.province = 'bagmati'
        place.clean_fields()
        place.save()
        self.assertEqual(place.get_province_display(), 'Bagmati')



