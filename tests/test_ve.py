from django.test import SimpleTestCase

from localflavor.ve.forms import VERegionSelect, VEStateSelect


class VELocalFlavorTests(SimpleTestCase):

    def test_VERegionSelect(self):
        f = VERegionSelect()

        out = '''<select name="regiones">
<option value="501">Regi\xf3n Capital</option>
<option value="502">Regi\xf3n Central</option>
<option value="503">Regi\xf3n de los Llanos</option>
<option value="504">Regi\xf3n Centro Occidental</option>
<option value="505">Regi\xf3n Zuliana</option>
<option value="506">Regi\xf3n de los Andes</option>
<option value="507">Regi\xf3n Nor-Oriental</option>
<option value="508" selected="selected">Regi\xf3n Insular</option>
<option value="509">Regi\xf3n Guayana</option>
<option value="510">Regi\xf3n Sur Occidental</option>
</select>'''

        self.assertHTMLEqual(f.render('regiones', '508'), out)


    def test_VEStateSelect(self):
        f = VEStateSelect()

        out = '''<select name="estados">
<option value="VE-Z">Amazonas</option>
<option value="VE-B">Anzo\xe1tegui</option>
<option value="VE-C">Apure</option>
<option value="VE-D">Aragua</option>
<option value="VE-E">Barinas</option>
<option value="VE-F">Bolívar</option>
<option value="VE-G">Carabobo</option>
<option value="VE-H" selected="selected">Cojedes</option>
<option value="VE-Y">Delta Amacuro</option>
<option value="VE-W">Dependencias Federales</option>
<option value="VE-A">Distrito Capital</option>
<option value="VE-I">Falc\xf3n</option>
<option value="VE-J">Gu\xe1rico</option>
<option value="VE-K">Lara</option>
<option value="VE-L">M\xe9rida</option>
<option value="VE-M">Miranda</option>
<option value="VE-N">Monagas</option>
<option value="VE-O">Nueva Esparta</option>
<option value="VE-P">Portuguesa</option>
<option value="VE-R">Sucre</option>
<option value="VE-S">T\xe1chira</option>
<option value="VE-T">Trujillo</option>
<option value="VE-X">Vargas</option>
<option value="VE-U">Yaracuy</option>
<option value="VE-V">Zulia</option>
</select>'''

        self.assertHTMLEqual(f.render('estados', 'VE-H'), out)
