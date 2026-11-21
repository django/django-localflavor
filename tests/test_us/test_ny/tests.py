from __future__ import unicode_literals
from django.test import SimpleTestCase
from localflavor.us.ny.forms import NYSCountySelect

class US_NYSLocalFlavorTests(SimpleTestCase):
    def test_NYSCountySelect(self):
        f = NYSCountySelect()
        out = '''<select name="counties">
    <option value="001">Albany</option>
    <option value="003">Allegany</option>
    <option value="005">Bronx</option>
    <option value="007">Broome</option>
    <option value="009">Cattaraugus</option>
    <option value="011">Cayuga</option>
    <option value="013">Chautauqua</option>
    <option value="015">Chemung</option>
    <option value="017">Chenango</option>
    <option value="019">Clinton</option>
    <option value="021">Columbia</option>
    <option value="023">Cortland</option>
    <option value="025">Delaware</option>
    <option value="027">Dutchess</option>
    <option value="029">Erie</option>
    <option value="031">Essex</option>
    <option value="033">Franklin</option>
    <option value="035">Fulton</option>
    <option value="037">Genesee</option>
    <option value="039">Greene</option>
    <option value="041">Hamilton</option>
    <option value="043">Herkimer</option>
    <option value="045">Jefferson</option>
    <option value="047">Kings</option>
    <option value="049">Lewis</option>
    <option value="051">Livingston</option>
    <option value="053">Madison</option>
    <option value="055">Monroe</option>
    <option value="057">Montgomery</option>
    <option value="059">Nassau</option>
    <option value="061" selected="selected">New York</option>
    <option value="063">Niagara</option>
    <option value="065">Oneida</option>
    <option value="067">Onondaga</option>
    <option value="069">Ontario</option>
    <option value="071">Orange</option>
    <option value="073">Orleans</option>
    <option value="075">Oswego</option>
    <option value="077">Otsego</option>
    <option value="079">Putnam</option>
    <option value="081">Queens</option>
    <option value="083">Rensselaer</option>
    <option value="085">Richmond</option>
    <option value="087">Rockland</option>
    <option value="091">Saratoga</option>
    <option value="093">Schenectady</option>
    <option value="095">Schoharie</option>
    <option value="097">Schuyler</option>
    <option value="099">Seneca</option>
    <option value="089">St. Lawrence</option>
    <option value="101">Steuben</option>
    <option value="103">Suffolk</option>
    <option value="105">Sullivan</option>
    <option value="107">Tioga</option>
    <option value="109">Tompkins</option>
    <option value="111">Ulster</option>
    <option value="113">Warren</option>
    <option value="115">Washington</option>
    <option value="117">Wayne</option>
    <option value="119">Westchester</option>
    <option value="121">Wyoming</option>
    <option value="123">Yates</option>
    </select>'''
        self.assertHTMLEqual(f.render('counties', '061'), out)
