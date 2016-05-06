from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.kw.forms import KWCivilIDNumberField, KWGovernorateSelect


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

    def test_KWGovernorateSelect(self):
        f = KWGovernorateSelect()
        result = '''<select name="governorates">
<option value="AH">Ahmadi</option>
<option value="FA">Farwaniyah</option>
<option value="JA">Jahra</option>
<option value="KU" selected="selected">Capital</option>
<option value="HA">Hawalli</option>
<option value="MU">Mubarak Al Kabir</option>
</select>'''
        self.assertHTMLEqual(f.render('governorates', 'KU'), result)
