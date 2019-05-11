"""Egypt-specific Form helpers."""
import textwrap
from datetime import date

from django.forms import ValidationError
from django.forms.fields import CharField, Select
from django.utils.translation import gettext_lazy as _

from .choices import GOVERNORATE_CHOICES


class EGNationalIDNumberField(CharField):
    """
    Egypt ID numbers are 14 digits, second to seventh digits represents the person's birthdate.

    Checks the following rules to determine the validity of the number:
        * The number consist of 14 digits.
        * The birthdate of the person is a valid date.
        * The calculated checksum equals to the last digit of the National ID.
    """

    default_error_messages = {
        'invalid': _('Enter a valid Egypt ID number'),
    }

    def __init__(self, max_length=14, min_length=14, *args, **kwargs):
        super().__init__(
            r'\d{14}', max_length=max_length, min_length=min_length,
            *args, **kwargs
        )

    def clean(self, value):
        super().clean(value)
        if value in self.empty_values:
            return self.empty_value

        century = value[0]
        year, month, day = textwrap.wrap(value[1:7], 2)
        governorate_code = value[7:9]

        # Complete year (19XX, 20XX)
        if int(century) == 3:
            year = '20{}'.format(year)
        elif int(century) == 2:
            year = '19{}'.format(year)
        # is valid date?
        try:
            date(int(year), int(month), int(day))
        except ValueError:
            raise ValidationError(self.error_messages['invalid'])

        # is valid governorate code?
        governorate_codes = (
            '01', '02', '03', '04', '11', '12', '13', '14', '15', '16', '17', '18', '19', '21',
            '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '34', '35', '88')
        if governorate_code not in governorate_codes:
            raise ValidationError(self.error_messages['invalid'])

        return value


class EGGovernorateSelect(Select):
    """
    A Select widget that uses a list of Egypt governorates as its choices.
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=GOVERNORATE_CHOICES)
