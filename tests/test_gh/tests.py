from django.test import SimpleTestCase
from localflavor.gh.forms import  GHRegionSelect,  GHPostalCodeFormField
from .selectfields_html import   regions_select

class GhanaDetails(SimpleTestCase):
    """
        This Test class tests all the selectbox
        fields and Postal Code Fields.
    """
    
    def test_GHRegionSelect(self):
        field = GHRegionSelect()
        self.assertHTMLEqual(field.render('region','ahafo'), regions_select)

    
    def test_GHPostalCodeFieldTest(self):
        error_format = ['Enter a postal code in format XXXXX']
        valid = {
            'GA105': 'GA105',
            'GA170':'GA170',
            'GA205': 'GA205'
        }
        invalid = {
            'GA_205': error_format,
            'GA-205': error_format,
            '123-85': error_format,
            'abcd-': error_format,
            '-123': error_format,
        }
        self.assertFieldOutput(GHPostalCodeFormField, valid, invalid)