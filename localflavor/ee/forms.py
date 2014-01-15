from __future__ import absolute_import, unicode_literals

import re
from datetime import date

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select
from django.utils.translation import ugettext_lazy as _

from .ee_counties import COUNTY_CHOICES


idcode = re.compile(r'^([1-6])(\d\d)(\d\d)(\d\d)(?:\d{3})(\d)$')
zipcode = re.compile(r'^[1-9]\d{4}$')


class EEZipCodeField(RegexField):
    """
    A form field that validates input as a Estonian zip code. Valid codes
    consist of five digits; first digit cannot be 0.
    """
    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(EEZipCodeField, self).__init__(zipcode, max_length, min_length, *args, **kwargs)


class EECountySelect(Select):
    """
    A Select widget that uses a list of Estonian counties as its choices.
    """
    def __init__(self, attrs=None):
        super(EECountySelect, self).__init__(attrs, choices=COUNTY_CHOICES)


class EEPersonalIdentificationCode(Field):
    """A form field that validates input as a Estonian personal identification code.

    See: https://www.riigiteataja.ee/akt/106032012004
    """
    default_error_messages = {
        'invalid_format': _('Enter an 11-digit Estonian personal identification code.'),
        'invalid': _('Enter a valid Estonian personal identification code.'),
    }

    @staticmethod
    def ee_checksum(value):
        """Takes a string of 10 digits as input, returns check digit."""

        for i in (1, 3):
            check = 0
            for c in value:
                check += i * int(c)
                i = (i % 9) + 1
            check %= 11
            if check < 10:
                return check
            # If check==10 then we do another loop starting at i=3

        return check % 10

    def clean(self, value):
        super(EEPersonalIdentificationCode, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        match = re.match(idcode, value)
        if not match:
            raise ValidationError(self.error_messages['invalid_format'])

        century, year, month, day, check = map(int, match.groups())

        if check != self.ee_checksum(value[:10]):
            raise ValidationError(self.error_messages['invalid'])

        # Century digit also encodes gender:
        # 1 - male born in 18xx
        # 2 - female born in 18xx
        # 3 - male born in 19xx
        # ...
        year += 1800 + 100 * ((century - 1) // 2)
        try:
            date(year, month, day)
        except ValueError:
            raise ValidationError(self.error_messages['invalid'])

        return value
