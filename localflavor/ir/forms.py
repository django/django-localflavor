# -*- coding: utf-8 -*-
"""AR-specific Form helpers."""

from __future__ import unicode_literals

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.translation import ugettext_lazy as _

from .ir_provinces import PROVINCE_CHOICES




class IRProvinceSelect(Select):
    """A Select widget that uses a list of Iranian provinces/autonomous cities as its choices."""

    def __init__(self, attrs=None):
        super(IRProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)




class IRPostlCodeField(RegexField):
    """
      A field that accepts a 'classic' XXXXXXXXXX Postal Code o.

      See:
          https://en.wikipedia.org/wiki/List_of_postal_codes
      """

    default_error_messages = {
        'invlid': _("Enter a postal code in the format xxxxxxxxxx")
    }

    def __init__(self, max_length=10, min_length=11, *args, **kwargs):
        super(IRPostlCodeField,self).__init__(r'^\d{4}$|^[A-HJ-NP-Za-hj-np-z]\d{4}\D{3}$',
        max_length,
        min_length,
        *args,
        **kwargs
      )

    def clean(self, value):
        value = super(IRPostlCodeField,self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        if len(value) != 10 :
            raise ValidationError(self.error_messages['invalid'])
        if len(value) == 10:
            return '%s%s%s' % (value[0].upper(), value[1:5], value[5:].upper())
        return value

