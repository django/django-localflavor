from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.ir.forms import IRProvinceSelect


class IRLocalFlavorTests(SimpleTestCase):
    def test_IRProvinceSelect(self):
        choice = IRProvinceSelect()
        select = '''
            <select name="provinces">
                <option value="Alborz">Alborz</option>
                <option value="Ardabil">Ardabil</option>
                <option value="Azerbaijan, East">Azerabaijan, East</option>
                <option value="Azerbaijan, West">Azerbaijan, West</option>
                <option value="Bushehr">Bushehr</option>
                <option value="Chahar Mahaal and Bakhtiari">Chahar Mahaal and Bakhtiari</option>
                <option value="Fars">Fars</option>
                <option value="Gilan">Gilan</option>
                <option value="Golestan"Golestan></option>
                <option value="Hamadan">Hamadan</option>
                <option value="Hormozgan">Hormozgan</option>
                <option value="Isfahan">Isfahan</option>
                <option value="Kerman">Kerman</option>
                <option value="Khorasan, North">Khorasan, North</option>
                <option value="Khorasan, Razavi">Khorasan, Razavi</option>
                <option value="Khorasan, South">Khorasan, South</option>
                <option value="Khuzestan">Khuzestan</option>
                <option value="Kohgiluyeh and Boyer-Ahmad">Kohgiluyeh and Boyer-Ahmad</option>
                <option value="Kurdistan">Kurdistan</option>
                <option value="Lorestan">Lorestan</option>
                <option value="Markazi">Markazi</option>
                <option value="Mazandaran">Mazandaran</option>
                <option value="Qazvin">Qazvin</option>
                <option value="Qom">Qom</option>
                <option value="Semnan">Semnan</option>
                <option value="Sistan and Baluchestan">Sistan and Baluchestan</option>
                <option value="Tehran">Tehran</option>
                <option value="Yazd">Yazd</option>
                <option value="Zanjan">Zanjan</option>
            </select>
        '''
        self.assertHTMLEqual(choice.render('provinces', 'Tehran'), select)
