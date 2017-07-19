# -*- coding: utf-8 -*-
"""AR-specific Form helpers."""

from __future__ import unicode_literals

from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.translation import ugettext_lazy as _

from localflavor.compat import EmptyValueCompatMixin

from .ir_provinces import PROVINCE_CHOICES

class IRProvinceSelect(Select):
    """A Select widget that uses a list of Argentinean provinces/autonomous cities as its choices."""

    def __init__(self, attrs=None):
        super(IRProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)
