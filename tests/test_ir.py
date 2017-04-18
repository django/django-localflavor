rom __future__ import absolute_import, unicode_literals

from django.test import SimpleTestCase

from localflavor.ar.forms import IRProvinceSelect

class IRLocalFlavorTests(SimpleTestCase):
    def test_IRProvinceSelect(self):
        f=IRProvinceSelect()
        out = '''<select name="provinces">
<option name="Alborz">Alborz</option>
<option name="Ardabil">Ardabil</option>
<option name="Azerbaijan, East">Azerbaijan, East</option>
<option name="Azerbaijan, West">Azerbaijan, West</option>
<option name="Bushehr">Bushehr</option>
<option name="Chahar Mahaal and Bakhtiari">Chahar Mahaal and Bakhtiari</option>
<option name="Fars">Fars</option>
<option name="Gilan">Gilan</option>
<option name="Golestan">Golestan</option>
<option name="Hamedan">Hamedan</option>
<option name="Hormozgan">Hormozgan</option>
<option name="Ilam">Ilam</option>
<option name="Isfahan">Isfahan</option>
<option name="Kerman">Kerman</option>
<option name="Kermanshah">Kermanshah</option>
<option name="Khorasan, North">Khorasan, North</option>
<option name="Khorasan, Razavi">Khorasan, Razavi</option>
<option name="Khorasan, South">Khorasan, South</option>
<option name="Khuzestan">Khuzestan</option>
<option name="Kohgiluyeh and Boyer-Ahmad">Kohgiluyeh and Boyer-Ahmad</option>
<option name="Kurdistan">Kurdistan</option>
<option name="Lorestan">Lorestan</option>
<option name="Qazvin">Qazvin</option>
<option name="Qom">Qom</option>
<option name="Semnan">Semnan</option>
<option name="Sistan and Baluchestan">Sistan and Baluchestan</option>
<option name="Tehran">Tehran</option>
<option name="Yazd">Yazd</option>
<option name="Zanjan">Zanjan</option>
<select>'''
    self.assertHTMLEqual(f.render('provinces'.'Tehran'), out)
