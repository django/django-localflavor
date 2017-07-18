from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.ie.forms import IECountySelect


class IELocalFlavorTests(SimpleTestCase):

    def test_IECountySelect(self):
        f = IECountySelect()
        out = '''<select name="counties">
<option value="carlow">Carlow</option>
<option value="cavan">Cavan</option>
<option value="clare">Clare</option>
<option value="cork">Cork</option>
<option value="donegal">Donegal</option>
<option value="dublin" selected="selected">Dublin</option>
<option value="galway">Galway</option>
<option value="kerry">Kerry</option>
<option value="kildare">Kildare</option>
<option value="kilkenny">Kilkenny</option>
<option value="laois">Laois</option>
<option value="leitrim">Leitrim</option>
<option value="limerick">Limerick</option>
<option value="longford">Longford</option>
<option value="louth">Louth</option>
<option value="mayo">Mayo</option>
<option value="meath">Meath</option>
<option value="monaghan">Monaghan</option>
<option value="offaly">Offaly</option>
<option value="roscommon">Roscommon</option>
<option value="sligo">Sligo</option>
<option value="tipperary">Tipperary</option>
<option value="waterford">Waterford</option>
<option value="westmeath">Westmeath</option>
<option value="wexford">Wexford</option>
<option value="wicklow">Wicklow</option>
</select>'''
        self.assertHTMLEqual(f.render('counties', 'dublin'), out)
