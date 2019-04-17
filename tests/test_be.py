from django.test import SimpleTestCase

from localflavor.be.forms import BEPostalCodeField, BEProvinceSelect, BERegionSelect


class BELocalFlavorTests(SimpleTestCase):
    def test_BEPostalCodeField(self):
        error_format = ['Enter a valid postal code in the range and format 1XXX - 9XXX.']
        valid = {
            '1451': '1451',
            '2540': '2540',
        }
        invalid = {
            '0287': error_format,
            '14309': error_format,
            '873': error_format,
            '35 74': error_format,
            '859A': error_format,
        }
        self.assertFieldOutput(BEPostalCodeField, valid, invalid)

    def test_BERegionSelect(self):
        f = BERegionSelect()
        out = '''<select name="regions">
<option value="BRU">Brussels Capital Region</option>
<option value="VLG" selected="selected">Flemish Region</option>
<option value="WAL">Wallonia</option>
</select>'''
        self.assertHTMLEqual(f.render('regions', 'VLG'), out)

    def test_BEProvinceSelect(self):
        f = BEProvinceSelect()
        out = '''<select name="provinces">
<option value="VAN">Antwerp</option>
<option value="BRU">Brussels</option>
<option value="VOV">East Flanders</option>
<option value="VBR">Flemish Brabant</option>
<option value="WHT">Hainaut</option>
<option value="WLG" selected="selected">Liege</option>
<option value="VLI">Limburg</option>
<option value="WLX">Luxembourg</option>
<option value="WNA">Namur</option>
<option value="WBR">Walloon Brabant</option>
<option value="VWV">West Flanders</option>
</select>'''
        self.assertHTMLEqual(f.render('provinces', 'WLG'), out)
