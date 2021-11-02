from django.test import TestCase

from localflavor.np.forms import NPDistrictSelect, NPPostalCodeFormField, NPProvinceSelect, NPZoneSelect

from .selectfields_html import districts_select, provinces_select, zones_select

from .forms import NepaliPlaceForm


class NepalDetails(TestCase):
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


class NepaliPlaceFormTest(TestCase):
    """
        This Test class tests the NepaliPlaceForm
    """
    def setUp(self):
        self.form = NepaliPlaceForm({
            'postal': '12345',
            'district': 'achham',
            'zone': 'mahakali',
            'province': 'bagmati',
        })

    def test_get_display_methods(self):
        """Test that the get_*_display() methods are added to the model instances."""
        place = self.form.save()
        self.assertEqual(place.get_district_display(), 'Achham')
        self.assertEqual(place.get_zone_display(), 'Mahakali')
        self.assertEqual(place.get_province_display(), 'Bagmati')

    def test_errors(self):
        """Test that required NepaliFormFields throw appropriate errors."""
        form = NepaliPlaceForm({
            'postal': 'xxx',
            'district': 'Invalid district',
            'zone': 'Invalid zone',
            'province': 'Invalid province',

        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['district'], ['Select a valid choice. Invalid district is not one of the available choices.']
        )
        self.assertEqual(
            form.errors['zone'], ['Select a valid choice. Invalid zone is not one of the available choices.']
        )
        self.assertEqual(
            form.errors['province'], ['Select a valid choice. Invalid province is not one of the available choices.']
        )
        self.assertEqual(form.errors['postal'], ['Enter a postal code in format XXXXX'])

