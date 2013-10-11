from __future__ import unicode_literals
from django.test import SimpleTestCase
from localflavor.ua.forms import (UARegionSelect, UAPostalCodeField,
                                  INVALID_POSTAL_CODE)


class UALocalFlavorTests(SimpleTestCase):

    def test_UARegionSelect(self):
        f = UARegionSelect()
        out = '''<select name="region">
<option value="01">Autonomous Republic of Crimea</option>
<option value="02">Cherkasy Oblast</option>
<option value="03">Chernihiv Oblast</option>
<option value="04">Chernivtsi Oblast</option>
<option value="05">Dnipropetrovsk Oblast</option>
<option value="06">Donetsk Oblast</option>
<option value="07">Ivano-Frankivsk Oblast</option>
<option value="08">Kharkiv Oblast</option>
<option value="09">Kherson Oblast</option>
<option value="10">Khmelnytskyi Oblast</option>
<option value="11">Kiev Oblast</option>
<option value="12">Kirovohrad Oblast</option>
<option value="13">Luhansk Oblast</option>
<option value="14">Lviv Oblast</option>
<option value="15">Mykolaiv Oblast</option>
<option value="16">Odessa Oblast</option>
<option value="17">Poltava Oblast</option>
<option value="18">Rivne Oblast</option>
<option value="19">Sumy Oblast</option>
<option value="20">Ternopil Oblast</option>
<option value="21">Vinnytsia Oblast</option>
<option value="22">Volyn Oblast</option>
<option value="23">Zakarpattia Oblast</option>
<option value="23">Zaporizhia Oblast</option>
<option value="24">Zhytomyr Oblast</option>
<option value="25">Kyiv City</option>
<option value="26">Sevastopol City</option>
</select>'''
        self.assertHTMLEqual(f.render('region', None), out)

    def test_UAPostalCodeField(self):
        error = [INVALID_POSTAL_CODE]
        valid = {
            '41019': '41019',
            '03190': '03190',
            '33000': '33000',
        }
        invalid = {
            'bad': error,
            '123 34': error,
            '1234': error,
            '123456': error,
            '1234567': error,
            '00123': error,
        }
        self.assertFieldOutput(UAPostalCodeField, valid, invalid)
