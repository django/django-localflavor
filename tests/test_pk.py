from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.pk.forms import PKPostCodeField, PKPhoneNumberField, PKStateSelect


class PKLocalFlavorTests(SimpleTestCase):
    def test_PKStateSelect(self):
        f = PKStateSelect()
        out = '''<select name="state">
<option value="PK-JK">Azad Jammu &amp; Kashmir</option>
<option value="PK-BA" selected="selected">Balochistan</option>
<option value="PK-TA">Federally Administered Tribal Areas</option>
<option value="PK-GB">Gilgit-Baltistan</option>
<option value="PK-IS">Islamabad</option>
<option value="PK-KP">Khyber Pakhtunkhwa</option>
<option value="PK-PB">Punjab</option>
<option value="PK-SD">Sindh</option>
</select>'''
        self.assertHTMLEqual(f.render('state', 'PK-BA'), out)

    def test_PKPostcodeField(self):
        error_format = ['Enter a 5 digit postcode.']
        valid = {
            '12345': '12345',
            '20000': '20000',
        }
        invalid = {
            '1234': error_format,
            '123456': error_format,
        }
        self.assertFieldOutput(PKPostCodeField, valid, invalid)

    def test_PKPhoneNumberField(self):
        error_format = ['Phone numbers must contain 9, 10 or 11 digits.']
        valid = {
            '123456789': '123456789',
            '1234567890': '1234567890',
            '12345678901': '12345678901',
            '0513456789': '0513456789',
            '051 3456789': '0513456789',
            '051 3456 789': '0513456789',
            '(051) 3456 789': '0513456789',
            '(051) 3456-789': '0513456789',
            '(051)3456-789': '0513456789',
            '0300 1234567': '03001234567',
            '0300 1234 567': '03001234567',
        }
        invalid = {
            '123': error_format,
            '1800DJANGO': error_format,
        }
        self.assertFieldOutput(PKPhoneNumberField, valid, invalid)
