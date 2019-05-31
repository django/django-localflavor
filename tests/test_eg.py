from django.test import SimpleTestCase

from localflavor.eg.forms import EGGovernorateSelect, EGNationalIDNumberField


class EGLocalFlavorTests(SimpleTestCase):
    maxDiff = None

    def test_EGNationalIDNumberField(self):
        error_invalid = ['Enter a valid Egyptian National ID number']
        valid = {
            '29406191300551': '29406191300551',
            '29602071300217': '29602071300217',
            '30302071301592': '30302071301592',
        }
        invalid = {
            '29406190500551': error_invalid,
            '29413191300551': error_invalid,
            '30000000000555': error_invalid,
            '30332071301592': error_invalid,
            '49602071300217': error_invalid,
        }
        self.assertFieldOutput(EGNationalIDNumberField, valid, invalid)

    def test_EGGovernorateSelect(self):
        f = EGGovernorateSelect()
        result = '''<select name="governorates">
<option value="DK">Dakahlia</option>
<option value="BA">Red Sea</option>
<option value="BH">Beheira</option>
<option value="FYM" selected="selected">Faiyum</option>
<option value="GH">Gharbia</option>
<option value="ALX">Alexandria</option>
<option value="IS">Ismailia</option>
<option value="GZ">Giza</option>
<option value="MNF">Monufia</option>
<option value="MN">Minya</option>
<option value="C">Cairo</option>
<option value="KB">Qalyubia</option>
<option value="LX">Luxor</option>
<option value="WAD">New Valley</option>
<option value="SUZ">Suez</option>
<option value="SHR">Al Sharqia</option>
<option value="ASN">Aswan</option>
<option value="AST">Asyut</option>
<option value="BNS">Beni Suef</option>
<option value="PTS">Port Said</option>
<option value="DT">Damietta</option>
<option value="JS">South Sinai</option>
<option value="KFS">Kafr el-Sheikh</option>
<option value="MT">Matrouh</option>
<option value="KN">Qena</option>
<option value="SIN">North Sinai</option>
<option value="SHG">Sohag</option>
</select>'''
        self.assertHTMLEqual(f.render('governorates', 'FYM'), result)
