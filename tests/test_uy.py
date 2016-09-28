from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.uy.forms import UYCIField, UYDepartmentSelect
from localflavor.uy.util import get_validation_digit


class UYLocalFlavorTests(SimpleTestCase):
    def test_UYDepartmentSelect(self):
        f = UYDepartmentSelect()
        out = '''<select name="departamentos">
<option value="G">Artigas</option>
<option value="A">Canelones</option>
<option value="E">Cerro Largo</option>
<option value="L">Colonia</option>
<option value="Q">Durazno</option>
<option value="N">Flores</option>
<option value="O">Florida</option>
<option value="P">Lavalleja</option>
<option value="B">Maldonado</option>
<option value="S" selected="selected">Montevideo</option>
<option value="I">Paysand\xfa</option>
<option value="J">R\xedo Negro</option>
<option value="F">Rivera</option>
<option value="C">Rocha</option>
<option value="H">Salto</option>
<option value="M">San Jos\xe9</option>
<option value="K">Soriano</option>
<option value="R">Tacuaremb\xf3</option>
<option value="D">Treinta y Tres</option>
</select>'''
        self.assertHTMLEqual(f.render('departamentos', 'S'), out)

    def test_UYCIField(self):
        valid = {
            '4098053': '4098053',
            '409805-3': '409805-3',
            '409.805-3': '409.805-3',
            '10054112': '10054112',
            '1005411-2': '1005411-2',
            '1.005.411-2': '1.005.411-2',
        }
        invalid = {
            'foo': ['Enter a valid CI number in X.XXX.XXX-X,XXXXXXX-X or XXXXXXXX format.'],
            '409805-2': ['Enter a valid CI number.'],
            '1.005.411-5': ['Enter a valid CI number.'],
        }
        self.assertFieldOutput(UYCIField, valid, invalid)
        self.assertEqual(get_validation_digit(409805), 3)
        self.assertEqual(get_validation_digit(1005411), 2)
