from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.jp.forms import JPPostalCodeField, JPPrefectureCodeSelect, JPPrefectureSelect


class JPLocalFlavorTests(SimpleTestCase):
    def test_JPPrefectureSelect(self):
        f = JPPrefectureSelect()
        out = '''<select name="prefecture">
<option value="hokkaido">Hokkaido</option>
<option value="aomori">Aomori</option>
<option value="iwate">Iwate</option>
<option value="miyagi">Miyagi</option>
<option value="akita">Akita</option>
<option value="yamagata">Yamagata</option>
<option value="fukushima">Fukushima</option>
<option value="ibaraki">Ibaraki</option>
<option value="tochigi">Tochigi</option>
<option value="gunma">Gunma</option>
<option value="saitama">Saitama</option>
<option value="chiba">Chiba</option>
<option value="tokyo">Tokyo</option>
<option value="kanagawa" selected="selected">Kanagawa</option>
<option value="niigata">Niigata</option>
<option value="toyama">Toyama</option>
<option value="ishikawa">Ishikawa</option>
<option value="fukui">Fukui</option>
<option value="yamanashi">Yamanashi</option>
<option value="nagano">Nagano</option>
<option value="gifu">Gifu</option>
<option value="shizuoka">Shizuoka</option>
<option value="aichi">Aichi</option>
<option value="mie">Mie</option>
<option value="shiga">Shiga</option>
<option value="kyoto">Kyoto</option>
<option value="osaka">Osaka</option>
<option value="hyogo">Hyogo</option>
<option value="nara">Nara</option>
<option value="wakayama">Wakayama</option>
<option value="tottori">Tottori</option>
<option value="shimane">Shimane</option>
<option value="okayama">Okayama</option>
<option value="hiroshima">Hiroshima</option>
<option value="yamaguchi">Yamaguchi</option>
<option value="tokushima">Tokushima</option>
<option value="kagawa">Kagawa</option>
<option value="ehime">Ehime</option>
<option value="kochi">Kochi</option>
<option value="fukuoka">Fukuoka</option>
<option value="saga">Saga</option>
<option value="nagasaki">Nagasaki</option>
<option value="kumamoto">Kumamoto</option>
<option value="oita">Oita</option>
<option value="miyazaki">Miyazaki</option>
<option value="kagoshima">Kagoshima</option>
<option value="okinawa">Okinawa</option>
</select>'''
        self.assertHTMLEqual(f.render('prefecture', 'kanagawa'), out)

    def test_JPPrefectureCodeSelect(self):
        f = JPPrefectureCodeSelect()
        out = '''<select name="prefecture">
<option value="01">Hokkaido</option>
<option value="02">Aomori</option>
<option value="03">Iwate</option>
<option value="04">Miyagi</option>
<option value="05">Akita</option>
<option value="06">Yamagata</option>
<option value="07">Fukushima</option>
<option value="08">Ibaraki</option>
<option value="09">Tochigi</option>
<option value="10">Gunma</option>
<option value="11">Saitama</option>
<option value="12">Chiba</option>
<option value="13">Tokyo</option>
<option value="14" selected="selected">Kanagawa</option>
<option value="15">Niigata</option>
<option value="16">Toyama</option>
<option value="17">Ishikawa</option>
<option value="18">Fukui</option>
<option value="19">Yamanashi</option>
<option value="20">Nagano</option>
<option value="21">Gifu</option>
<option value="22">Shizuoka</option>
<option value="23">Aichi</option>
<option value="24">Mie</option>
<option value="25">Shiga</option>
<option value="26">Kyoto</option>
<option value="27">Osaka</option>
<option value="28">Hyogo</option>
<option value="29">Nara</option>
<option value="30">Wakayama</option>
<option value="31">Tottori</option>
<option value="32">Shimane</option>
<option value="33">Okayama</option>
<option value="34">Hiroshima</option>
<option value="35">Yamaguchi</option>
<option value="36">Tokushima</option>
<option value="37">Kagawa</option>
<option value="38">Ehime</option>
<option value="39">Kochi</option>
<option value="40">Fukuoka</option>
<option value="41">Saga</option>
<option value="42">Nagasaki</option>
<option value="43">Kumamoto</option>
<option value="44">Oita</option>
<option value="45">Miyazaki</option>
<option value="46">Kagoshima</option>
<option value="47">Okinawa</option>
</select>'''
        self.assertHTMLEqual(f.render('prefecture', '14'), out)

    def test_JPPostalCodeField(self):
        error_format = ['Enter a postal code in the format XXXXXXX or XXX-XXXX.']
        valid = {
            '251-0032': '2510032',
            '2510032': '2510032',
        }
        invalid = {
            '2510-032': error_format,
            '251a0032': error_format,
            'a51-0032': error_format,
            '25100321': error_format,
        }
        self.assertFieldOutput(JPPostalCodeField, valid, invalid)
