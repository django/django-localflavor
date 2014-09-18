"""
Singapore-specific Form helpers
"""

from __future__ import absolute_import, unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, RegexField
from django.utils.encoding import smart_text
# from django.utils.translation import ugettext_lazy as _


PHONE_DIGITS_RE = re.compile(r'^(6|8|9)(\d{7})$')


class SGPostCodeField(RegexField):
    """ Singapore post code field.

    Assumed to be 6 digits.
    """
    default_error_messages = {
        'invalid': 'Enter a 6-digit postal code.',
    }

    def __init__(self, max_length=6, min_length=None, *args, **kwargs):
        super(SGPostCodeField, self).__init__(r'^\d{6}$',
                                              max_length, min_length,
                                              *args, **kwargs)


class SGPhoneNumberField(CharField):
    """
    A form field that validates input as a Singapore phone number.

    Valid numbers have 8 digits and start with either 6, 8, or 9
    """
    default_error_messages = {
        'invalid': ('Phone numbers must contain 8 digits and start with '
                    'either 6, or 8, or 9.')

    }

    def clean(self, value):
        """
        Validate a phone number. Strips parentheses, whitespace and hyphens.
        """
        super(SGPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\(|\)|\s+|-)', '', smart_text(value))
        phone_match = PHONE_DIGITS_RE.search(value)
        if phone_match:
            return '%s' % phone_match.group()
        raise ValidationError(self.error_messages['invalid'])
