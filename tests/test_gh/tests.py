from django.test import TransactionTestCase

from localflavor.gh.forms import GHRegionSelect

from .models import GHPlace
from .selectfields_html import regions_select


class GhanaDetails(TransactionTestCase):
    """
        This Test class tests all the selectbox
        fields.
    """

    def test_GHRegionSelect(self):
        field = GHRegionSelect()
        self.assertHTMLEqual(field.render('region','ahafo'), regions_select)

    def test_GHRegionField(self):
        place = GHPlace()
        place.region = 'ashanti'
        place.clean_fields()
        place.save()
        self.assertEqual(place.get_region_display(), 'Ashanti')

