"""India-specific Form helpers."""

from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Field, RegexField, Select
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.forms import DeprecatedPhoneNumberFormFieldMixin

from .in_states import STATE_CHOICES, STATES_NORMALIZED

phone_digits_re = re.compile(r"""
(
    (?P<std_code>                   # the std-code group
        ^0                          # all std-codes start with 0
        (
            (?P<twodigit>\d{2})   | # either two, three or four digits
            (?P<threedigit>\d{3}) | # following the 0
            (?P<fourdigit>\d{4})
        )
    )
    [-\s]                           # space or -
    (?P<phone_no>                   # the phone number group
        [1-6]                       # first digit of phone number
        (
            (?(twodigit)\d{7})   |  # 7 more phone digits for 3 digit stdcode
            (?(threedigit)\d{6}) |  # 6 more phone digits for 4 digit stdcode
            (?(fourdigit)\d{5})     # 5 more phone digits for 5 digit stdcode
        )
    )
)$""", re.VERBOSE)

aadhaar_re = re.compile(r"^(?P<part1>\d{4})[-\ ]?(?P<part2>\d{4})[-\ ]?(?P<part3>\d{4})$")


class INZipCodeField(RegexField):
    """A form field that validates input as an Indian zip code, with the format XXXXXXX."""

    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXXX or XXX XXX.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(INZipCodeField, self).__init__(r'^\d{3}\s?\d{3}$',
                                             max_length, min_length, *args, **kwargs)

    def clean(self, value):
        value = super(INZipCodeField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        # Convert to "NNNNNN" if "NNN NNN" given
        value = re.sub(r'^(\d{3})\s(\d{3})$', r'\1\2', value)
        return value


class INStateField(Field):
    """
    A form field that validates its input is a Indian state name or abbreviation.

    It normalizes the input to the standard two-letter vehicle
    registration abbreviation for the given state or union territory

    .. versionchanged:: 1.1

       Added Telangana to list of states. More details at
       https://en.wikipedia.org/wiki/Telangana#Bifurcation_of_Andhra_Pradesh

    """

    default_error_messages = {
        'invalid': _('Enter an Indian state or territory.'),
    }

    def clean(self, value):
        value = super(INStateField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        try:
            value = value.strip().lower()
        except AttributeError:
            pass
        else:
            try:
                return force_text(STATES_NORMALIZED[value.strip().lower()])
            except KeyError:
                pass
        raise ValidationError(self.error_messages['invalid'])


class INAadhaarNumberField(Field):
    """
    A form field for Aadhaar number issued by Unique Identification Authority of India (UIDAI).

    Checks the following rules to determine whether the number is valid:

        * Conforms to the XXXX XXXX XXXX format.
        * No group consists entirely of zeroes.

    Important information:

        * Aadhaar number is a proof of identity but not of citizenship.
        * Aadhaar number is issued to every resident of India including
          foreign citizens.
        * Aadhaar number is not mandatory.

    More information can be found at
    http://uidai.gov.in/what-is-aadhaar-number.html
    """

    default_error_messages = {
        'invalid': _('Enter a valid Aadhaar number in XXXX XXXX XXXX or '
                     'XXXX-XXXX-XXXX format.'),
    }

    def clean(self, value):
        value = super(INAadhaarNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        match = re.match(aadhaar_re, value)
        if not match:
            raise ValidationError(self.error_messages['invalid'])
        part1, part2, part3 = match.groupdict()['part1'], match.groupdict()['part2'], match.groupdict()['part3']

        # all the parts can't be zero
        if part1 == '0000' and part2 == '0000' and part3 == '0000':
            raise ValidationError(self.error_messages['invalid'])

        return '%s %s %s' % (part1, part2, part3)


class INStateSelect(Select):
    """
    A Select widget that uses a list of Indian states/territories as its choices.

    .. versionchanged:: 1.1

       Added Telangana to list of states. More details at
       https://en.wikipedia.org/wiki/Telangana#Bifurcation_of_Andhra_Pradesh

    """

    def __init__(self, attrs=None):
        super(INStateSelect, self).__init__(attrs, choices=STATE_CHOICES)


class INPhoneNumberField(CharField, DeprecatedPhoneNumberFormFieldMixin):
    """
    INPhoneNumberField validates that the data is a valid Indian phone number, including the STD code.

    It's normalised to 0XXX-XXXXXXX or 0XXX XXXXXXX
    format. The first string is the STD code which is a '0' followed by 2-4
    digits. The second string is 8 digits if the STD code is 3 digits, 7
    digits if the STD code is 4 digits and 6 digits if the STD code is 5
    digits. The second string will start with numbers between 1 and 6. The
    separator is either a space or a hyphen.
    """

    default_error_messages = {
        'invalid': _('Phone numbers must be in 02X-8X or 03X-7X or 04X-6X format.'),
    }

    def clean(self, value):
        value = super(INPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = force_text(value)
        m = phone_digits_re.match(value)
        if m:
            return '%s' % (value)
        raise ValidationError(self.error_messages['invalid'])
