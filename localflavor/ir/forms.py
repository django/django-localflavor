# -*- coding: utf-8 -*-
"""IR-specific Form helpers."""

from __future__ import unicode_literals
import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField,Select
from django.utils.encoding import force_text

from localflavor.generic.forms import DeprecatedPhoneNumberFormFieldMixin
from .ir_provinces import PROVINCE_CHOICES

PHONE_DIGITS_RE = re.compile(r'^(\d{10})$')






class IRProvinceSelect(Select):
    """A Select widget that uses a list of Iranian provinces/autonomous cities as its choices."""

    def __init__(self, attrs=None):
        super(IRProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)




class IRhoneNumberField(CharField, DeprecatedPhoneNumberFormFieldMixin):
    """
    A form field that validates input as an Iranian phone number.

    Valid numbers have ten digits.
    """

    default_error_messages = {
        'invalid': 'Phone numbers must contain 10 digits.',
    }

    def clean(self, value):
        """Validate a phone number. Strips parentheses, whitespace and hyphens."""
        super(IRhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\(|\)|\s+|-)', '', force_text(value))
        phone_match = PHONE_DIGITS_RE.search(value)
        if phone_match:
            return '%s' % phone_match.group(1)
        raise ValidationError(self.error_messages['invalid'])
