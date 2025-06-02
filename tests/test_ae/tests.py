from django.test import TestCase
from django.core.exceptions import ValidationError
from unittest.mock import patch

from localflavor.ae import forms
from localflavor.ae.validators import UAEEmiratesIDValidator, UAEPostalCodeValidator, UAEPOBoxValidator

from .forms import UAEPlaceForm


class UAELocalFlavorTests(TestCase):

    def setUp(self):
        self.form = UAEPlaceForm({
            'name': 'Test Location',
            'emirate': 'DU',
            'emirates_id': '784-1984-1234567-1',
            'postal_code': '00000',
            'po_box': '12345',
            'tax_number': '123456789012345',
        })

    def test_get_display_methods(self):
        """Test that the get_*_display() methods are added to the model instances."""
        place = self.form.save()
        self.assertEqual(place.get_emirate_display(), 'Dubai')

    def test_required_fields(self):
        """Test that required fields throw appropriate errors."""
        form = UAEPlaceForm({'name': 'Test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['emirate'], ['This field is required.'])

    def test_UAEEmiratesIDField(self):
        """Test Emirates ID validation."""
        error_invalid = ['Enter a valid UAE Emirates ID number in format 784-YYYY-NNNNNNN-N.']

        valid = {
            '784-1984-1234567-1': '784-1984-1234567-1',
            '784198412345671': '784-1984-1234567-1',
            '784 1984 1234567 1': '784-1984-1234567-1',
            '784-2000-9876543-2': '784-2000-9876543-2',
        }
        invalid = {
            '123-1984-1234567-1': error_invalid,  # Wrong country code
            '784-1800-1234567-1': error_invalid,  # Year too old
            '784-2200-1234567-1': error_invalid,  # Year too new
            '78419841234567': error_invalid,      # Too short
            '7841984123456789': error_invalid,    # Too long
            'invalid': error_invalid,
        }
        self.assertFieldOutput(forms.UAEEmiratesIDField, valid, invalid)

    def test_UAEEmiratesIDField_invalid_format_returns_original(self):
        """Test that invalid Emirates ID format returns original value (line 50)."""
        field = forms.UAEEmiratesIDField(required=False)
        field.validators = []

        result = field.clean('78412345')
        self.assertEqual(result, '78412345')

    def test_UAEEmirateField(self):
        """Test Emirate field validation."""
        field = forms.UAEEmirateField()
        self.assertEqual(field.clean('DU'), 'DU')
        self.assertEqual(field.clean('AZ'), 'AZ')

        with self.assertRaises(ValidationError):
            field.clean('XX')

    def test_UAEPostalCodeField(self):
        """Test postal code validation."""
        field = forms.UAEPostalCodeField()

        self.assertEqual(field.clean('00000'), '00000')
        self.assertEqual(field.clean(''), '')

        with self.assertRaises(ValidationError):
            field.clean('12345')

        with self.assertRaises(ValidationError):
            field.clean('invalid')

    def test_UAEPostalCodeField_fallback_logic(self):
        """Test postal code field fallback return (line 99)."""
        field = forms.UAEPostalCodeField(required=False)
        field.validators = []

        result = field.clean('12345')
        self.assertEqual(result, '12345')

    def test_UAEPOBoxField(self):
        """Test P.O. Box validation."""
        error_invalid = ['Enter a valid P.O. Box number.']

        valid = {
            '12345': '12345',
            '1': '1',
            '1234567890': '1234567890',
            'P.O. Box 12345': '12345',
            'PO BOX 12345': '12345',
            'P.O.Box 12345': '12345',
            'po box 12345': '12345',
        }
        invalid = {
            '12345678901': error_invalid,  # Too long
            'abc': error_invalid,
            '123abc': error_invalid,
            'P.O. Box abc': error_invalid,
        }
        self.assertFieldOutput(forms.UAEPOBoxField, valid, invalid)

    def test_UAEPOBoxField_fallback_logic(self):
        """Test P.O. Box field fallback return (line 136)."""
        field = forms.UAEPOBoxField(required=False)
        field.validators = []

        result = field.clean('P.O. Box abc')
        self.assertEqual(result, 'P.O. Box abc')

    def test_UAETaxRegistrationNumberField(self):
        """Test Tax Registration Number validation."""
        error_invalid = ['Enter a valid UAE Tax Registration Number (15 digits).']

        valid = {
            '123456789012345': '123456789012345',
            '100000000000001': '100000000000001',
        }
        invalid = {
            '12345678901234': error_invalid,   # Too short
            '1234567890123456': error_invalid, # Too long
            'abc456789012345': error_invalid,  # Contains letters
        }
        self.assertFieldOutput(forms.UAETaxRegistrationNumberField, valid, invalid)

    def test_UAEEmirateSelect(self):
        """Test UAE Emirate Select widget."""
        f = forms.UAEEmirateSelect()
        out = '''<select name="emirate">
<option value="AZ">Abu Dhabi</option>
<option value="AJ">Ajman</option>
<option value="DU" selected="selected">Dubai</option>
<option value="FU">Fujairah</option>
<option value="RA">Ras Al Khaimah</option>
<option value="SH">Sharjah</option>
<option value="UQ">Umm Al Quwain</option>
</select>'''
        self.assertHTMLEqual(f.render('emirate', 'DU'), out)

    def test_form_widget_html(self):
        """Test that form widgets render correctly."""
        form = UAEPlaceForm({
            'name': 'Test Location',
            'emirate': 'DU',
            'emirates_id': '784-1984-1234567-1',
            'postal_code': '00000',
            'po_box': '12345',
            'tax_number': '123456789012345',
        })

        emirate_html = str(form['emirate'])
        self.assertIn('Dubai', emirate_html)
        self.assertIn('Abu Dhabi', emirate_html)

        emirates_id_html = str(form['emirates_id'])
        self.assertIn('784-1984-1234567-1', emirates_id_html)

    def test_error_messages(self):
        """Test error messages for invalid data."""
        form = UAEPlaceForm({
            'name': 'Test Location',
            'emirate': 'invalid',
            'emirates_id': 'invalid',
            'postal_code': 'invalid',
            'po_box': 'invalid',
            'tax_number': 'invalid',
        })

        self.assertFalse(form.is_valid())

        self.assertIn('Select a valid choice', str(form.errors['emirate']))
        self.assertIn('Enter a valid UAE Emirates ID', str(form.errors['emirates_id']))
        self.assertIn('Enter a valid UAE postal code', str(form.errors['postal_code']))
        self.assertIn('Enter a valid P.O. Box', str(form.errors['po_box']))
        self.assertIn('Enter a valid UAE Tax Registration Number', str(form.errors['tax_number']))

    def test_empty_values(self):
        """Test that empty values are handled correctly for optional fields."""
        form = UAEPlaceForm({
            'name': 'Test Location',
            'emirate': 'DU',
            'emirates_id': '',
            'postal_code': '',
            'po_box': '',
            'tax_number': '',
        })

        self.assertTrue(form.is_valid())
        place = form.save()
        self.assertEqual(place.name, 'Test Location')
        self.assertEqual(place.emirate, 'DU')
        self.assertEqual(place.emirates_id, '')
        self.assertEqual(place.postal_code, '')
        self.assertEqual(place.po_box, '')
        self.assertEqual(place.tax_number, '')


class UAEValidatorTests(TestCase):
    """Additional tests to achieve 100% coverage of validators."""

    def test_emirates_id_validator_custom_params(self):
        """Test Emirates ID validator with custom message and code (lines 26, 28)."""
        custom_message = 'Custom Emirates ID error'
        custom_code = 'custom_code'
        validator = UAEEmiratesIDValidator(message=custom_message, code=custom_code)

        self.assertEqual(validator.message, custom_message)
        self.assertEqual(validator.code, custom_code)

        with self.assertRaises(ValidationError) as cm:
            validator('invalid')

        self.assertEqual(str(cm.exception.message), custom_message)
        self.assertEqual(cm.exception.code, custom_code)

    def test_emirates_id_validator_empty_value(self):
        """Test Emirates ID validator with empty value (line 33)."""
        validator = UAEEmiratesIDValidator()

        validator(None)
        validator('')
        validator(False)
        validator(0)

    def test_emirates_id_validator_year_range(self):
        """Test Emirates ID validator with year boundary validation (line 54)."""
        validator = UAEEmiratesIDValidator()

        with self.assertRaises(ValidationError):
            validator('784189912345671')

        with self.assertRaises(ValidationError):
            validator('784215112345671')

    @patch('builtins.int')
    def test_emirates_id_validator_value_error(self, mock_int):
        """Test Emirates ID validator ValueError exception handling (line 54)."""
        validator = UAEEmiratesIDValidator()

        # Mock int() to raise ValueError
        mock_int.side_effect = ValueError("invalid literal")

        with self.assertRaises(ValidationError):
            validator('784200012345671')  # Valid format but int() will fail

    def test_postal_code_validator_custom_params(self):
        """Test postal code validator with custom message and code (lines 69, 71)."""
        custom_message = 'Custom postal code error'
        custom_code = 'custom_postal_code'
        validator = UAEPostalCodeValidator(message=custom_message, code=custom_code)

        self.assertEqual(validator.message, custom_message)
        self.assertEqual(validator.code, custom_code)

        with self.assertRaises(ValidationError) as cm:
            validator('12345')

        self.assertEqual(str(cm.exception.message), custom_message)
        self.assertEqual(cm.exception.code, custom_code)

    def test_postal_code_validator_empty_value(self):
        """Test postal code validator with empty value (line 76)."""
        validator = UAEPostalCodeValidator()

        validator(None)
        validator('')
        validator(False)
        validator(0)

    def test_po_box_validator_custom_params(self):
        """Test P.O. Box validator with custom message and code (lines 97, 99)."""
        custom_message = 'Custom P.O. Box error'
        custom_code = 'custom_po_box'
        validator = UAEPOBoxValidator(message=custom_message, code=custom_code)

        self.assertEqual(validator.message, custom_message)
        self.assertEqual(validator.code, custom_code)

        with self.assertRaises(ValidationError) as cm:
            validator('invalid')

        self.assertEqual(str(cm.exception.message), custom_message)
        self.assertEqual(cm.exception.code, custom_code)

    def test_po_box_validator_empty_value(self):
        """Test P.O. Box validator with empty value (line 104)."""
        validator = UAEPOBoxValidator()

        validator(None)
        validator('')
        validator(False)
        validator(0)
