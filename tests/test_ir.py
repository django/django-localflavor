from django.test import SimpleTestCase

from localflavor.ir.forms import IRIDNumberField, IRPostalCodeField, IRProvinceSelect


class IRLocalFlavorTests(SimpleTestCase):
    def test_IRProvinceSelect(self):
        f = IRProvinceSelect()
        out = '''
        <select name="province">
            <option value="AL">Alborz</option>
            <option value="AR">Ardabil</option>
            <option value="AE">Azerbaijan East</option>
            <option value="AW">Azerbaijan Wast</option>
            <option value="BU">Bushehr</option>
            <option value="CM">Chahar Mahaal and Bakhtiari</option>
            <option value="FA">Fars</option>
            <option value="GI">Gilan</option>
            <option value="GO">Golestan</option>
            <option value="HA">Hamadan</option>
            <option value="HO">Hormozgan</option>
            <option value="IL">Ilam</option>
            <option value="IS">Isfahan</option>
            <option value="KE">Kerman</option>
            <option value="KM">Kermanshah</option>
            <option value="KN">Khorasan North</option>
            <option value="KR">Khorasan Razavi</option>
            <option value="KS">Khorasan South</option>
            <option value="KH">Khuzestan</option>
            <option value="KB">Kohgiluyeh and Boyer-Ahmad</option>
            <option value="KU">Kurdistan</option>
            <option value="LO">Lorestan</option>
            <option value="MA">Markazi</option>
            <option value="MZ">Mazandaran</option>
            <option value="QA">Qazvin</option>
            <option value="QO">Qom</option>
            <option value="SE">Semnan</option>
            <option value="SB">Sistan and Baluchestan</option>
            <option value="TH" selected="selected">Tehran</option>
            <option value="YZ">Yazd</option>
            <option value="ZN">Zanjan</option>
        </select>'''
        self.assertHTMLEqual(f.render('province', 'TH'), out)

    def test_IRPostalCodeField(self):
        error_format = ['Enter a postal code in the format XXXXXXXXXX - digits only']
        valid = {
            '1496675465': '1496675465',
        }
        invalid = {
            '84545x': error_format,
            '1496575465': error_format,
            '1234': error_format,
            '123 4': error_format,
            '44455522': error_format,
        }
        self.assertFieldOutput(IRPostalCodeField, valid, invalid)

    def test_IRIDNumberField(self):
        error_invalid = ['Enter a valid ID number.']
        valid = {
            '1362136042': '1362136042',
            '0492427259': '0492427259',
            '0920388159': '0920388159',
            '0566360276': '0566360276',
            '0126692548': '0126692548',
        }
        invalid = {
            '123456789': error_invalid,
            '12345678-9': error_invalid,
            '012346578': error_invalid,
            '012346578-': error_invalid,
            '01266925485': error_invalid,
            '0566360272': error_invalid
        }
        self.assertFieldOutput(IRIDNumberField, valid, invalid)
