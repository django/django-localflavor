"""Nepal specific form helpers."""

from django.forms.fields import RegexField
from django.utils.translation import gettext_lazy as _
from django.forms.fields import Select
from .np_zones import ZONES
from .np_provinces import PROVINCES
from .np_districts import ALL_DISTRICTS

class NPPostalCodeFormField(RegexField):
    """
        A form field that accepts Nepali postal code.
        Format : XXXXX

        Postal codes: https://en.wikipedia.org/wiki/List_of_postal_codes_in_Nepal
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

class NPZoneSelect(Select):
    """
    A Select widget with option to select a zone from 
    list of all zones of Nepal.
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=ZONES)

class NPProvinceSelect(Select):
    """
    A Select widget with option to select a province from 
    list of all provinces of Nepal.
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=PROVINCES)

class NPDistrictSelect(Select):
    """
    A Select widget with option to select a district from 
    list of all districts of Nepal.
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=ALL_DISTRICTS)
