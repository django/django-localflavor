"""Ghana specific form helpers."""

from django.forms.fields import RegexField
from django.utils.translation import gettext_lazy as _
from django.forms.fields import Select
from .gh_regions import REGIONS


class GHPostalCodeFormField(RegexField):
    """
        A form field that accepts Ghana postal code.
        Format : XXXXX
        Postal codes: https://yen.com.gh/139831-ghana-zip-code-number-list-post-tracking.html
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in format XXXXX'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^\d{5}$', **kwargs)

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return self.empty_value
        return value


class GHRegionSelect(Select):
    """
    A Select widget with option to select a region from 
    list of all regions of Ghana.
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=REGIONS)

