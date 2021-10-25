from django.test import SimpleTestCase
from localflavor.gh.forms import  GHRegionSelect
from .selectfields_html import   regions_select

class GhanaDetails(SimpleTestCase):
    """
        This Test class tests all the selectbox
        fields.
    """

    def test_GHRegionSelect(self):
        field = GHRegionSelect()
        self.assertHTMLEqual(field.render('region','ahafo'), regions_select)