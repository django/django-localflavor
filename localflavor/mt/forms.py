# -*- coding: utf-8 -*-
"""Maltese-specific Form helpers."""
from __future__ import unicode_literals

from django.forms.fields import RegexField
from django.utils.translation import ugettext_lazy as _


class MTPostalCodeField(RegexField):
    """
    A form field that validates its input as a Maltese postal code.

    Maltese postal code is a seven digits string, with first three
    being letters and the final four numbers.
    """

    default_error_messages = {
        'invalid': _('Enter a valid postal code in format AAA 0000.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(MTPostalCodeField, self).__init__(
            r'^[A-Z]{3}\ \d{4}$',
            max_length, min_length, *args, **kwargs)
