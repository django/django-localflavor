from django.test import SimpleTestCase

from localflavor.tn.forms import TNGovernorateSelect


class TNLocalFlavorTests(SimpleTestCase):
    """Tunisia Local Flavor Tests class."""

    def test_tn_governorate_select(self):
        """Tests Select Governorate."""
        form = TNGovernorateSelect()

        select_governorate_html = '''<select name="governorate">
<option value="ariana">Ariana</option>
<option value="beja">Beja</option>
<option value="ben arous">Ben Arous</option>
<option value="bizert">Bizert</option>
<option value="gabes" selected="selected">Gabes</option>
<option value="gafsa">Gafsa</option>
<option value="jendouba">Jendouba</option>
<option value="kairouan">Kairouan</option>
<option value="kasserine">Kasserine</option>
<option value="kebili">Kebili</option>
<option value="kef">Kef</option>
<option value="mahdia">Mahdia</option>
<option value="manouba">Manouba</option>
<option value="medenine">Medenine</option>
<option value="monastir">Monastir</option>
<option value="nabeul">Nabeul</option>
<option value="sfax">Sfax</option>
<option value="sidi bouzid">Sidi Bouzid</option>
<option value="siliana">Siliana</option>
<option value="sousse">Sousse</option>
<option value="tataouine">Tataouine</option>
<option value="tozeur">Tozeur</option>
<option value="tunis">Tunis</option>
<option value="zaghouan">Zaghouan</option>
</select>'''

        self.assertHTMLEqual(
            form.render('governorate', 'gabes'),
            select_governorate_html
        )
