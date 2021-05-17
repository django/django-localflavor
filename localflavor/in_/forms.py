"""India-specific Form helpers."""

import re
import warnings

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from .in_states import STATE_CHOICES, STATES_NORMALIZED

aadhaar_re = re.compile(r"^(?P<part1>\d{4})[-\ ]?(?P<part2>\d{4})[-\ ]?(?P<part3>\d{4})$")


class INZipCodeField(RegexField):
    """A form field that validates input as an Indian zip code, with the format XXXXXXX."""

    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXXX or XXX XXX.'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^\d{3}\s?\d{3}$', **kwargs)

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return self.empty_value
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
        value = super().clean(value)
        if value in EMPTY_VALUES:
            return ''
        try:
            value = value.strip().lower()
        except AttributeError:
            pass
        else:
            try:
                return force_str(STATES_NORMALIZED[value.strip().lower()])
            except KeyError:
                pass
        raise ValidationError(self.error_messages['invalid'], code='invalid')


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
        value = super().clean(value)
        if value in EMPTY_VALUES:
            return ''

        match = re.match(aadhaar_re, value)
        if not match:
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        part1, part2, part3 = match.groupdict()['part1'], match.groupdict()['part2'], match.groupdict()['part3']

        # all the parts can't be zero
        if part1 == '0000' and part2 == '0000' and part3 == '0000':
            raise ValidationError(self.error_messages['invalid'], code='invalid')

        return '%s %s %s' % (part1, part2, part3)


class INStateSelect(Select):
    """
    A Select widget that uses a list of Indian states/territories as its choices.

    .. versionchanged:: 1.1

       Added Telangana to list of states. More details at
       https://en.wikipedia.org/wiki/Telangana#Bifurcation_of_Andhra_Pradesh

    .. versionchanged:: 3.1

       Updated Indian states and union territories names and code as per iso 3166
       (https://www.iso.org/obp/ui/#iso:code:3166:IN)
    """

    def __init__(self, attrs=None):
        warnings.warn("Choices have changed for INStateSelect in localflavor 3.1. See changelog for details.")
        super().__init__(attrs, choices=STATE_CHOICES)
