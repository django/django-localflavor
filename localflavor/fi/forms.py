"""FI-specific Form helpers."""

from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select
from django.utils.translation import ugettext_lazy as _

from .fi_municipalities import MUNICIPALITY_CHOICES


class FIZipCodeField(RegexField):
    """
    A form field that validates input as a Finnish zip code.

    Valid codes consist of five digits.
    """

    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX.'),
    }

    def __init__(self, *args, **kwargs):
        super(FIZipCodeField, self).__init__(r'^\d{5}$', *args, **kwargs)


class FIMunicipalitySelect(Select):
    """A Select widget that uses a list of Finnish municipalities as its choices."""

    def __init__(self, attrs=None):
        super(FIMunicipalitySelect, self).__init__(attrs, choices=MUNICIPALITY_CHOICES)


class FISocialSecurityNumber(Field):
    """A form field that validates input as a Finnish social security number."""

    default_error_messages = {
        'invalid': _('Enter a valid Finnish social security number.'),
    }

    def clean(self, value):
        super(FISocialSecurityNumber, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        checkmarks = "0123456789ABCDEFHJKLMNPRSTUVWXY"
        result = re.match(r"""^
            (?P<date>([0-2]\d|3[01])
            (0\d|1[012])
            (\d{2}))
            [A+-]
            (?P<serial>(\d{3}))
            (?P<checksum>[%s])$""" % checkmarks, value, re.VERBOSE | re.IGNORECASE)
        if not result:
            raise ValidationError(self.error_messages['invalid'])
        gd = result.groupdict()
        checksum = int(gd['date'] + gd['serial'])
        if checkmarks[checksum % len(checkmarks)] == gd['checksum'].upper():
            return '%s' % value.upper()
        raise ValidationError(self.error_messages['invalid'])
