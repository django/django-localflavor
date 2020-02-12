from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from localflavor.nl import forms, models, validators

from .forms import NLCarForm, NLPlaceForm
from .models import NLCar, NLPlace


class NLLocalFlavorValidatorTests(SimpleTestCase):
    def assert_validator(self, validator, valid=(), invalid=()):
        for item in valid:
            validator(item)

        for item in invalid:
            self.assertRaises(ValidationError, lambda: validator(item))

    def test_NLZipCodeValidator(self):
        valid = [
            '1234 AB',
            '2403 BW',
            '2612 JJ',
        ]
        invalid = [
            '0123 AB',
            '1123  BA'
            '11235BA'
            '3243 A1',
            'AA 1245',
            '1234-AB',
            'foo',
        ]
        self.assert_validator(validators.NLZipCodeFieldValidator(), valid, invalid)

    def test_NLBSNValidator(self):
        valid = [
            '123456782',
        ]
        invalid = [
            '000000000',
            '123456789',
            'foo',
        ]
        self.assert_validator(validators.NLBSNFieldValidator(), valid, invalid)

    def test_NLLicensePlateValidator(self):
        valid = [
            '12-AA-13',
            'CDJ-123',
            'AA-01',
        ]
        invalid = [
            'ZZZ-123',
            'AA-AAA-1',
            '11-123-A',
        ]
        self.assert_validator(validators.NLLicensePlateFieldValidator(), valid, invalid)


class NLLocalFlavorModelTests(SimpleTestCase):
    def test_NLZipCodeField(self):
        field = models.NLZipCodeField()

        self.assertEqual(field.to_python('1234AB'), '1234 AB')
        self.assertEqual(field.to_python(None), None)
        self.assertEqual(field.to_python(''), '')

        self.assertIsInstance(field.formfield(), forms.NLZipCodeField)

    def test_NL_model(self):
        m = NLPlace(**{
            'zipcode': '2403BW',
            'province': 'OV',
            'bsn': '123456782',
        })

        self.assertEqual(str(m.zipcode), '2403BW')
        self.assertEqual(str(m.province), 'OV')

        self.assertEqual(str(m.bsn), '123456782')

        m.clean_fields()

    def test_NL_model_cleanup(self):
        m = NLPlace(**{
            'zipcode': '2403 bwa',
            'province': 'OV',
            'bsn': '123456782',
        })
        # zipcode is not quite right, so it should raise an error
        self.assertRaises(ValidationError, lambda: m.clean_fields())

        # correct zipcode, should be clean now
        m.zipcode = '2403 bw'
        m.clean_fields()
        self.assertEqual(str(m.zipcode), '2403 BW')

    def test_NL_car(self):
        m = NLCar(**{
            'license_plate': 'AB-12-CD'
        })

        m.clean_fields()
        self.assertEqual(str(m.license_plate), 'AB-12-CD')

    def test_NL_car_cleanup(self):
        m = NLCar(**{
            'license_plate': 'AA11AA'
        })

        # incorrect license plate number, should raise an error
        self.assertRaises(ValidationError, lambda: m.clean_fields())

        # correct license plate number, should be clean now
        m.license_plate = 'AA-11-AA'
        m.clean_fields()
        self.assertEqual(str(m.license_plate), 'AA-11-AA')


class NLLocalFlavorFormTests(SimpleTestCase):
    def test_NLZipCodeField(self):
        error_invalid = ['Enter a valid zip code.']
        valid = {
            '1234ab': '1234 AB',
            '1234 ab': '1234 AB',
            '1234 AB': '1234 AB',
            # superfluous spaces should get cleaned off
            '1234   AB ': '1234 AB',
            ' 1234AB ': '1234 AB',
        }
        invalid = {
            '0123AB': error_invalid,
            'foo': error_invalid,
            '1234ABC': error_invalid,
            '1234A': error_invalid,
        }
        self.assertFieldOutput(forms.NLZipCodeField, valid, invalid)

    def test_NLProvinceSelect(self):
        f = forms.NLProvinceSelect()
        out = '''<select name="provinces">
<option value="DR">Drenthe</option>
<option value="FL">Flevoland</option>
<option value="FR">Fryslân</option>
<option value="GL">Gelderland</option>
<option value="GR">Groningen</option>
<option value="LB">Limburg</option>
<option value="NB">Noord-Brabant</option>
<option value="NH">Noord-Holland</option>
<option value="OV" selected="selected">Overijssel</option>
<option value="UT">Utrecht</option>
<option value="ZE">Zeeland</option>
<option value="ZH">Zuid-Holland</option>
</select>'''
        self.assertHTMLEqual(f.render('provinces', 'OV'), out)

    def test_NLBSNFormField(self):
        error_invalid = ['Enter a valid BSN.']
        valid = {
            '123456782': '123456782',
        }
        invalid = {
            '000000000': error_invalid,
            '123456789': error_invalid,
            'foo': error_invalid,
        }
        self.assertFieldOutput(forms.NLBSNFormField, valid, invalid)

    def test_NL_ModelForm_errors(self):
        form = NLPlaceForm({
            'zipcode': 'invalid',
            'province': 'invalid',
            'bsn': 'invalid',
        })

        self.assertFalse(form.is_valid())

        invalid_choice = 'Select a valid choice. invalid is not one of the available choices.'
        self.assertEqual(form.errors['zipcode'], ['Enter a valid zip code.'])
        self.assertEqual(form.errors['province'], [invalid_choice])
        self.assertEqual(form.errors['bsn'], ['Enter a valid BSN.'])

    def test_NL_ModelForm_valid(self):
        form = NLPlaceForm({
            'zipcode': '2233 AB',
            'province': 'OV',
            'bsn': '123456782',
        })
        self.assertTrue(form.is_valid())

    def test_NLLicensePlateFormField(self):
        error_invalid = ['Enter a valid license plate']
        valid = {
            '12-AAA-1': '12-AAA-1',
            '12-AAA-1': '12-AAA-1',
            'CDJ-123': 'CDJ-123',
        }
        invalid = {
            'AAA-AA-1': error_invalid,
            'CDA-111': error_invalid,
            'a1s2d3': error_invalid,
        }
        self.assertFieldOutput(forms.NLLicensePlateFormField, valid, invalid)

    def test_NL_car_ModelForm_valid(self):
        form = NLCarForm({
            'license_plate': 'AA-11-AA',
        })

        self.assertTrue(form.is_valid())

    def test_NL_car_ModelForm_invalid(self):
        form = NLCarForm({
            'license_plate': 'AA-AAA-1',
        })

        self.assertFalse(form.is_valid())
