import re

from django.core.exceptions import ValidationError
from django.test import TestCase

from localflavor.au import forms, models
from localflavor.au.validators import (AUBusinessNumberFieldValidator, AUCompanyNumberFieldValidator,
                                       AUTaxFileNumberFieldValidator)

from .forms import AustralianPlaceForm
from .models import AustralianPlace

SELECTED_OPTION_PATTERN = r'<option value="%s" selected>'
BLANK_OPTION_PATTERN = r'<option value="">'
INPUT_VALUE_PATTERN = r'<input[^>]*value="%s"[^>]*>'


class AULocalflavorTests(TestCase):

    def setUp(self):
        self.form = AustralianPlaceForm(
            {'state': 'WA',
             'state_required': 'QLD',
             'name': 'dummy',
             'postcode': '1234',
             'postcode_required': '4321',
             'abn': '74457506140',
             'tfn': '123456782'
             })

    def test_get_display_methods(self):
        """Ensure get_*_display() methods are added to model instances."""
        place = self.form.save()
        self.assertEqual(place.get_state_display(), 'Western Australia')
        self.assertEqual(place.get_state_required_display(), 'Queensland')

    def test_default_values(self):
        """Ensure that default values are selected in forms."""
        form = AustralianPlaceForm()
        self.assertTrue(re.search(SELECTED_OPTION_PATTERN % 'NSW',
                                  str(form['state_default'])))
        self.assertTrue(re.search(INPUT_VALUE_PATTERN % '2500',
                                  str(form['postcode_default'])))

    def test_required(self):
        """Test that required AUStateFields throw appropriate errors."""
        form = AustralianPlaceForm({'state': 'NSW', 'name': 'Wollongong'})
        self.assertFalse(form.is_valid())
        self.assertEqual(set(form.errors.keys()),
                         set(('state_required',
                              'postcode_required',
                              'abn', 'tfn')))
        self.assertEqual(
            form.errors['state_required'], ['This field is required.'])
        self.assertEqual(
            form.errors['postcode_required'], ['This field is required.'])
        self.assertEqual(
            form.errors['abn'], ['This field is required.'])
        self.assertEqual(
            form.errors['tfn'], ['This field is required.'])

    def test_field_blank_option(self):
        """Test that the empty option is there."""
        self.assertTrue(re.search(BLANK_OPTION_PATTERN,
                                  str(self.form['state'])))

    def test_selected_values(self):
        """Ensure selected states match the initial values provided."""
        self.assertTrue(re.search(SELECTED_OPTION_PATTERN % 'WA',
                                  str(self.form['state'])))
        self.assertTrue(re.search(SELECTED_OPTION_PATTERN % 'QLD',
                                  str(self.form['state_required'])))
        self.assertTrue(re.search(INPUT_VALUE_PATTERN % '1234',
                                  str(self.form['postcode'])))
        self.assertTrue(re.search(INPUT_VALUE_PATTERN % '4321',
                                  str(self.form['postcode_required'])))

    def test_AUStateSelect(self):
        f = forms.AUStateSelect()
        out = '''<select name="state">
<option value="ACT">Australian Capital Territory</option>
<option value="NSW" selected="selected">New South Wales</option>
<option value="NT">Northern Territory</option>
<option value="QLD">Queensland</option>
<option value="SA">South Australia</option>
<option value="TAS">Tasmania</option>
<option value="VIC">Victoria</option>
<option value="WA">Western Australia</option>
</select>'''
        self.assertHTMLEqual(f.render('state', 'NSW'), out)

    def test_AUPostCodeField(self):
        error_format = ['Enter a 4 digit postcode.']
        valid = {
            '1234': '1234',
            '2000': '2000',
        }
        invalid = {
            'abcd': error_format,
            '20001': ['Ensure this value has at most 4 characters (it has 5).'] + error_format,
        }
        self.assertFieldOutput(forms.AUPostCodeField, valid, invalid)

    def test_abn(self):
        error_format = ['Enter a valid ABN.']
        valid = {
            '53004085616': '53004085616',
            '53 004 085 616': '53004085616',
        }
        invalid = {
            '53004085617': error_format,
            '5300A085616': error_format,
        }
        self.assertFieldOutput(forms.AUBusinessNumberField, valid, invalid)

    def test_acn(self):
        error_format = ['Enter a valid ACN.']
        valid = {
            '604327504': '604327504',
            '604 327 504': '604327504',
        }
        invalid = {
            '604327505': error_format,
            '60A327504': error_format,
        }
        self.assertFieldOutput(forms.AUCompanyNumberField, valid, invalid)

    def test_tfn(self):
        error_format = ['Enter a valid TFN.']
        valid = {
            '123456782': '123456782',
            '123 456 782': '123 456 782'
        }
        invalid = {
            '123456789': error_format,    # wrong number
            '12345678B': error_format,    # letter at the end
        }
        self.assertFieldOutput(forms.AUTaxFileNumberField, valid, invalid)


