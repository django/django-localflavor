+from __future__ import unicode_literals
 +
 +from django.test import SimpleTestCase
 +
 +from localflavor.ir.forms import IRPostlCodeField,IRProvinceSelect
 +
 +class IRLocalFlavourTests(SimpleTestCase):
 +    def test_IRProvinceSelect(self):
 +        f = IRProvinceSelect()
 +        out ='''<select name="provinces">
 +<option value="Alborz">Alborz</option>
 +<option value="Ardabil">Ardabil</option>
 +<option value="Azerbaijan, East">Azerbaijan, East</option>
 +<option value="Azerbaijan, West">Azerbaijan, West</option>
 +<option value="Bushehr">Bushehr</option>
 +<option value="Chahar Mahaal and Bakhtiari">Chahar Mahaal and Bakhtiari</option>
 +<option value="Fars">Fars</option>
 +<option value="Gilan">Gilan</option>
 +<option value="Golestan">Golestan</option>
 +<option value="Hamadan">Hamadan</option>
 +<option value="Hormozgān">Hormozgān</option>
 +<option value="Iliam">Iliam</option>
 +<option value="Isfahan">Isfahan</option>
 +<option value="Kerman">Kerman</option>
 +<option value="Khorasan, North">Khorasan, North</option>
 +<option value="Khorasan, Razavi">Khorasan, Razavi</option>
 +<option value="Khorasan, South">Khorasan, South</option>
 +<option value="Khuzestan">Khuzestan</option>
 +<option value="Kohgiluyeh and Boyer-Ahmad">Kohgiluyeh and Boyer-Ahmad</option>
 +<option value="Kurdistan">Kurdistan</option>
 +<option value="Lorestan">Lorestan</option>
 +<option value="Markazi">Markazi</option>
 +<option value="Mazandaran">Mazandaran</option>
 +<option value="Qazvin">Qazvin</option>
 +<option value="Qom">Qom</option>
 +<option value="Semnan">Semnan</option>
 +<option value="Sistan and Baluchestan">Sistan and Baluchestan</option>
 +<option value="Tehran">Tehran</option>
 +<option value="Yazd">Yazd</option>
 +<option value="Zanjan">Zanjan</option>
 +</select>'''
 +        self.assertHTMLEqual(f.render('provinces'),'Alborz', out)
 +    def test_IRPostalCodeField(self):
 +        error_format = ['Enter a postal code in the format xxxxxxxxxx .']
 +        error_atmost = ['Ensure this value has at most 10 characters (it has 11).']
 +        error_atleast = ['Ensure this value has at least 10 characters (it has 9).']
 +
 +        valid = {
 +            '5987456987' : '9874698741',
 +            '5987456321' : '4895785787',
 +            'c464646464' : '4848748487',
 +        }
 +
 +        invalid = {
 +            '4545' : error_atmost+error_format,
 +            '464676467676' : error_atleast+error_format,
 +        }
 +        self.assertFieldOutput(IRPostlCodeField, valid, invalid)
