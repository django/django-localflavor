from __future__ import unicode_literals

import re
from datetime import date

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select
from django.utils.translation import ugettext_lazy as _

from .lt_choices import COUNTY_CHOICES, MUNICIPALITY_CHOICES

postalcode = re.compile(r'^(LT\s?-\s?)?(?P<code>\d{5})$', re.IGNORECASE)


class LTCountySelect(Select):
    """A select field with the Lithuanian counties as choices"""

    def __init__(self, attrs=None):
        super(LTCountySelect, self).__init__(attrs, choices=COUNTY_CHOICES)


class LTMunicipalitySelect(Select):
    """A select field with the Lithuanian municipalities as choices"""

    def __init__(self, attrs=None):
        super(LTMunicipalitySelect, self).__init__(attrs,
                                                   choices=MUNICIPALITY_CHOICES)


class LTIDCodeField(RegexField):
    """
    A form field that validates as Lithuanian ID Code.

    Checks:
        * Made of exactly 11 decimal numbers.
        * Checksum is correct.
        * ID contains valid date.
    """

    default_error_messages = {
        'invalid': _('ID Code consists of exactly 11 decimal digits.'),
        'checksum': _('Wrong ID Code checksum.'),
        'date': _('ID Code contains invalid date.')
    }

    def __init__(self, *args, **kwargs):
        super(LTIDCodeField, self).__init__(r'^\d{11}$', *args, **kwargs)

    def clean(self, value):
        super(LTIDCodeField, self).clean(value)

        if value in self.empty_values:
            return self.empty_value

        if not self.valid_date(value):
            raise ValidationError(self.error_messages['date'])

        if not self.valid_checksum(value):
            raise ValidationError(self.error_messages['checksum'])
        return value

    def valid_checksum(self, value):
        first_sum = 0
        second_sum = 0

        for i in range(10):
            first_sum += int(value[i]) * (i % 9 + 1)
            second_sum += int(value[i]) * ((i + 2) % 9 + 1)

        k = first_sum % 11
        if k == 10:
            k = second_sum % 11
            k = 0 if k == 10 else k

        return True if k == int(value[-1]) else False

    def valid_date(self, value):
        """
        Check if date in ID code is valid.

        We won't check for dates in future as it would become too restrictive.
        """
        try:
            year = {'1': 1800, '2': 1800, '3': 1900, '4': 1900, '5': 2000,
                    '6': 2000}[value[0]] + int(value[1:3])
            date(year, int(value[3:5]), int(value[5:7]))
            return True
        except (ValueError, KeyError):
            return False


class LTPostalCodeField(Field):
    """
    A form field that validates and normalizes Lithanuan postal codes.

    Lithuanian postal codes in following forms accepted:
        * XXXXX
        * LT-XXXXX
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in the format XXXXX or LT-XXXXX.'),
    }

    def clean(self, value):
        value = super(LTPostalCodeField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        match = re.match(postalcode, value)
        if not match:
            raise ValidationError(self.error_messages['invalid'])

        return 'LT-' + match.group('code')
