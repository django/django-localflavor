# -*- coding: utf-8 -*-
"""AR-specific Form helpers."""

from __future__ import unicode_literals

from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.translation import ugettext_lazy as _

from localflavor.compat import EmptyValueCompatMixin

from .ir_provinces import PROVINCE_CHOICES

class ARProvinceSelect(Select):
    """A Select widget that uses a list of Iran provinces cities as its choices."""

    def __init__(self, attrs=None):
        super(ARProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)

class IRPostalCodeField(EmptyValueCompatMixin, RegexField):
    """
    A field that accepts a 'classic' NNNNNNNNNN Postal Code.

    See:
        https://en.youbianku.com/iran
    """

    default_error_messages = {
        'invalid': _("Enter a postal code in the format NNNNNNNNNN."),
    }

    def __init__(self,*args, **kwargs):
        super(ARPostalCodeField, self).__init__(r'^d{10}$',*args, **kwargs)

    def clean(self, value):
        value = super(IRPostalCodeField, self).clean(value)
        if value in self.empty_values:
            return self.empty_value
        if len(value) != 10:
            raise ValidationError(self.error_messages['invalid'])
        return value