class AULocalFlavorAUBusinessNumberFieldValidatorTests(TestCase):

    def test_no_error_for_a_valid_abn(self):
        """Test a valid ABN does not cause an error."""

        valid_abn = '53004085616'
        validator = AUBusinessNumberFieldValidator()
        validator(valid_abn)

    def test_raises_error_for_abn_containing_a_letter(self):
        """Test an ABN containing a letter is invalid."""

        invalid_abn = '5300408561A'
        validator = AUBusinessNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_abn))

    def test_raises_error_for_too_short_abn(self):
        """Test an ABN with fewer than eleven digits is invalid."""

        invalid_abn = '5300408561'
        validator = AUBusinessNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_abn))

    def test_raises_error_for_too_long_abn(self):
        """Test an ABN with more than eleven digits is invalid."""

        invalid_abn = '530040856160'
        validator = AUBusinessNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_abn))

    def test_raises_error_for_whitespace(self):
        """Test an ABN can be valid when it contains whitespace."""

        # NB: Form field should strip the whitespace before regex validation is run.
        invalid_abn = '5300 4085 616'
        validator = AUBusinessNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_abn))

    def test_raises_error_for_invalid_abn(self):
        """Test that an ABN must pass the ATO's validation algorithm."""

        invalid_abn = '53004085617'
        validator = AUBusinessNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_abn))


class AULocalFlavorAUCompanyNumberFieldValidatorTests(TestCase):

    def test_no_error_for_a_valid_acn(self):
        """Test a valid ACN does not cause an error."""

        valid_acn = '604327504'
        validator = AUCompanyNumberFieldValidator()
        validator(valid_acn)

    def test_raises_error_for_acn_containing_a_letter(self):
        """Test an ACN containing a letter is invalid."""

        invalid_acn = '60432750A'
        validator = AUCompanyNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_acn))

    def test_raises_error_for_too_short_acn(self):
        """Test an ACN with fewer than nine digits is invalid."""

        invalid_acn = '60432750'
        validator = AUCompanyNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_acn))

    def test_raises_error_for_too_long_acn(self):
        """Test an ACN with more than nine digits is invalid."""

        invalid_acn = '6043275040'
        validator = AUCompanyNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_acn))

    def test_raises_error_for_whitespace(self):
        """Test an ACN can be valid when it contains whitespace."""

        # NB: Form field should strip the whitespace before regex validation is run.
        invalid_acn = '604 327 504'
        validator = AUCompanyNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_acn))

    def test_raises_error_for_invalid_acn(self):
        """Test that an ACN must pass the ATO's validation algorithm."""

        invalid_acn = '604327509'
        validator = AUCompanyNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_acn))


