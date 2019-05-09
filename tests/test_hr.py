from django.test import SimpleTestCase

from localflavor.hr.forms import (HRCountySelect, HRJMBAGField, HRJMBGField, HRLicensePlateField,
                                  HRLicensePlatePrefixSelect, HROIBField, HRPostalCodeField)


class HRLocalFlavorTests(SimpleTestCase):
    def test_HRCountySelect(self):
        f = HRCountySelect()
        out = '''<select name="county">
<option value="GZG" selected="selected">Grad Zagreb</option>
<option value="BBŽ">Bjelovarsko-bilogorska županija</option>
<option value="BPŽ">Brodsko-posavska županija</option>
<option value="DNŽ">Dubrovačko-neretvanska županija</option>
<option value="IŽ">Istarska županija</option>
<option value="KŽ">Karlovačka županija</option>
<option value="KKŽ">Koprivničko-križevačka županija</option>
<option value="KZŽ">Krapinsko-zagorska županija</option>
<option value="LSŽ">Ličko-senjska županija</option>
<option value="MŽ">Međimurska županija</option>
<option value="OBŽ">Osječko-baranjska županija</option>
<option value="PSŽ">Požeško-slavonska županija</option>
<option value="PGŽ">Primorsko-goranska županija</option>
<option value="SMŽ">Sisačko-moslavačka županija</option>
<option value="SDŽ">Splitsko-dalmatinska županija</option>
<option value="ŠKŽ">Šibensko-kninska županija</option>
<option value="VŽ">Varaždinska županija</option>
<option value="VPŽ">Virovitičko-podravska županija</option>
<option value="VSŽ">Vukovarsko-srijemska županija</option>
<option value="ZDŽ">Zadarska županija</option>
<option value="ZGŽ">Zagrebačka županija</option>
</select>'''
        self.assertHTMLEqual(f.render('county', 'GZG'), out)

    def test_HRLicensePlatePrefixSelect(self):
        f = HRLicensePlatePrefixSelect()
        out = '''<select name="license">
<option value="BJ" selected="selected">BJ</option>
<option value="BM">BM</option>
<option value="ČK">ČK</option>
<option value="DA">DA</option>
<option value="DE">DE</option>
<option value="DJ">DJ</option>
<option value="DU">DU</option>
<option value="GS">GS</option>
<option value="IM">IM</option>
<option value="KA">KA</option>
<option value="KC">KC</option>
<option value="KR">KR</option>
<option value="KT">KT</option>
<option value="KŽ">KŽ</option>
<option value="MA">MA</option>
<option value="NA">NA</option>
<option value="NG">NG</option>
<option value="OG">OG</option>
<option value="OS">OS</option>
<option value="PU">PU</option>
<option value="PŽ">PŽ</option>
<option value="RI">RI</option>
<option value="SB">SB</option>
<option value="SK">SK</option>
<option value="SL">SL</option>
<option value="ST">ST</option>
<option value="ŠI">ŠI</option>
<option value="VK">VK</option>
<option value="VT">VT</option>
<option value="VU">VU</option>
<option value="VŽ">VŽ</option>
<option value="ZD">ZD</option>
<option value="ZG">ZG</option>
<option value="ŽU">ŽU</option>
</select>'''
        self.assertHTMLEqual(f.render('license', 'BJ'), out)

    def test_HRLicensePlateField(self):
        error_invalid = ['Enter a valid vehicle license plate number']
        error_area = ['Enter a valid location code']
        error_number = ['Number part cannot be zero']
        valid = {
            'ZG 1234-AA': 'ZG 1234-AA',
            'ZG 123-A': 'ZG 123-A',
        }
        invalid = {
            'PV12345': error_invalid,
            'PV1234AA': error_area,
            'ZG0000CC': error_number,
        }
        self.assertFieldOutput(HRLicensePlateField, valid, invalid)

    def test_HRPostalCodeField(self):
        error_invalid = ['Enter a valid 5 digit postal code']
        valid = {
            '10000': '10000',
            '35410': '35410',
        }
        invalid = {
            'ABCD': error_invalid,
            '99999': error_invalid,
        }
        self.assertFieldOutput(HRPostalCodeField, valid, invalid)

    def test_HROIBField(self):
        error_invalid = ['Enter a valid 11 digit OIB']
        valid = {
            '12345678901': '12345678901',
        }
        invalid = {
            '1234567890': ['Ensure this value has at least 11 characters (it has 10).'] + error_invalid,
            'ABCDEFGHIJK': error_invalid,
        }
        self.assertFieldOutput(HROIBField, valid, invalid)

    def test_HRJMBGField(self):
        error_invalid = ['Enter a valid 13 digit JMBG']
        error_date = ['Error in date segment']
        valid = {
            '1211984302155': '1211984302155',
            '2701984307107': '2701984307107',
        }
        invalid = {
            '1211984302156': error_invalid,
            'ABCDEFG': error_invalid,
            '9999999123456': error_date,
        }
        self.assertFieldOutput(HRJMBGField, valid, invalid)

    def test_HRJMBAGField(self):
        error_invalid = ['Enter a valid 19 digit JMBAG starting with 601983']
        error_copy = ['Card issue number cannot be zero']
        valid = {
            '601983 11 0130185856 4': '6019831101301858564',
        }
        invalid = {
            '601983 11 0130185856 5': error_invalid,
            '601983 01 0130185856 4': error_copy,
        }
        self.assertFieldOutput(HRJMBAGField, valid, invalid)
