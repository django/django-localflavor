"""
Kuwait-specific Form helpers
"""
from __future__ import unicode_literals

import textwrap
from datetime import date

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import RegexField
from django.utils.translation import gettext_lazy as _


def has_valid_checksum(value):
    weight = (2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    calculated_checksum = 0
    for i in range(11):
        calculated_checksum += int(value[i]) * weight[i]

    remainder = calculated_checksum % 11
    checkdigit = 11 - remainder
    if checkdigit != int(value[11]):
        return False
    return True


class KWCivilIDNumberField(RegexField):
    """
    Kuwaiti Civil ID numbers are 12 digits, second to seventh digits
    represents the person's birthdate.

    Checks the following rules to determine the validty of the number:
        * The number consist of 12 digits.
        * The birthdate of the person is a valid date.
        * The calculated checksum equals to the last digit of the Civil ID.
    """
    default_error_messages = {
        'invalid': _('Enter a valid Kuwaiti Civil ID number'),
    }

    def __init__(self, max_length=12, min_length=12, *args, **kwargs):
        super(KWCivilIDNumberField, self).__init__(r'\d{12}',
                                                   max_length,
                                                   min_length, *args, **kwargs)

    def clean(self, value):
        super(KWCivilIDNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        cc = value[0]  # Century value
        yy, mm, dd = textwrap.wrap(value[1:7], 2)  # Date parts

        # Fix the dates so that those born
        # in 2000+ pass the validation check
        if int(cc) == 3:
            yy = '20{}'.format(yy)
        elif int(cc) == 2:
            yy = '19{}'.format(yy)

        try:
            date(int(yy), int(mm), int(dd))
        except ValueError:
            raise ValidationError(self.error_messages['invalid'])

        if not has_valid_checksum(value):
            raise ValidationError(self.error_messages['invalid'])

        return value
