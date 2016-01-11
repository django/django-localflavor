"""
Australian-specific Form helpers
"""

from __future__ import absolute_import, unicode_literals

import re

from django.forms.fields import RegexField, Select
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.forms import PhoneNumberField

from .au_states import STATE_CHOICES

PHONE_DIGITS_RE = re.compile(r'^(\d{10})$')


class AUPostCodeField(RegexField):
    """ Australian post code field.

    Assumed to be 4 digits.
    Northern Territory 3-digit postcodes should have leading zero.
    """
    default_error_messages = {
        'invalid': _('Enter a 4 digit postcode.'),
    }

    def __init__(self, max_length=4, min_length=None, *args, **kwargs):
        super(AUPostCodeField, self).__init__(r'^\d{4}$',
                                              max_length, min_length, *args, **kwargs)


class AUPhoneNumberField(PhoneNumberField):
    """
    A form field that validates input as an Australian phone number.

    Valid numbers have ten digits.
    """
    region = 'AU'

    default_error_messages = {
        'invalid': 'Phone numbers must contain 10 digits.',
    }


class AUStateSelect(Select):
    """
    A Select widget that uses a list of Australian states/territories as its
    choices.
    """
    def __init__(self, attrs=None):
        super(AUStateSelect, self).__init__(attrs, choices=STATE_CHOICES)
