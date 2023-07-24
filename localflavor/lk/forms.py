"""Sri Lanka specific Form helpers."""

from django.forms.fields import RegexField, Select
from django.utils.translation import gettext_lazy as _

from .lk_provinces import PROVINCES
from .lk_districts import DISTRICTS


class LKPostalCodeFormField(RegexField):
    """
        A form field that accepts Sri Lanka postal code.
        Format : XXXXX

        Postal codes: https://en.wikipedia.org/wiki/Postal_codes_in_Sri_Lanka
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in format XXXXX'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^\d{5}$', **kwargs)


class LKProvinceSelect(Select):
    """
    A Select widget with option to select a provinces from
    list of all provinces of Sri Lanka.
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=PROVINCES)


class LKDistrictsSelect(Select):
    """
    A Select widget with option to select a districts from
    list of all districts of Sri Lanka.
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=DISTRICTS)
