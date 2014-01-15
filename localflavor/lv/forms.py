from __future__ import unicode_literals

from django.forms.fields import Select

from .lv_choices import MUNICIPALITY_CHOICES


class LVMunicipalitySelect(Select):
    """A select field of Latvian municipalities."""

    def __init__(self, attrs=None):
        super(LVMunicipalitySelect, self).__init__(attrs, choices=MUNICIPALITY_CHOICES)
