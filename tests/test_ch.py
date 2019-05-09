from django.test import SimpleTestCase
from django.utils.translation import gettext as _
from django.utils.translation import override

from localflavor.ch.forms import CHIdentityCardNumberField, CHSocialSecurityNumberField, CHStateSelect, CHZipCodeField


class CHLocalFlavorTests(SimpleTestCase):

    def test_CHStateSelect(self):
        with override('en'):
            f = CHStateSelect()
            out = '''<select name="state">
<option value="AG" selected="selected">Aargau</option>
<option value="AI">Appenzell Innerrhoden</option>
<option value="AR">Appenzell Ausserrhoden</option>
<option value="BS">Basel-Stadt</option>
<option value="BL">Basel-Land</option>
<option value="BE">Berne</option>
<option value="FR">Fribourg</option>
<option value="GE">Geneva</option>
<option value="GL">Glarus</option>
<option value="GR">Graubuenden</option>
<option value="JU">Jura</option>
<option value="LU">Lucerne</option>
<option value="NE">Neuchatel</option>
<option value="NW">Nidwalden</option>
<option value="OW">Obwalden</option>
<option value="SH">Schaffhausen</option>
<option value="SZ">Schwyz</option>
<option value="SO">Solothurn</option>
<option value="SG">St. Gallen</option>
<option value="TG">Thurgau</option>
<option value="TI">Ticino</option>
<option value="UR">Uri</option>
<option value="VS">Valais</option>
<option value="VD">Vaud</option>
<option value="ZG">Zug</option>
<option value="ZH">Zurich</option>
</select>'''
            self.assertHTMLEqual(f.render('state', 'AG'), out)

    def test_CHZipCodeField(self):
        error_format = [_('Enter a valid postal code in the range and format 1XXX - 9XXX.')]
        valid = {
            '1234': '1234',
            '9999': '9999',
        }
        invalid = {
            '0000': error_format,
            '800x': error_format,
            '80 00': error_format,
            '99990': error_format,
        }
        self.assertFieldOutput(CHZipCodeField, valid, invalid)

    def test_CHIdentityCardNumberField(self):
        error_format = [_('Enter a valid Swiss identity or passport card number in X1234567<0 or 1234567890 format.')]
        valid = {
            'C1234567<0': 'C1234567<0',
            '2123456700': '2123456700',
        }
        invalid = {
            'C1234567<1': error_format,
            '2123456701': error_format,
        }
        self.assertFieldOutput(CHIdentityCardNumberField, valid, invalid)

    def test_CHSocialSecurityNumberField(self):
        error_format = [_('Enter a valid Swiss Social Security number in 756.XXXX.XXXX.XX format.')]
        valid = {
            '756.1234.5678.97': '756.1234.5678.97',
            '756.9217.0769.85': '756.9217.0769.85',
        }
        invalid = {
            '756.1234.5678.96': error_format,
            '757.1234.5678.97': error_format,
            '756.1234.5678': error_format,
        }
        self.assertFieldOutput(CHSocialSecurityNumberField, valid, invalid)
