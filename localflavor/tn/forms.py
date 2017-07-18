# -*- coding: utf-8 -*-
"""Tunisia-specific Form helpers."""
from __future__ import unicode_literals

from django.forms.fields import Select

from .tn_governorates import GOVERNORATE_CHOICES


class TNGovernorateSelect(Select):
    """A Select widget that uses a list of the Tunisian governorates as its choices."""

    def __init__(self, attrs=None):
        super(TNGovernorateSelect, self).__init__(
            attrs, choices=GOVERNORATE_CHOICES
        )
