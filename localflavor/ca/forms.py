"""Canada-specific Form helpers."""

from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Field, Select
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.checksums import luhn

sin_re = re.compile(r"^(\d{3})-(\d{3})-(\d{3})$")


class CAPostalCodeField(CharField):
    """
    Canadian postal code form field.

    Validates against known invalid characters: D, F, I, O, Q, U
    Additionally the first character cannot be Z or W.
    For more info see:
    http://www.canadapost.ca/tools/pg/manual/PGaddress-e.asp#1402170
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in the format XXX XXX.'),
    }

    postcode_regex = re.compile(
        r'^([ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ]) *(\d[ABCEGHJKLMNPRSTVWXYZ]\d)$')

    def clean(self, value):
        value = super(CAPostalCodeField, self).clean(value)
        if value in self.empty_values:
            return self.empty_value
        postcode = value.upper().strip()
        m = self.postcode_regex.match(postcode)
        if not m:
            raise ValidationError(self.error_messages['invalid'])
        return "%s %s" % (m.group(1), m.group(2))


class CAProvinceField(Field):
    """
    A form field that validates its input is a Canadian province name or abbreviation.

    It normalizes the input to the standard two-leter postal service
    abbreviation for the given province.
    """

    default_error_messages = {
        'invalid': _('Enter a Canadian province or territory.'),
    }

    def clean(self, value):
        super(CAProvinceField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        try:
            value = value.strip().lower()
        except AttributeError:
            pass
        else:
            # Load data in memory only when it is required, see also #17275
            from .ca_provinces import PROVINCES_NORMALIZED
            try:
                return PROVINCES_NORMALIZED[value.strip().lower()]
            except KeyError:
                pass
        raise ValidationError(self.error_messages['invalid'])


class CAProvinceSelect(Select):
    """A Select widget that uses a list of Canadian provinces and territories as its choices."""

    def __init__(self, attrs=None):
        # Load data in memory only when it is required, see also #17275
        from .ca_provinces import PROVINCE_CHOICES
        super(CAProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)


class CASocialInsuranceNumberField(Field):
    """
    A Canadian Social Insurance Number (SIN).

    Checks the following rules to determine whether the number is valid:

    * Conforms to the XXX-XXX-XXX format.

    * Passes the check digit process "Luhn Algorithm"
         See: http://en.wikipedia.org/wiki/Social_Insurance_Number

    """

    default_error_messages = {
        'invalid': _(
            'Enter a valid Canadian Social Insurance number in XXX-XXX-XXX format.'),
    }

    def clean(self, value):
        super(CASocialInsuranceNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        match = re.match(sin_re, value)
        if not match:
            raise ValidationError(self.error_messages['invalid'])

        number = '%s-%s-%s' % (match.group(1), match.group(2), match.group(3))
        check_number = '%s%s%s' % (
            match.group(1),
            match.group(2),
            match.group(3))
        if not luhn(check_number):
            raise ValidationError(self.error_messages['invalid'])
        return number
