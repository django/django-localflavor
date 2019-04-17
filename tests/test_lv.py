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
<option value="JKB">Jēkabpils</option>
<option value="JUR">Jūrmala</option>
<option value="LPX">Liepāja</option>
<option value="REZ">Rēzekne</option>
<option value="RIX">Riga</option>
<option value="VMR">Valmiera</option>
<option value="VEN">Ventspils</option>
<option value="001">Aglona municipality</option>
<option value="002">Aizkraukle municipality</option>
<option value="003">Aizpute municipality</option>
<option value="004">Aknīste municipality</option>
<option value="005">Aloja municipality</option>
<option value="006">Alsunga municipality</option>
<option value="007">Alūksne municipality</option>
<option value="008">Amata municipality</option>
<option value="009">Ape municipality</option>
<option value="010">Auce municipality</option>
<option value="011">Ādaži municipality</option>
<option value="012">Babīte municipality</option>
<option value="013">Baldone municipality</option>
<option value="014">Baltinava municipality</option>
<option value="015">Balvi municipality</option>
<option value="016">Bauska municipality</option>
<option value="017">Beverīna municipality</option>
<option value="018">Brocēni municipality</option>
<option value="019">Burtnieki municipality</option>
<option value="020">Carnikava municipality</option>
<option value="021">Cesvaine municipality</option>
<option value="022">Cēsis municipality</option>
<option value="023">Cibla municipality</option>
<option value="024">Dagda municipality</option>
<option value="025">Daugavpils municipality</option>
<option value="026">Dobele municipality</option>
<option value="027">Dundaga municipality</option>
<option value="028">Durbe municipality</option>
<option value="029">Engure municipality</option>
<option value="030">Ērgļi municipality</option>
<option value="031">Garkalne municipality</option>
<option value="032">Grobiņa municipality</option>
<option value="033">Gulbene municipality</option>
<option value="034">Iecava municipality</option>
<option value="035">Ikšķile municipality</option>
<option value="036">Ilūkste municipality</option>
<option value="037">Inčukalns municipality</option>
<option value="038">Jaunjelgava municipality</option>
<option value="039">Jaunpiebalga municipality</option>
<option value="040">Jaunpils municipality</option>
<option value="041">Jelgava municipality</option>
<option value="042">Jēkabpils municipality</option>
<option value="043">Kandava municipality</option>
<option value="044">Kārsava municipality</option>
<option value="045">Kocēni municipality</option>
<option value="046">Koknese municipality</option>
<option value="047">Krāslava municipality</option>
<option value="048">Krimulda municipality</option>
<option value="049">Krustpils municipality</option>
<option value="050">Kuldīga municipality</option>
<option value="051">Ķegums municipality</option>
<option value="052">Ķekava municipality</option>
<option value="053">Lielvārde municipality</option>
<option value="054">Limbaži municipality</option>
<option value="055">Līgatne municipality</option>
<option value="056">Līvāni municipality</option>
<option value="057">Lubāna municipality</option>
<option value="058">Ludza municipality</option>
<option value="059">Madona municipality</option>
<option value="060">Mazsalaca municipality</option>
<option value="061">Mālpils municipality</option>
<option value="062">Mārupe municipality</option>
<option value="063">Mērsrags municipality</option>
<option value="064">Naukšēni municipality</option>
<option value="065">Nereta municipality</option>
<option value="066">Nīca municipality</option>
<option value="067">Ogre municipality</option>
<option value="068">Olaine municipality</option>
<option value="069">Ozolnieki municipality</option>
<option value="070">Pārgauja municipality</option>
<option value="071">Pāvilosta municipality</option>
<option value="072">Pļaviņas municipality</option>
<option value="073">Preiļi municipality</option>
<option value="074">Priekule municipality</option>
<option value="075">Priekuļi municipality</option>
<option value="076">Rauna municipality</option>
<option value="077">Rēzekne municipality</option>
<option value="078">Riebiņi municipality</option>
<option value="079">Roja municipality</option>
<option value="080">Ropaži municipality</option>
<option value="081">Rucava municipality</option>
<option value="082">Rugāji municipality</option>
<option value="083">Rundāle municipality</option>
<option value="084">Rūjiena municipality</option>
<option value="085">Sala municipality</option>
<option value="086">Salacgrīva municipality</option>
<option value="087">Salaspils municipality</option>
<option value="088">Saldus municipality</option>
<option value="089">Saulkrasti municipality</option>
<option value="090">Sēja municipality</option>
<option value="091">Sigulda municipality</option>
<option value="092">Skrīveri municipality</option>
<option value="093">Skrunda municipality</option>
<option value="094">Smiltene municipality</option>
<option value="095">Stopiņi municipality</option>
<option value="096">Strenči municipality</option>
<option value="097">Talsi municipality</option>
<option value="098">Tērvete municipality</option>
<option value="099">Tukums municipality</option>
<option value="100">Vaiņode municipality</option>
<option value="101">Valka municipality</option>
<option value="102">Varakļāni municipality</option>
<option value="103">Vārkava municipality</option>
<option value="104">Vecpiebalga municipality</option>
<option value="105">Vecumnieki municipality</option>
<option value="106">Ventspils municipality</option>
<option value="107">Viesīte municipality</option>
<option value="108">Viļaka municipality</option>
<option value="109">Viļāni municipality</option>
<option value="110">Zilupe municipality</option>
</select>'''
        self.assertHTMLEqual(f.render('municipality', None), expected)
