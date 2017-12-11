from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select
from django.utils.translation import ugettext_lazy as _

from .tr_provinces import PROVINCE_CHOICES


class TRPostalCodeField(RegexField):
    """
    A form field that validates input as a Turkish zip code.

    Valid codes consist of five digits.
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in the format XXXXX.'),
    }

    def __init__(self, max_length=5, min_length=5, *args, **kwargs):
        super(TRPostalCodeField, self).__init__(
            r'^\d{5}$', max_length=max_length, min_length=min_length,
            *args, **kwargs
        )

    def clean(self, value):
        value = super(TRPostalCodeField, self).clean(value)
        if value in self.empty_values:
            return self.empty_value
        if len(value) != 5:
            raise ValidationError(self.error_messages['invalid'])
        province_code = int(value[:2])
        if province_code == 0 or province_code > 81:
            raise ValidationError(self.error_messages['invalid'])
        return value


class TRIdentificationNumberField(Field):
    """
    A Turkey Identification Number number.

    See: http://tr.wikipedia.org/wiki/T%C3%BCrkiye_Cumhuriyeti_Kimlik_Numaras%C4%B1

    Checks the following rules to determine whether the number is valid:

        * The number is 11-digits.
        * First digit is not 0.
        * Conforms to the following two formula:
          (sum(1st, 3rd, 5th, 7th, 9th)*7 - sum(2nd,4th,6th,8th)) % 10 = 10th digit
          sum(1st to 10th) % 10 = 11th digit
    """

    default_error_messages = {
        'invalid': _('Enter a valid Turkish Identification number.'),
        'not_11': _('Turkish Identification number must be 11 digits.'),
    }

    def clean(self, value):
        super(TRIdentificationNumberField, self).clean(value)

        if value in EMPTY_VALUES:
            return ''

        if len(value) != 11:
            raise ValidationError(self.error_messages['not_11'])

        if not re.match(r'^\d{11}$', value):
            raise ValidationError(self.error_messages['invalid'])

        if int(value[0]) == 0:
            raise ValidationError(self.error_messages['invalid'])

        chksum = (sum([int(value[i]) for i in range(0, 9, 2)]) * 7 -
                  sum([int(value[i]) for i in range(1, 9, 2)])) % 10

        if (chksum != int(value[9]) or
                (sum([int(value[i])
                      for i in range(10)]) % 10) != int(value[10])):
            raise ValidationError(self.error_messages['invalid'])

        return value


class TRProvinceSelect(Select):
    """A Select widget that uses a list of provinces in Turkey as its choices."""

    def __init__(self, attrs=None):
        super(TRProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)
