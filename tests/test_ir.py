from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.ir.forms import IRPostlCodeField,IRProvinceSelect

class IRLocalFlavourTests(SimpleTestCase):
    def test_IRProvinceSelect(self):
        f = IRProvinceSelect()
        out ='''<select name="provinces">
<option value="ALB">Alborz</option>
<option value="ARD">Ardabil</option>
<option value="AZE">Azerbaijan, East</option>
<option value="AZW">Azerbaijan, West</option>
<option value="BSH">Bushehr</option>
<option value="CMB">Chahar Mahaal and Bakhtiari</option>
<option value="FAR">Fars</option>
<option value="GIL">Gilan</option>
<option value="GOL">Golestan</option>
<option value="HAM">Hamadan</option>
<option value="HOR">Hormozgān</option>
<option value="ILA">Iliam</option>
<option value="ISF">Isfahan</option>
<option value="KES">Kerman</option>
<option value="KHN">Khorasan, North</option>
<option value="KHR">Khorasan, Razavi</option>
<option value="KHS">Khorasan, South</option>
<option value="KHU">Khuzestan</option>
<option value="KBA">Kohgiluyeh and Boyer-Ahmad</option>
<option value="KUR">Kurdistan</option>
<option value="LOR">Lorestan</option>
<option value="MAR">Markazi</option>
<option value="MAZ">Mazandaran</option>
<option value="QAZ">Qazvin</option>
<option value="QOM">Qom</option>
<option value="SEM">Semnan</option>
<option value="SBA">Sistan and Baluchestan</option>
<option value="TEH">Tehran</option>
<option value="YZD">Yazd</option>
<option value="ZNJ">Zanjan</option>
</select>'''
        self.assertHTMLEqual(f.render('provinces'),'ALB', out)
    def test_IRPostalCodeField(self):
        error_format = ['Enter a postal code in the format xxxxxxxxxx .']
        error_atmost = ['Ensure this value has at most 10 characters (it has 11).']
        error_atleast = ['Ensure this value has at least 10 characters (it has 9).']

        valid = {
            '5987456987' : '9874698741',
            '5987456321' : '4895785787',
            'c464646464' : '4848748487',
        }

        invalid = {
            '4545' : error_atmost+error_format,
            '464676467676' : error_atleast+error_format,
        }
        self.assertFieldOutput(IRPostlCodeField, valid, invalid)
