from django.test import SimpleTestCase

from localflavor.lv.forms import LVMunicipalitySelect, LVPersonalCodeField, LVPostalCodeField


class LVLocalFlavorTests(SimpleTestCase):
    def test_LVPersonalCodeField(self):
        invalid_format = ['Enter a Latvian personal code in format XXXXXX-XXXXX.']
        invalid = ['Enter a valid Latvian personal code.']

        valid = {
            '261155-10410': '261155-10410',
            '010100-10005': '010100-10005',  # smallest valid code
            '311299-29999': '311299-29999',  # greatest valid code
            '290212-21232': '290212-21232',  # leap year
        }
        invalid = {
            '26115510410': invalid_format,  # missing dash
            '261155-90414': invalid_format,  # invalid century
            '123456-12345': invalid,  # invalid checksum
            '310200-10006': invalid,  # invalid date
            '000000-10007': invalid,  # invalid day/month
            '290214-21234': invalid,  # not leap year
        }

        self.assertFieldOutput(LVPersonalCodeField, valid, invalid)

    def test_LVPostalCodeField(self):
        invalid = [LVPostalCodeField().error_messages['invalid']]

        valid = {
            'LV-1023': 'LV-1023',
            'lv - 5750': 'LV-5750',
            '3036': 'LV-3036',
        }
        invalid = {
            '123': invalid,
            '12345': invalid,
            'LV-12345': invalid,
            '0123': invalid,  # out of range
            'LV-9999': invalid,  # out of range
        }
        self.assertFieldOutput(LVPostalCodeField, valid, invalid)

    def test_LVMunicipalitySelect(self):
        f = LVMunicipalitySelect()
        expected = '''
<select name="municipality">
<option value="DGV">Daugavpils</option>
<option value="JEL">Jelgava</option>
<option value="JUR">Jūrmala</option>
<option value="LPX">Liepāja</option>
<option value="REZ">Rēzekne</option>
<option value="RIX">Riga</option>
<option value="VEN">Ventspils</option>
<option value="002">Aizkraukle municipality</option>
<option value="007">Alūksne municipality</option>
<option value="011">Ādaži municipality</option>
<option value="015">Balvi municipality</option>
<option value="016">Bauska municipality</option>
<option value="022">Cēsis municipality</option>
<option value="026">Dobele municipality</option>
<option value="033">Gulbene municipality</option>
<option value="041">Jelgava municipality</option>
<option value="042">Jēkabpils municipality</option>
<option value="047">Krāslava municipality</option>
<option value="050">Kuldīga municipality</option>
<option value="052">Ķekava municipality</option>
<option value="054">Limbaži municipality</option>
<option value="056">Līvāni municipality</option>
<option value="058">Ludza municipality</option>
<option value="059">Madona municipality</option>
<option value="062">Mārupe municipality</option>
<option value="067">Ogre municipality</option>
<option value="068">Olaine municipality</option>
<option value="073">Preiļi municipality</option>
<option value="077">Rēzekne municipality</option>
<option value="080">Ropaži municipality</option>
<option value="087">Salaspils municipality</option>
<option value="088">Saldus municipality</option>
<option value="089">Saulkrasti municipality</option>
<option value="091">Sigulda municipality</option>
<option value="094">Smiltene municipality</option>
<option value="097">Talsi municipality</option>
<option value="099">Tukums municipality</option>
<option value="101">Valka municipality</option>
<option value="102">Varakļāni municipality</option>
<option value="106">Ventspils municipality</option>
<option value="111">Augšdaugava municipality</option>
<option value="112">Dienvidkurzeme municipality</option>
<option value="113">Valmiera municipality</option>
</select>'''
        self.assertHTMLEqual(f.render('municipality', None), expected)
