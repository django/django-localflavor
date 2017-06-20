"""Pakistani-specific Form helpers."""

from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.forms import DeprecatedPhoneNumberFormFieldMixin

from .pk_states import STATE_CHOICES

POSTCODE_DIGITS_RE = re.compile(r'^(\d{5})$')
PHONE_DIGITS_RE = re.compile(r'^(\d{9,11})$')


class PKPostCodeField(RegexField):
    """
    Pakistani post code field.

    Assumed to be 5 digits.
    """

    default_error_messages = {
        'invalid': _('Enter a 5 digit postcode.'),
    }

    def __init__(self, *args, **kwargs):
        super(PKPostCodeField, self).__init__(POSTCODE_DIGITS_RE, *args, **kwargs)


class PKPhoneNumberField(CharField, DeprecatedPhoneNumberFormFieldMixin):
    """
    A form field that validates input as an Pakistani phone number.

    Valid numbers have nine to eleven digits.
    """

    default_error_messages = {
        'invalid': _('Phone numbers must contain 9, 10 or 11 digits.'),
    }

    def clean(self, value):
        """
        Validate a phone number.

        Strips parentheses, whitespace and hyphens.
        """
        super(PKPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\(|\)|\s+|-)', '', force_text(value))
        phone_match = PHONE_DIGITS_RE.search(value)
        if phone_match:
            return '%s' % phone_match.group(1)
        raise ValidationError(self.error_messages['invalid'])


class PKStateSelect(Select):
    """A Select widget that uses a list of Pakistani states/territories as its choices."""

    def __init__(self, attrs=None):
        super(PKStateSelect, self).__init__(attrs, choices=STATE_CHOICES)
