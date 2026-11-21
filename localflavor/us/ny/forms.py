"""
New York State Form helpers
"""

from __future__ import absolute_import, unicode_literals

from django.forms.fields import Select


class NYSCountySelect(Select):
    """
    A Select widget that uses a list of U.S. states/territories as its choices.
    """
    def __init__(self, attrs=None):
        from .nys_detail import NYS_COUNTY_CHOICES
        super(NYSCountySelect, self).__init__(attrs, choices=NYS_COUNTY_CHOICES)
