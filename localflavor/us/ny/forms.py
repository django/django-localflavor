"""
New York State Form helpers
"""

from __future__ import absolute_import, unicode_literals

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select, CharField
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

class NYSCountySelect(Select):
    """
    A Select widget that uses a list of U.S. states/territories as its choices.
    """
    def __init__(self, attrs=None):
        from .nys_detail import NYS_COUNTY_CHOICES
        super(NYSCountySelect, self).__init__(attrs, choices=NYS_COUNTY_CHOICES)
