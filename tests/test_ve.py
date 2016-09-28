from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.ve.forms import VERegionSelect

class VELocalFlavorTests(SimpleTestCase):

    def test_VERegionSelect(self):
        f = VERegionSelect()

        out = '''<select name="regiones">
<option value=""></option>
<option value="501">Región Capital</option>
<option value="502">Región Central</option>
<option value="503">Región de los Llanos</option>
<option value="504">Región Centro Occidental</option>
<option value="505">Región Zuliana</option>
<option value="506">Región de los Andes</option>
<option value="507">Región Nor-Oriental</option>
<option value="508" selected="selected">Región Insular</option>
<option value="509">Región Guayana</option>
<option value="510">Región Sur Occidental</option>
</select>'''

        self.assertHTMLEqual(f.render('regiones', '508'), out)
