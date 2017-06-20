from __future__ import unicode_literals

import re

from django.test import TestCase

from localflavor.pk.forms import PKPhoneNumberField, PKPostCodeField, PKStateSelect

from .forms import PakistaniPlaceForm

# From Django 1.11, HTML5 syntax is used (selected)
SELECTED_OPTION_PATTERN = r'<option value="%s" selected(="selected")?>'
BLANK_OPTION_PATTERN = r'<option value="">'
INPUT_VALUE_PATTERN = r'<input[^>]*value="%s"[^>]*>'


class PKLocalflavorTests(TestCase):

    def setUp(self):
        self.form = PakistaniPlaceForm(
            {'state': 'PK-IS',
             'state_required': 'PK-PB',
             'name': 'dummy',
             'postcode': '44000',
             'postcode_required': '46000',
             })

    def test_get_display_methods(self):
        """Ensure get_*_display() methods are added to model instances."""
        place = self.form.save()
        self.assertEqual(place.get_state_display(), 'Islamabad')
        self.assertEqual(place.get_state_required_display(), 'Punjab')

    def test_default_values(self):
        """Ensure that default values are selected in forms."""
        form = PakistaniPlaceForm()
        self.assertTrue(re.search(SELECTED_OPTION_PATTERN % 'PK-IS',
                                  str(form['state_default'])))
        self.assertTrue(re.search(INPUT_VALUE_PATTERN % '44000',
                                  str(form['postcode_default'])))

    def test_required(self):
        """Test that required PKStateFields throw appropriate errors."""
        form = PakistaniPlaceForm({'state': 'PK-PB', 'name': 'Lahore'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['state_required'], ['This field is required.'])
        self.assertEqual(
            form.errors['postcode_required'], ['This field is required.'])

    def test_field_blank_option(self):
        """Test that the empty option is there."""
        self.assertTrue(re.search(BLANK_OPTION_PATTERN,
                                  str(self.form['state'])))

    def test_selected_values(self):
        """Ensure selected states match the initial values provided."""
        self.assertTrue(re.search(SELECTED_OPTION_PATTERN % 'PK-IS',
                                  str(self.form['state'])))
        self.assertTrue(re.search(SELECTED_OPTION_PATTERN % 'PK-PB',
                                  str(self.form['state_required'])))
        self.assertTrue(re.search(INPUT_VALUE_PATTERN % '44000',
                                  str(self.form['postcode'])))
        self.assertTrue(re.search(INPUT_VALUE_PATTERN % '46000',
                                  str(self.form['postcode_required'])))

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

    def test_PKPostCodeField(self):
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
