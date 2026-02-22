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

    def test_USIndividualTaxpayerIdentificationNumberField(self):
        error_invalid = ['Enter a valid U.S. Individual Taxpayer Identification Number in XXX-XX-XXXX format.']
        valid = {
            '900-70-5678': '900-70-5678',   # group 70 (lower bound of 70–88 range)
            '900-88-1234': '900-88-1234',   # group 88 (upper bound of 70–88 range)
            '912701234': '912-70-1234',      # no separators
            '950-90-9999': '950-90-9999',   # group 90 (lower bound of 90–92 range)
            '950-92-9999': '950-92-9999',   # group 92 (upper bound of 90–92 range)
            '950-94-9999': '950-94-9999',   # group 94 (lower bound of 94–99 range)
            '950-99-1234': '950-99-1234',   # group 99 (upper bound of 94–99 range)
        }
        invalid = {
            '123-70-1234': error_invalid,   # area doesn't start with 9
            '900-00-1234': error_invalid,   # group 00
            '900-70-0000': error_invalid,   # serial 0000
            '900-50-1234': error_invalid,   # group 50 (not an ITIN range)
            '900-69-1234': error_invalid,   # group 69 (below 70–88 range)
            '900-89-1234': error_invalid,   # group 89 (gap between 70–88 and 90–92)
            '900-93-1234': error_invalid,   # group 93 (ATIN, not ITIN)
        }
        self.assertFieldOutput(forms.USIndividualTaxpayerIdentificationNumberField, valid, invalid)

    def test_USAdoptionTaxpayerIdentificationNumberField(self):
        error_invalid = ['Enter a valid U.S. Adoption Taxpayer Identification Number in XXX-XX-XXXX format.']
        valid = {
            '900-93-1234': '900-93-1234',   # group 93 (only valid ATIN group)
            '912-93-5678': '912-93-5678',   # group 93, different area
            '999931234': '999-93-1234',     # no separators
        }
        invalid = {
            '123-93-1234': error_invalid,   # area doesn't start with 9
            '900-93-0000': error_invalid,   # serial 0000
            '900-70-1234': error_invalid,   # group 70 (ITIN range, not ATIN)
            '900-92-5678': error_invalid,   # group 92 (ITIN range, not ATIN)
            '900-30-1234': error_invalid,   # group 30 (neither ITIN nor ATIN)
            '900-94-5678': error_invalid,   # group 94 (ITIN range, not ATIN)
        }
        self.assertFieldOutput(forms.USAdoptionTaxpayerIdentificationNumberField, valid, invalid)

    def test_USTaxpayerIdentificationNumberField(self):
        error_invalid = ['Enter a valid U.S. taxpayer identification number in XXX-XX-XXXX format.']
        valid = {
            '123-45-6789': '123-45-6789',   # valid SSN
            '900-70-5678': '900-70-5678',   # valid ITIN
            '900-93-1234': '900-93-1234',   # valid ATIN
        }
        invalid = {
            '000-45-6789': error_invalid,   # area all zeros
            '666-45-6789': error_invalid,   # area 666 (invalid SSN block)
            '078-05-1120': error_invalid,   # blocked SSN
            '900-89-1234': error_invalid,   # 9xx with invalid group (not ITIN or ATIN)
            '123-45-0000': error_invalid,   # serial all zeros
            '123-00-6789': error_invalid,   # group all zeros
        }
        self.assertFieldOutput(forms.USTaxpayerIdentificationNumberField, valid, invalid)
