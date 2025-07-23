from django.test import SimpleTestCase

from localflavor.tw.forms import TWAdministrativeDivisionSelect


class TWLocalFlavorTests(SimpleTestCase):
    def test_TWAdministrativeDivisionSelect(self):
        f = TWAdministrativeDivisionSelect()
        correct_output = '''<select name="administrative_divisions">
<option value="changhua_county">Changhua County</option>
<option value="chiayi_city">Chiayi City</option>
<option value="chiayi_county">Chiayi County</option>
<option value="hsinchu_city">Hsinchu City</option>
<option value="hsinchu_county">Hsinchu County</option>
<option value="hualien_county">Hualien County</option>
<option value="kaohsiung_city">Kaohsiung City</option>
<option value="keelung_city">Keelung City</option>
<option value="kinmen_county">Kinmen County</option>
<option value="lienchiang_county">Lienchiang County</option>
<option value="miaoli_county">Miaoli County</option>
<option value="nantou_county">Nantou County</option>
<option value="new_taipei_city">New Taipei City</option>
<option value="penghu_county">Penghu County</option>
<option value="pingtung_county">Pingtung County</option>
<option value="taichung_city">Taichung City</option>
<option value="tainan_city">Tainan City</option>
<option value="taipei_city" selected="selected">Taipei City</option>
<option value="taitung_county">Taitung County</option>
<option value="taoyuan_city">Taoyuan City</option>
<option value="yilan_county">Yilan County</option>
<option value="yunlin_county">Yunlin County</option>
</select>'''
        self.assertHTMLEqual(f.render('administrative_divisions', 'taipei_city'), correct_output)
