import random
import string

from django.core.validators import MaxLengthValidator
from django.test import TestCase

from localflavor.by import forms
from .forms import BYTestForm


class BYLocalFlavorTests(TestCase):

    def setUp(self):
        self.form = BYTestForm()
        self.valid_payload = {
            '': '',
        }

    def _gen_pass_id(self, is_valid):
        if is_valid:
            values = (
                ''.join(
                    list(str(random.randint(0, 9)) for n in range(7))
                    + list(random.choice(string.ascii_letters))
                    + list(str(random.randint(0, 9)) for n in range(3))
                    + list(random.choice(string.ascii_letters) for n in range(2))
                    + [str(random.randint(0, 9))]
                ) for n in range(random.randint(0, 200))
            )
        else:
            values = (
                ''.join(
                    list(str(random.randint(0, 9)) for n in range(random.randint(0, 9)))
                    + list(random.choice(string.ascii_letters) for n in range(2))
                    + list(str(random.randint(0, 9)) for n in range(random.randint(0, 9)))
                    + list(
                        random.choice(string.ascii_letters) for n in range(
                            random.randint(0, 9)
                        )
                    )
                    + [str(random.randint(0, 9))]
                )[:14] for n in range(random.randint(0, 200))
            )
        return values

    def test_form_fields(self):
        """Test that ModelForm creates valid field types for model fields."""
        fields = self.form.fields
        self.assertIsInstance(fields.get('region'), forms.BYRegionField)
        self.assertIsInstance(fields.get('pass_num'), forms.BYPassNumberField)
        self.assertIsInstance(fields.get('pass_id'), forms.BYPassIdNumberField)
        self.assertIsInstance(fields.get('postal_code'), forms.ByPostalCodeField)

    def test_BYRegions_select(self):
        """Test that BYRegionField has valid choices"""
        choices = self.form.fields.get('region').choices
        self.assertEqual(tuple(choices), forms.BY_REGIONS_CHOICES)

    def test_BYRegions_test(self):
        """Test that BYRegionField properly validates its unput"""
        error_message = self.form.fields.get('region').error_messages.get(
            'invalid_choice'
        )
        valid = {
            '1': '1',
            2: '2',
            3: '3',
            '4': '4',
            '5': '5',
        }
        nums = (10, '11', '22', 17, '1222', 1345)
        invalid = {
            num: [error_message % {'value': num}] for num in nums
        }
        self.assertFieldOutput(
            forms.BYRegionField, valid, invalid, empty_value=None
        )

    def test_BY_pass_num(self):
        """Test that ByPassNumberField properly validates its input."""
        invalid_regex = self.form.fields.get('pass_num').error_messages.get(
            'invalid'
        )

        valid_nums = ('AM8871722', 'BM7172588', 'MP1711922')
        valid = {
            num: num for num in valid_nums
        }

        invalid_nums = ('22117', 'CM22122', 'AM718')
        invalid = {
            num: [invalid_regex] for num in invalid_nums
        }

        self.assertFieldOutput(
            forms.BYPassNumberField, valid, invalid, empty_value=None
        )

    def test_BY_pass_id_num(self):
        """Test that ByPassIdNumberField properly validates its input."""
        invalid_regex = self.form.fields.get('pass_id').error_messages.get(
            'invalid'
        )

        valid = {
            value: value.upper() for value in self._gen_pass_id(True)
        }

        invalid = {
            value: [invalid_regex] for value in self._gen_pass_id(False)
        }
        self.assertFieldOutput(
            forms.BYPassIdNumberField, valid, invalid, empty_value=None
        )

    def test_BY_Postal_code(self):
        max_len = self.form.fields.get('postal_code').error_messages.get('max_length')
        min_len = self.form.fields.get('postal_code').error_messages.get('min_length')

        valid = {
            '210001': '210001',
            220050: '220050',
            225320: '225320',
            '225440': '225440',
            '225650': '225650',
            225370: '225370'
        }
        invalid = {
            2100001: [max_len],
            '111222333': [max_len],
            '131': [min_len],
        }

        self.assertFieldOutput(
            forms.ByPostalCodeField, valid, invalid, empty_value=None
        )
