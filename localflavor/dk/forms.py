"""
Denmark specific form helpers.
"""

from __future__ import absolute_import, unicode_literals

from django.forms.widgets import Select

from .dk_postalcodes import DK_POSTALCODES


class DKPostalCodeSelect(Select):
    """
    A Select widget that uses a list of Danish postal codes as its choices.
    """
    def __init__(self, attrs=None):
        super(DKPostalCodeSelect, self).__init__(attrs, choices=DK_POSTALCODES)
