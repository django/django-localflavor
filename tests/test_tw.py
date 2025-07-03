from django.test import SimpleTestCase

from localflavor.tw.forms import TWAdministrativeDivisionSelect


class TWLocalFlavorTests(SimpleTestCase):
    def test_TWAdministrativeDivisionSelect(self):
        f = TWAdministrativeDivisionSelect()
        correct_output = '''<select name="administrative_divisions">
<option value="changhua_county">\u5f70\u5316\u7e23</option>
<option value="chiayi_city">\u5609\u7fa9\u5e02</option>
<option value="chiayi_county">\u5609\u7fa9\u7e23</option>
<option value="hsinchu_city">\u65b0\u7af9\u5e02</option>
<option value="hsinchu_county">\u65b0\u7af9\u7e23</option>
<option value="hualien_county">\u82b1\u84ee\u7e23</option>
<option value="kaohsiung_city">\u9ad8\u96c4\u5e02</option>
<option value="keelung_city">\u57fa\u9686\u5e02</option>
<option value="kinmen_county">\u91d1\u9580\u7e23</option>
<option value="lienchiang_county">\u9023\u6c5f\u7e23</option>
<option value="miaoli_county">\u82d7\u6817\u7e23</option>
<option value="nantou_county">\u5357\u6295\u7e23</option>
<option value="new_taipei_city">\u65b0\u5317\u5e02</option>
<option value="penghu_county">\u6f8e\u6e56\u7e23</option>
<option value="pingtung_county">\u5c4f\u6771\u7e23</option>
<option value="taichung_city">\u53f0\u4e2d\u5e02</option>
<option value="tainan_city">\u53f0\u5357\u5e02</option>
<option value="taipei_city" selected="selected">\u53f0\u5317\u5e02</option>
<option value="taitung_county">\u53f0\u6771\u7e23</option>
<option value="taoyuan_city">\u6843\u5712\u5e02</option>
<option value="yilan_county">\u5b9c\u862d\u7e23</option>
<option value="yunlin_county">\u96f2\u6797\u7e23</option>
</select>'''
        self.assertHTMLEqual(f.render('administrative_divisions', 'taipei_city'), correct_output)
