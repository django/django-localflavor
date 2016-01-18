from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.kw.forms import KWCivilIDNumberField


class KWLocalFlavorTests(SimpleTestCase):
    def test_KWCivilIDNumberField(self):
        error_invalid = ['Enter a valid Kuwaiti Civil ID number']
        valid = {
            '282040701483': '282040701483',
            '300092400929': '300092400929',
            '304022600325': '304022600325',
        }
        invalid = {
            '289332013455': error_invalid,
            '300000000005': error_invalid,
            '289332Ol3455': error_invalid,
            '2*9332013455': error_invalid,
        }
        self.assertFieldOutput(KWCivilIDNumberField, valid, invalid)
