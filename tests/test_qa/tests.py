from django.core.exceptions import ValidationError
from django.db.migrations.serializer import serializer_factory
from django.test import TestCase

from localflavor.qa import forms
from localflavor.qa.models import QAMunicipalityField, QANationalIDField
from localflavor.qa.validators import QANationalIDValidator

from .forms import QAPlaceForm
from .models import QAPlace


VALID_QA_IDS = (
    '30363412345',
    '29984054321',
    '29535600001',
)

# (value, reason)
INVALID_QA_ID_CASES = (
    ('10363412345', 'Invalid century digit (must be 2 or 3)'),
    ('30900012345', 'Invalid ISO 3166 numeric nationality code (000)'),
    ('39963412345', 'Future birth year (2099)'),
    ('3036341234A', 'Non-digit character present'),
    ('3036341234',  'Too short (10 digits)'),
    ('303634123456', 'Too long (12 digits)'),
)

DEFAULT_ERROR_MESSAGE = 'Enter a valid Qatari National ID number'

class QANationalIDFormFieldTests(TestCase):
    def setUp(self):
        self.field = forms.QANationalIDNumberField()

    def _assert_invalid(self, value):
        with self.assertRaises(ValidationError) as cm:
            self.field.clean(value)
        self.assertIn(DEFAULT_ERROR_MESSAGE, cm.exception.messages)

    def test_accepts_valid_values(self):
        for value in VALID_QA_IDS:
            with self.subTest(value=value):
                self.assertEqual(self.field.clean(value), value)

    def test_rejects_invalid_values(self):
        for value, reason in INVALID_QA_ID_CASES:
            with self.subTest(value=value, reason=reason):
                self._assert_invalid(value)

    def test_optional_accepts_empty_string(self):
        field = forms.QANationalIDNumberField(required=False)
        self.assertEqual(field.clean(''), '')


class QANationalIDFormTests(TestCase):
    def test_valid_submission(self):
        valid_id = VALID_QA_IDS[0]
        form = QAPlaceForm({'name': 'Test Location', 'national_id': valid_id})
        self.assertTrue(form.is_valid())
        place = form.save()
        self.assertEqual(place.national_id, valid_id)

    def test_invalid_id_produces_correct_error(self):
        invalid_id = INVALID_QA_ID_CASES[0][0]
        form = QAPlaceForm({'name': 'Test Location', 'national_id': invalid_id})
        self.assertFalse(form.is_valid())
        self.assertIn(DEFAULT_ERROR_MESSAGE, form.errors['national_id'])


class QANationalIDValidatorTests(TestCase):
    def setUp(self):
        self.validator = QANationalIDValidator()

    def test_accepts_valid_values(self):
        for value in VALID_QA_IDS:
            with self.subTest(value=value):
                self.validator(value)

    def test_rejects_invalid_values(self):
        for value, reason in INVALID_QA_ID_CASES:
            with self.subTest(value=value, reason=reason):
                with self.assertRaises(ValidationError):
                    self.validator(value)

    def test_skips_empty_string(self):
        self.validator('')

    def test_skips_none(self):
        self.validator(None)

    def test_custom_message_and_code(self):
        validator = QANationalIDValidator(message='Custom error', code='custom_code')
        with self.assertRaises(ValidationError) as cm:
            validator('not-valid')
        self.assertEqual(cm.exception.message, 'Custom error')
        self.assertEqual(cm.exception.code, 'custom_code')

    def test_is_migration_serializable(self):
        serializer_factory(self.validator).serialize()


class QANationalIDModelFieldTests(TestCase):
    def test_always_includes_validator(self):
        # Ensure the validator is appended even when validators= is overridden
        field = QANationalIDField(validators=())
        self.assertTrue(any(isinstance(v, QANationalIDValidator) for v in field.validators))

    def test_formfield_class(self):
        self.assertIsInstance(QANationalIDField().formfield(), forms.QANationalIDNumberField)

    def test_full_clean_rejects_invalid_id(self):
        invalid_id = INVALID_QA_ID_CASES[0][0]
        place = QAPlace(name='Test', national_id=invalid_id)
        with self.assertRaises(ValidationError) as cm:
            place.full_clean()
        self.assertIn(
            DEFAULT_ERROR_MESSAGE,
            cm.exception.message_dict['national_id'],
        )


class QAMunicipalityFormFieldTests(TestCase):
    def setUp(self):
        self.field = forms.QAMunicipalityField()

    def test_accepts_iso_codes(self):
        for code in ('DA', 'KH', 'RA', 'MS', 'SH', 'WA', 'ZA', 'US'):
            with self.subTest(code=code):
                self.assertEqual(self.field.clean(code), code)

    def test_accepts_english_names(self):
        cases = {
            'Doha': 'DA', 'doha': 'DA',
            'Al Rayyan': 'RA', 'al rayyan': 'RA',
            'Al Wakrah': 'WA',
            'Umm Salal': 'US',
        }
        for name, expected in cases.items():
            with self.subTest(name=name):
                self.assertEqual(self.field.clean(name), expected)

    def test_accepts_arabic_names(self):
        cases = {
            'الدوحة': 'DA',
            'الريان': 'RA',
            'الوكرة': 'WA',
            'الضعاين': 'ZA',
            'أم صلال': 'US',
        }
        for name, expected in cases.items():
            with self.subTest(name=name):
                self.assertEqual(self.field.clean(name), expected)

    def test_rejects_invalid_values(self):
        for value in ('المعادي', 'Cairo', 'Wakanda'):
            with self.subTest(value=value):
                with self.assertRaises(ValidationError):
                    self.field.clean(value)

    def test_rejects_empty_values(self):
        for empty in ('', None):
            with self.subTest(value=empty):
                with self.assertRaises(ValidationError):
                    self.field.clean(empty)


class QAMunicipalityModelFieldTests(TestCase):
    def test_formfield_class(self):
        self.assertIsInstance(QAMunicipalityField().formfield(), forms.QAMunicipalityField)

    def test_deconstruct_omits_choices(self):
        _, _, _, kwargs = QAMunicipalityField().deconstruct()
        self.assertNotIn('choices', kwargs)
