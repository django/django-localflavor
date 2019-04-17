"""Contains a set of tests which can be used to validate the current implementation."""
from django.test import SimpleTestCase

from localflavor.pt.forms import PTCitizenCardNumberField, PTRegionSelect, PTSocialSecurityNumberField, PTZipCodeField


class PTLocalFlavorTests(SimpleTestCase):
    def test_PTCitizenCardNumberField(self):
        error_badchecksum = ['The specified value is not a valid Citizen Card number.']
        error_invalid = ['Citizen Card numbers have the format XXXXXXXXXYYX or XXXXXXXX-XYYX '
                         '(where X is a digit and Y is an alphanumeric character).']
        valid = {
            '132011441ZZ8': '13201144-1ZZ8',
            '129463833ZY7': '12946383-3ZY7',
            '129463833ZZ5': '12946383-3ZZ5',
            '13201144-1ZZ8': '13201144-1ZZ8',
            '12946383-3ZY7': '12946383-3ZY7',
            '12946383-3ZZ5': '12946383-3ZZ5',
        }
        invalid = {
            '13201ZZ8': error_invalid,
            '12943ZY7': error_invalid,
            '13201144': error_invalid,
            '12946383': error_invalid,
            '13201144AZZ8': error_invalid,
            '12946383EZY7': error_invalid,
            '13201144-1zz8': error_invalid,
            '12946383-3zy7': error_invalid,
            '12946383-3zz5': error_invalid,
            '13201144(1ZZ8)': error_invalid,
            '12946373(3ZY7)': error_invalid,
            '13201144 (1ZZ8)': error_invalid,
            '12946373 (3ZY7)': error_invalid,
            '13201144-1ZZ7': error_badchecksum,
            '13201144-3ZZ8': error_badchecksum,
            '12946383-3ZY5': error_badchecksum,
            '12946383-3ZZ7': error_badchecksum,
        }
        self.assertFieldOutput(PTCitizenCardNumberField, valid, invalid)

    def test_PTRegionSelect(self):
        field = PTRegionSelect()
        output = '''<select name="regions">
                    <option value="01">Aveiro</option>
                    <option value="02">Beja</option>
                    <option value="03">Braga</option>
                    <option value="04">Bragança</option>
                    <option value="05">Castelo Branco</option>
                    <option value="06" selected="selected">Coimbra</option>
                    <option value="07">Évora</option>
                    <option value="08">Faro</option>
                    <option value="09">Guarda</option>
                    <option value="10">Leiria</option>
                    <option value="11">Lisboa</option>
                    <option value="12">Portalegre</option>
                    <option value="13">Porto</option>
                    <option value="14">Santarém</option>
                    <option value="15">Setúbal</option>
                    <option value="16">Viana do Castelo</option>
                    <option value="17">Vila Real</option>
                    <option value="18">Viseu</option>
                    <option value="20">Região Autónoma da Madeira</option>
                    <option value="30">Região Autónoma dos Açores</option>
                    </select>'''
        self.assertHTMLEqual(field.render('regions', '06'), output)

    def test_PTSocialSecurityNumberField(self):
        error_badchecksum = ['The specified number is not a valid Social Security number.']
        error_invalid = ['Social Security numbers must be in the format XYYYYYYYYYY '
                         '(where X is either 1 or 2 and Y is any other digit).']
        valid = {
            '12347312896': 12347312896,
            '21865241240': 21865241240,
            '17512436983': 17512436983,
            '21467822675': 21467822675,
            '14652348947': 14652348947,
        }
        invalid = {
            '3465 234': error_invalid,
            '1234-3094': error_invalid,
            '0175423542': error_invalid,
            '123A7312894': error_invalid,
            '01467822673': error_invalid,
            '12347312892': error_badchecksum,
            '21865241241': error_badchecksum,
            '17512436987': error_badchecksum,
            '21467822673': error_badchecksum,
            '14652348944': error_badchecksum,
        }
        self.assertFieldOutput(PTSocialSecurityNumberField, valid, invalid)

    def test_PTZipCodeField(self):
        error_invalid = ['Zip codes must be in the format XYYY-YYY '
                         '(where X is a digit between 1 and 9 and Y is any other digit).']
        valid = {
            '3030-034': '3030-034',
            '3800-011': '3800-011',
            '9700-213': '9700-213',
        }
        invalid = {
            '2A200': error_invalid,
            '980001': error_invalid,
            '1003456': error_invalid,
            '0178-281': error_invalid,
        }
        self.assertFieldOutput(PTZipCodeField, valid, invalid)
