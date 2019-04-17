from django.test import SimpleTestCase

from localflavor.co.forms import CODepartmentSelect, CONITField


class COLocalFlavorTests(SimpleTestCase):
    def test_CODepartmentSelect(self):
        d = CODepartmentSelect()
        out = """<select name="department">
<option value="AMA">Amazonas</option>
<option value="ANT">Antioquia</option>
<option value="ARA">Arauca</option>
<option value="ATL">Atl\xe1ntico</option>
<option value="DC">Bogot\xe1</option>
<option value="BOL">Bol\xedvar</option>
<option value="BOY">Boyac\xe1</option>
<option value="CAL">Caldas</option>
<option value="CAQ">Caquet\xe1</option>
<option value="CAS">Casanare</option>
<option value="CAU">Cauca</option>
<option value="CES">Cesar</option>
<option value="CHO">Choc\xf3</option>
<option value="COR" selected="selected">C\xf3rdoba</option>
<option value="CUN">Cundinamarca</option>
<option value="GUA">Guain\xeda</option>
<option value="GUV">Guaviare</option>
<option value="HUI">Huila</option>
<option value="LAG">La Guajira</option>
<option value="MAG">Magdalena</option>
<option value="MET">Meta</option>
<option value="NAR">Nari\xf1o</option>
<option value="NSA">Norte de Santander</option>
<option value="PUT">Putumayo</option>
<option value="QUI">Quind\xedo</option>
<option value="RIS">Risaralda</option>
<option value="SAP">San Andr\xe9s and Providencia</option>
<option value="SAN">Santander</option>
<option value="SUC">Sucre</option>
<option value="TOL">Tolima</option>
<option value="VAC">Valle del Cauca</option>
<option value="VAU">Vaup\xe9s</option>
<option value="VID">Vichada</option>
</select>"""
        self.assertHTMLEqual(d.render('department', 'COR'), out)

    def test_CONITField(self):
        error_format = ['Enter a valid NIT in XXXXXXXXXXX-Y or XXXXXXXXXXXY format.']
        error_invalid = ['Invalid NIT.']
        valid = {
            '37547837-0': '37547837-0',
            '900227140-3': '900227140-3',
            '79626331-8': '79626331-8',
            '375478370': '37547837-0',
            '796273731': '79627373-1',
            '9002271403': '900227140-3',
        }
        invalid = {
            '2-375478370-9': error_format,
            '20-10123456-': error_format,
            '3-375478370': error_format,
            '375478370-': error_format,
            '37547837-5': error_invalid,
            '37547837-2': error_invalid,
            '9002271401': error_invalid,
        }
        self.assertFieldOutput(CONITField, valid, invalid)
