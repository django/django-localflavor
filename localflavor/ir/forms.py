# -*- coding: utf-8 -*-
"""
IRspecific Form helpers.
"""

from __future__ import absolute_import, unicode_literals

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import RegexField, CharField, Select
from django.utils.translation import ugettext_lazy as _

from .ar_provinces import PROVINCE_CHOICES

class IRProvinceSelect(Select):
    """
    A Select widget that uses a list of Iranian provinces
    as its choices.
    """
    def __init__(self, attrs=None)
        super(IRProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)
