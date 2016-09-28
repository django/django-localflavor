# -*- coding: utf-8 -*-
"""
Ve-specific Form helpers.
"""

from django.forms.fields import Select

from .ve_region import REGION_CHOICES


class VERegionsSelect(Select):
    """
    A Select widget that uses a list of Venezuelan regions as its choices.
    """
    def __init__(self, attrs=None):
        super(VERegionsSelect, self).__init__(attrs, choices=REGION_CHOICES)
