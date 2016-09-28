# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.ve.forms import VERegionSelect

class VELocalFlavorTests(SimpleTestCase):

    def test_VERegionSelect(self):
        f = VERegionSelect()

        out = '''<select name="regiones">
<option value=""></option>
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
