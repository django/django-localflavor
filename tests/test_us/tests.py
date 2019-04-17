from django.test import TestCase

from localflavor.us import forms

from .forms import USPlaceForm


class USLocalFlavorTests(TestCase):

    def setUp(self):
        self.form = USPlaceForm({
            'state': 'GA',
            'state_req': 'NC',
            'postal_code': 'GA',
            'name': 'impossible',
            'zip_code': '12345',
        })

    def test_get_display_methods(self):
        """Test that the get_*_display() methods are added to the model instances."""
        place = self.form.save()
        self.assertEqual(place.get_state_display(), 'Georgia')
        self.assertEqual(place.get_state_req_display(), 'North Carolina')

    def test_required(self):
        """Test that required USStateFields throw appropriate errors."""
        form = USPlaceForm({'state': 'GA', 'name': 'Place in GA'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['state_req'], ['This field is required.'])

    def test_errors(self):
        form = USPlaceForm({
            'state': 'invalid',
            'state_req': 'invalid',
            'postal_code': 'invalid',
            'name': 'name',
            'ssn': 'invalid',
            'zip_code': 'invalid'
        })
        self.assertFalse(form.is_valid())
        choice_messages = ['Select a valid choice. invalid is not one of the available choices.']
        self.assertEqual(form.errors['state'], choice_messages)
        self.assertEqual(form.errors['state_req'], choice_messages)
        self.assertEqual(form.errors['postal_code'], choice_messages)
        self.assertEqual(form.errors['ssn'], ['Enter a valid U.S. Social Security number in XXX-XX-XXXX format.'])
        self.assertEqual(form.errors['zip_code'], ['Enter a zip code in the format XXXXX or XXXXX-XXXX.'])

    def test_field_blank_option(self):
        """Test that the empty option is there."""
        state_select_html = """\
<select name="state" id="id_state">
<option value="">---------</option>
<option value="AL">Alabama</option>
<option value="AK">Alaska</option>
<option value="AS">American Samoa</option>
<option value="AZ">Arizona</option>
<option value="AR">Arkansas</option>
<option value="AA">Armed Forces Americas</option>
<option value="AE">Armed Forces Europe</option>
<option value="AP">Armed Forces Pacific</option>
<option value="CA">California</option>
<option value="CO">Colorado</option>
<option value="CT">Connecticut</option>
<option value="DE">Delaware</option>
<option value="DC">District of Columbia</option>
<option value="FL">Florida</option>
<option value="GA" selected="selected">Georgia</option>
<option value="GU">Guam</option>
<option value="HI">Hawaii</option>
<option value="ID">Idaho</option>
<option value="IL">Illinois</option>
<option value="IN">Indiana</option>
<option value="IA">Iowa</option>
<option value="KS">Kansas</option>
<option value="KY">Kentucky</option>
<option value="LA">Louisiana</option>
<option value="ME">Maine</option>
<option value="MD">Maryland</option>
<option value="MA">Massachusetts</option>
<option value="MI">Michigan</option>
<option value="MN">Minnesota</option>
<option value="MS">Mississippi</option>
<option value="MO">Missouri</option>
<option value="MT">Montana</option>
<option value="NE">Nebraska</option>
<option value="NV">Nevada</option>
<option value="NH">New Hampshire</option>
<option value="NJ">New Jersey</option>
<option value="NM">New Mexico</option>
<option value="NY">New York</option>
<option value="NC">North Carolina</option>
<option value="ND">North Dakota</option>
<option value="MP">Northern Mariana Islands</option>
<option value="OH">Ohio</option>
<option value="OK">Oklahoma</option>
<option value="OR">Oregon</option>
<option value="PA">Pennsylvania</option>
<option value="PR">Puerto Rico</option>
<option value="RI">Rhode Island</option>
<option value="SC">South Carolina</option>
<option value="SD">South Dakota</option>
<option value="TN">Tennessee</option>
<option value="TX">Texas</option>
<option value="UT">Utah</option>
<option value="VT">Vermont</option>
<option value="VI">Virgin Islands</option>
<option value="VA">Virginia</option>
<option value="WA">Washington</option>
<option value="WV">West Virginia</option>
<option value="WI">Wisconsin</option>
<option value="WY">Wyoming</option>
</select>"""
        self.assertHTMLEqual(str(self.form['state']), state_select_html)

    def test_full_postal_code_list(self):
        """Test that the full USPS code field is really the full list."""
        usps_select_html = """\
<select name="postal_code" id="id_postal_code">
<option value="">---------</option>
<option value="AL">Alabama</option>
<option value="AK">Alaska</option>
<option value="AS">American Samoa</option>
<option value="AZ">Arizona</option>
<option value="AR">Arkansas</option>
<option value="AA">Armed Forces Americas</option>
<option value="AE">Armed Forces Europe</option>
<option value="AP">Armed Forces Pacific</option>
<option value="CA">California</option>
<option value="CO">Colorado</option>
<option value="CT">Connecticut</option>
<option value="DE">Delaware</option>
<option value="DC">District of Columbia</option>
<option value="FM">Federated States of Micronesia</option>
<option value="FL">Florida</option>
<option value="GA" selected="selected">Georgia</option>
<option value="GU">Guam</option>
<option value="HI">Hawaii</option>
<option value="ID">Idaho</option>
<option value="IL">Illinois</option>
<option value="IN">Indiana</option>
<option value="IA">Iowa</option>
<option value="KS">Kansas</option>
<option value="KY">Kentucky</option>
<option value="LA">Louisiana</option>
<option value="ME">Maine</option>
<option value="MH">Marshall Islands</option>
<option value="MD">Maryland</option>
<option value="MA">Massachusetts</option>
<option value="MI">Michigan</option>
<option value="MN">Minnesota</option>
<option value="MS">Mississippi</option>
<option value="MO">Missouri</option>
<option value="MT">Montana</option>
<option value="NE">Nebraska</option>
<option value="NV">Nevada</option>
<option value="NH">New Hampshire</option>
<option value="NJ">New Jersey</option>
<option value="NM">New Mexico</option>
<option value="NY">New York</option>
<option value="NC">North Carolina</option>
<option value="ND">North Dakota</option>
<option value="MP">Northern Mariana Islands</option>
<option value="OH">Ohio</option>
<option value="OK">Oklahoma</option>
<option value="OR">Oregon</option>
<option value="PW">Palau</option>
<option value="PA">Pennsylvania</option>
<option value="PR">Puerto Rico</option>
<option value="RI">Rhode Island</option>
<option value="SC">South Carolina</option>
<option value="SD">South Dakota</option>
<option value="TN">Tennessee</option>
<option value="TX">Texas</option>
<option value="UT">Utah</option>
<option value="VT">Vermont</option>
<option value="VI">Virgin Islands</option>
<option value="VA">Virginia</option>
<option value="WA">Washington</option>
<option value="WV">West Virginia</option>
<option value="WI">Wisconsin</option>
<option value="WY">Wyoming</option>
</select>"""
        self.assertHTMLEqual(str(self.form['postal_code']), usps_select_html)

    def test_USStateSelect(self):
        f = forms.USStateSelect()
        out = '''<select name="state">
<option value="AL">Alabama</option>
<option value="AK">Alaska</option>
<option value="AS">American Samoa</option>
<option value="AZ">Arizona</option>
<option value="AR">Arkansas</option>
<option value="AA">Armed Forces Americas</option>
<option value="AE">Armed Forces Europe</option>
<option value="AP">Armed Forces Pacific</option>
<option value="CA">California</option>
<option value="CO">Colorado</option>
<option value="CT">Connecticut</option>
<option value="DE">Delaware</option>
<option value="DC">District of Columbia</option>
<option value="FL">Florida</option>
<option value="GA">Georgia</option>
<option value="GU">Guam</option>
<option value="HI">Hawaii</option>
<option value="ID">Idaho</option>
<option value="IL" selected="selected">Illinois</option>
<option value="IN">Indiana</option>
<option value="IA">Iowa</option>
<option value="KS">Kansas</option>
<option value="KY">Kentucky</option>
<option value="LA">Louisiana</option>
<option value="ME">Maine</option>
<option value="MD">Maryland</option>
<option value="MA">Massachusetts</option>
<option value="MI">Michigan</option>
<option value="MN">Minnesota</option>
<option value="MS">Mississippi</option>
<option value="MO">Missouri</option>
<option value="MT">Montana</option>
<option value="NE">Nebraska</option>
<option value="NV">Nevada</option>
<option value="NH">New Hampshire</option>
<option value="NJ">New Jersey</option>
<option value="NM">New Mexico</option>
<option value="NY">New York</option>
<option value="NC">North Carolina</option>
<option value="ND">North Dakota</option>
<option value="MP">Northern Mariana Islands</option>
<option value="OH">Ohio</option>
<option value="OK">Oklahoma</option>
<option value="OR">Oregon</option>
<option value="PA">Pennsylvania</option>
<option value="PR">Puerto Rico</option>
<option value="RI">Rhode Island</option>
<option value="SC">South Carolina</option>
<option value="SD">South Dakota</option>
<option value="TN">Tennessee</option>
<option value="TX">Texas</option>
<option value="UT">Utah</option>
<option value="VT">Vermont</option>
<option value="VI">Virgin Islands</option>
<option value="VA">Virginia</option>
<option value="WA">Washington</option>
<option value="WV">West Virginia</option>
<option value="WI">Wisconsin</option>
<option value="WY">Wyoming</option>
</select>'''
        self.assertHTMLEqual(f.render('state', 'IL'), out)

    def test_USZipCodeField(self):
        error_format = ['Enter a zip code in the format XXXXX or XXXXX-XXXX.']
        valid = {
            '60606': '60606',
            60606: '60606',
            '04000': '04000',
            ' 04000 ': '04000',
            '60606-1234': '60606-1234',
        }
        invalid = {
            '4000': error_format,
            '6060-1234': error_format,
            '60606-': error_format,
        }
        self.assertFieldOutput(forms.USZipCodeField, valid, invalid)

    def test_USZipCodeField_formfield(self):
        """Test that the full US ZIP code field is really the full list."""
        self.assertHTMLEqual(str(self.form['zip_code']),
                             '<input id="id_zip_code" maxlength="10" name="zip_code" type="text" value="12345" />')

    def test_USStateField(self):
        error_invalid = ['Enter a U.S. state or territory.']
        valid = {
            'il': 'IL',
            'IL': 'IL',
            'illinois': 'IL',
            '  illinois ': 'IL',
        }
        invalid = {
            60606: error_invalid,
        }
        self.assertFieldOutput(forms.USStateField, valid, invalid)

    def test_USSocialSecurityNumberField(self):
        error_invalid = ['Enter a valid U.S. Social Security number in XXX-XX-XXXX format.']

        valid = {
            '123-45-6789': '123-45-6789',
            '123456789': '123-45-6789',
        }
        invalid = {
            '078-05-1120': error_invalid,
            '078051120': error_invalid,
            '900-12-3456': error_invalid,
            '900123456': error_invalid,
            '999-98-7652': error_invalid,
            '999987652': error_invalid,
        }
        self.assertFieldOutput(forms.USSocialSecurityNumberField, valid, invalid)
