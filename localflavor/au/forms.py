"""Australian-specific Form helpers."""

from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.forms import DeprecatedPhoneNumberFormFieldMixin

from .au_states import STATE_CHOICES
from .validators import AUBusinessNumberFieldValidator, AUCompanyNumberFieldValidator, AUTaxFileNumberFieldValidator

PHONE_DIGITS_RE = re.compile(r'^(\d{10})$')


class AUPostCodeField(RegexField):
    """
    Australian post code field.

    Assumed to be 4 digits.
    Northern Territory 3-digit postcodes should have leading zero.
    """

    default_error_messages = {
        'invalid': _('Enter a 4 digit postcode.'),
    }

    def __init__(self, max_length=4, min_length=None, *args, **kwargs):
        super(AUPostCodeField, self).__init__(r'^\d{4}$',
                                              max_length, min_length, *args, **kwargs)


class AUPhoneNumberField(CharField, DeprecatedPhoneNumberFormFieldMixin):
    """
    A form field that validates input as an Australian phone number.

    Valid numbers have ten digits.
    """

    default_error_messages = {
        'invalid': 'Phone numbers must contain 10 digits.',
    }

    def clean(self, value):
        """Validate a phone number. Strips parentheses, whitespace and hyphens."""
        super(AUPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\(|\)|\s+|-)', '', force_text(value))
        phone_match = PHONE_DIGITS_RE.search(value)
        if phone_match:
            return '%s' % phone_match.group(1)
        raise ValidationError(self.error_messages['invalid'])


class AUStateSelect(Select):
    """A Select widget that uses a list of Australian states/territories as its choices."""

    def __init__(self, attrs=None):
        super(AUStateSelect, self).__init__(attrs, choices=STATE_CHOICES)


class AUBusinessNumberField(CharField):
    """
    A form field that validates input as an Australian Business Number (ABN).

    .. versionadded:: 1.3
    .. versionchanged:: 1.4
    """

    default_validators = [AUBusinessNumberFieldValidator()]

    def to_python(self, value):
        value = super(AUBusinessNumberField, self).to_python(value)
        return value.upper().replace(' ', '')

    def prepare_value(self, value):
        """Format the value for display."""
        if value is None:
            return value

        spaceless = ''.join(value.split())
        return '{} {} {} {}'.format(spaceless[:2], spaceless[2:5], spaceless[5:8], spaceless[8:])


class AUCompanyNumberField(CharField):
    """
    A form field that validates input as an Australian Company Number (ACN).

    .. versionadded:: 1.5
    """

    default_validators = [AUCompanyNumberFieldValidator()]

    def to_python(self, value):
        value = super(AUCompanyNumberField, self).to_python(value)
        return value.upper().replace(' ', '')

    def prepare_value(self, value):
        """Format the value for display."""
        if value is None:
            return value

        spaceless = ''.join(value.split())
        return '{} {} {}'.format(spaceless[:3], spaceless[3:6], spaceless[6:])


class AUTaxFileNumberField(CharField):
    """
    A form field that validates input as an Australian Tax File Number (TFN).

    .. versionadded:: 1.4
    """

    default_validators = [AUTaxFileNumberFieldValidator()]

    def prepare_value(self, value):
        """Format the value for display."""
        if value is None:
            return value

        spaceless = ''.join(value.split())
        return '{} {} {}'.format(spaceless[:3], spaceless[3:6], spaceless[6:])
