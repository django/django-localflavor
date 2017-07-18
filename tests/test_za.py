from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.za.forms import ZAIDField, ZAPostCodeField, ZAProvinceSelect


class ZALocalFlavorTests(SimpleTestCase):
    def test_ZAIDField(self):
        error_invalid = ['Enter a valid South African ID number']
        valid = {
            '0002290001003': '0002290001003',
            '000229 0001 003': '0002290001003',
        }
        invalid = {
            '0102290001001': error_invalid,
            '811208': error_invalid,
            '0002290001004': error_invalid,
        }
        self.assertFieldOutput(ZAIDField, valid, invalid)

    def test_ZAPostCodeField(self):
        error_invalid = ['Enter a valid South African postal code']
        valid = {
            '0000': '0000',
        }
        invalid = {
            'abcd': error_invalid,
            ' 7530': error_invalid,
        }
        self.assertFieldOutput(ZAPostCodeField, valid, invalid)

    def test_ZAProvinceSelect(self):
        f = ZAProvinceSelect()
        out = '''<select name="province">
<option value="EC" selected="selected">Eastern Cape</option>
<option value="FS">Free State</option>
<option value="GP">Gauteng</option>
<option value="KN">KwaZulu-Natal</option>
<option value="LP">Limpopo</option>
<option value="MP">Mpumalanga</option>
<option value="NC">Northern Cape</option>
<option value="NW">North West</option>
<option value="WC">Western Cape</option>
</select>'''
        self.assertHTMLEqual(f.render('province', 'EC'), out)
