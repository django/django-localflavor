from __future__ import unicode_literals

from django.test import SimpleTestCase

from .forms import KWCivilIDNumberField


class KWLocalFlavorTests(SimpleTestCase):
    def test_KWCivilIDNumberField(self):
        error_invalid = ['Enter a valid Kuwaiti Civil ID number']
        valid = {
            '282040701483': '282040701483',
        }
        invalid = {
            '289332013455': error_invalid,
        }
        self.assertFieldOutput(KWCivilIDNumberField, valid, invalid)
