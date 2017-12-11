# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from localflavor.nl import forms, models, validators

from .forms import NLPlaceForm
from .models import NLPlace


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
        self.assertEquals(str(m.zipcode), '2403 BW')


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