class AULocalFlavorAUTaxFileNumberFieldValidatorTests(TestCase):

    def test_no_error_for_a_valid_tfn(self):
        """Test a valid TFN does not cause an error."""
        valid_tfn = '123456782'
        validator = AUTaxFileNumberFieldValidator()
        validator(valid_tfn)

    def test_no_error_for_valid_tfn_with_whitespace(self):
        """Test a TFN can be valid when it contains whitespace."""
        valid_tfn = '123 456 782'
        validator = AUTaxFileNumberFieldValidator()
        validator(valid_tfn)

    def test_raises_error_for_tfn_containing_a_letter(self):
        """Test an TFN containing a letter is invalid."""
        invalid_tfn = '12345678W'
        validator = AUTaxFileNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_tfn))

    def test_raises_error_for_too_short_tfn(self):
        """Test a TFN with fewer than 8 digits is invalid."""
        invalid_tfn = '1234567'
        validator = AUTaxFileNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_tfn))

    def test_raises_error_for_too_long_tfn(self):
        """Test a TFN with more than 9 digits is invalid."""
        invalid_tfn = '1234567890'
        validator = AUTaxFileNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_tfn))

    def test_raises_error_for_invalid_tfn(self):
        """Test that a TFN must pass the ATO's validation algorithm."""
        invalid_tfn = '123456783'
        validator = AUTaxFileNumberFieldValidator()
        self.assertRaises(ValidationError, lambda: validator(invalid_tfn))

    def test_old_tfn(self):
        """Test old, 8-digit TFNs."""
        validator = AUTaxFileNumberFieldValidator()
        old_valid_tfn = '38593474'
        validator(old_valid_tfn)
        old_invalid_tfn = '38593475'
        self.assertRaises(ValidationError, lambda: validator(old_invalid_tfn))


class AULocalFlavorAUBusinessNumberModelTests(TestCase):

    def test_AUBusinessNumberModel_invalid_abn_raises_error(self):

        place = AustralianPlace(**{
            'state': 'WA',
            'state_required': 'QLD',
            'name': 'dummy',
            'postcode': '1234',
            'postcode_required': '4321',
            'abn': '5300 4085 616 INVALID',
            'tfn': '123456782'
        })

        self.assertRaises(ValidationError, place.clean_fields)


class AULocalFlavourAUBusinessNumberFormFieldTests(TestCase):

    def test_abn_with_spaces_remains_unchanged(self):
        """Test that an ABN with the formatting we expect is unchanged."""
        field = forms.AUBusinessNumberField()

        self.assertEqual('53 004 085 616', field.prepare_value('53 004 085 616'))

    def test_spaces_are_reconfigured(self):
        """Test that an ABN with formatting we don't expect is transformed."""
        field = forms.AUBusinessNumberField()

        self.assertEqual('53 004 085 616', field.prepare_value('53004085616'))
        self.assertEqual('53 004 085 616', field.prepare_value('53 0 04 08561 6'))


class AULocalFlavourAUCompanyNumberFormFieldTests(TestCase):

    def test_abn_with_spaces_remains_unchanged(self):
        """Test that an ACN with the formatting we expect is unchanged."""
        field = forms.AUCompanyNumberField()

        self.assertEqual('604 327 504', field.prepare_value('604 327 504'))

    def test_spaces_are_reconfigured(self):
        """Test that an ACN with formatting we don't expect is transformed."""
        field = forms.AUCompanyNumberField()

        self.assertEqual('604 327 504', field.prepare_value('604327504'))
        self.assertEqual('604 327 504', field.prepare_value('60 4 32750 4'))


class AULocalFlavourAUTaxFileNumberFormFieldTests(TestCase):

    def test_tfn_with_spaces_remains_unchanged(self):
        """Test that a TFN with the formatting we expect is unchanged."""
        field = forms.AUTaxFileNumberField()

        self.assertEqual('123 456 782', field.prepare_value('123 456 782'))

    def test_spaces_are_reconfigured(self):
        """Test that a TFN with formatting we don't expect is transformed."""
        field = forms.AUTaxFileNumberField()

        self.assertEqual('123 456 782', field.prepare_value('123456782'))
        self.assertEqual('123 456 782', field.prepare_value('12 345 678 2'))


class AULocalFlavourAUBusinessNumberModelFieldTests(TestCase):

    def test_to_python_strips_whitespace(self):
        """Test the value is stored without whitespace."""
        field = models.AUBusinessNumberField()

        self.assertEqual('53004085616', field.to_python('53 004 085 616'))


class AULocalFlavourAUTaxFileNumberModelFieldTests(TestCase):

    def test_to_python_strips_whitespace(self):
        """Test the value is stored without whitespace."""
        field = models.AUTaxFileNumberField()

        self.assertEqual('123456782', field.to_python('123 456 782'))
