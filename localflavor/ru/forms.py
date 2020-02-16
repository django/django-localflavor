"""Russian-specific forms helpers."""
from django.forms.fields import RegexField, Select
from django.utils.translation import gettext_lazy as _

from .ru_regions import RU_COUNTY_CHOICES, RU_REGIONS_CHOICES


class RUCountySelect(Select):
    """A Select widget that uses a list of Russian Counties as its choices."""

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=RU_COUNTY_CHOICES)


class RURegionSelect(Select):
    """A Select widget that uses a list of Russian Regions as its choices."""

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=RU_REGIONS_CHOICES)


class RUPostalCodeField(RegexField):
    """
    Russian Postal code field.

    Format: XXXXXX, where X is any digit, and first digit is not zero.
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in the format XXXXXX.'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^\d{6}$', **kwargs)


class RUPassportNumberField(RegexField):
    """
    Russian internal passport number format.

    XXXX XXXXXX where X - any digit.
    """

    default_error_messages = {
        'invalid': _('Enter a passport number in the format XXXX XXXXXX.'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^\d{4} \d{6}$', **kwargs)


class RUAlienPassportNumberField(RegexField):
    """
    Russian alien's passport number format.

    XX XXXXXXX where X - any digit.
    """

    default_error_messages = {
        'invalid': _('Enter a passport number in the format XX XXXXXXX.'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^\d{2} \d{7}$', **kwargs)
