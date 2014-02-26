from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.it.forms import (ITZipCodeField, ITRegionSelect,
                                  ITSocialSecurityNumberField,
                                  ITVatNumberField, ITPhoneNumberField)


class ITLocalFlavorTests(SimpleTestCase):
    def test_ITRegionSelect(self):
        f = ITRegionSelect()
        out = '''<select name="regions">
<option value="ABR">Abruzzo</option>
<option value="BAS">Basilicata</option>
<option value="CAL">Calabria</option>
<option value="CAM">Campania</option>
<option value="EMR">Emilia-Romagna</option>
<option value="FVG">Friuli-Venezia Giulia</option>
<option value="LAZ">Lazio</option>
<option value="LIG">Liguria</option>
<option value="LOM">Lombardia</option>
<option value="MAR">Marche</option>
<option value="MOL">Molise</option>
<option value="PMN" selected="selected">Piemonte</option>
<option value="PUG">Puglia</option>
<option value="SAR">Sardegna</option>
<option value="SIC">Sicilia</option>
<option value="TOS">Toscana</option>
<option value="TAA">Trentino-Alto Adige</option>
<option value="UMB">Umbria</option>
<option value="VAO">Valle d\u2019Aosta</option>
<option value="VEN">Veneto</option>
</select>'''
        self.assertHTMLEqual(f.render('regions', 'PMN'), out)

    def test_ITZipCodeField(self):
        error_invalid = ['Enter a valid zip code.']
        valid = {
            '00100': '00100',
        }
        invalid = {
            ' 00100': error_invalid,
        }
        self.assertFieldOutput(ITZipCodeField, valid, invalid)

    def test_ITSocialSecurityNumberField(self):
        error_invalid = ['Enter a valid Social Security number.']
        valid = {
            'LVSGDU99T71H501L': 'LVSGDU99T71H501L',
            'LBRRME11A01L736W': 'LBRRME11A01L736W',
            'lbrrme11a01l736w': 'LBRRME11A01L736W',
            'LBR RME 11A01 L736W': 'LBRRME11A01L736W',
        }
        invalid = {
            'LBRRME11A01L736A': error_invalid,
            '%BRRME11A01L736W': error_invalid,
        }
        self.assertFieldOutput(ITSocialSecurityNumberField, valid, invalid)

    def test_ITSocialSecurityNumberField_for_entities(self):
        error_invalid = ['Enter a valid Social Security number.']
        valid = {
            '07973780013': '07973780013',
            '7973780013': '07973780013',
            7973780013: '07973780013',
        }
        invalid = {
            '07973780014': error_invalid,
            'A7973780013': error_invalid,
        }
        self.assertFieldOutput(ITSocialSecurityNumberField, valid, invalid)

    def test_ITVatNumberField(self):
        error_invalid = ['Enter a valid VAT number.']
        valid = {
            '07973780013': '07973780013',
            '7973780013': '07973780013',
            7973780013: '07973780013',
        }
        invalid = {
            '07973780014': error_invalid,
            'A7973780013': error_invalid,
        }
        self.assertFieldOutput(ITVatNumberField, valid, invalid)

    def test_ITPhoneNumberField(self):
        error_format = ['Enter a valid Italian phone number.']
        valid = {
            '+39 347 1234567': '347 1234567',
            '39 347 123 4567': '347 1234567',
            '347-1234567': '347 1234567',
            '3471234567': '347 1234567',
            '+39 347 12345678': '347 12345678',
            '39 347 123 45678': '347 12345678',
            '347-12345678': '347 12345678',
            '34712345678': '347 12345678',
            '+39 347 123456': '347 123456',
            '39 347 123 456': '347 123456',
            '347-123456': '347 123456',
            '347123456': '347 123456',
            '+39 0861 12345678': '0861 12345678',
            '39 0861 1234 5678': '0861 12345678',
            '0861-12345678': '0861 12345678',
            '0861 12345': '0861 12345',
        }
        invalid = {
            '+44 347 1234567': error_format,
            '0471234567': error_format,
            '0861 123456789': error_format,
            '08661234567890': error_format,
        }
        self.assertFieldOutput(ITPhoneNumberField, valid, invalid)
