"""
Kazakh-specific forms helpers
"""
from __future__ import absolute_import, unicode_literals

import datetime
import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField
from django.utils.translation import ugettext_lazy as _


class KZZipCodeField(RegexField):
    """
    Kazakhstani Zip Code. Valid format is XXXXXX where X is any digit.
    Strips whitespaces around value.
    """
    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(KZZipCodeField, self).__init__(r'^\d{6}$',
                                             max_length, min_length, *args, **kwargs)

    def to_python(self, value):
        value = super(KZZipCodeField, self).to_python(value)
        return value.strip()


class KZIndividualIDField(Field):
    """
    Kazakhstani Individual ID number are 12 digits.

    Format XXXXXXXXXXXX, where
        * XX - birth year
        * XX - birth month
        * XX - birth day
        * XXXXXX - any digit
    """
    default_error_messages = {
        'invalid': _('Enter a valid Kazakhstani Individual ID number'),
    }

    def clean(self, value):
        """
        Validates the input and returns a string that contains only numbers.
        Returns empty string for empty values.
        """
        super(KZIndividualIDField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        if not re.match(r'^\d{12}$', value):
            raise ValidationError(self.error_messages['invalid'])

        birthdate = value[:6]  # first 6 digits indicate birthdate
        try:
            datetime.datetime.strptime(birthdate, '%y%m%d')
        except ValueError:
            raise ValidationError(self.error_messages['invalid'])

        return value


class KZCivilPassportNumberField(RegexField):
    """
    Kazakhstani Civil Passport ID Field.
    Format is NXXXXXXXX, where X is any digit.
    Strips whitespaces around value.
    """
    default_error_messages = {
        'invalid': _('Enter valid Kazakhstani Passport number. Format NXXXXXXXX'),
    }

    def to_python(self, value):
        value = super(KZCivilPassportNumberField, self).to_python(value)
        return value.upper().strip()

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(KZCivilPassportNumberField, self).__init__(
            r'^N\d{8}$', max_length, min_length, *args, **kwargs)
