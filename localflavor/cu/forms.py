from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.forms import CharField, RegexField, Select
from django.utils.translation import gettext_lazy as _

from .choices import PROVINCE_CHOICES, PROVINCE_NORMALIZED, REGION_CHOICES, REGION_NORMALIZED
from .validators import CUIdentityCardNumberBirthdayValidator


class CURegionField(CharField):
    """
    A form field for a Cuban region.
    The input is validated against a dictionary which includes names and abbreviations.

    It normalizes the input to the standard abbreviation for the given region.

    .. versionadded:: 1.6
    """

    default_error_messages = {
        'invalid': _('Enter a Cuban region.'),
    }

    def __init__(self, **kwargs):
        if "strip" in kwargs and kwargs["strip"] is False:
            raise ImproperlyConfigured("strip cannot be set to False")
        super().__init__(**kwargs)

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return value
        try:
            return REGION_NORMALIZED[value.lower()]
        except KeyError:
            pass
        raise ValidationError(self.error_messages['invalid'], code='invalid')


class CURegionSelect(Select):
    """
    A Select widget that uses a list of Cuban regions as its choices.

    .. versionadded:: 1.6
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=REGION_CHOICES)


class CUProvinceField(CharField):
    """
    A form field for a Cuban province.
    The input is validated against a dictionary which includes names and abbreviations.

    It normalizes the input to the standard abbreviation for the given province.

    .. versionadded:: 1.6
    """

    default_error_messages = {
        'invalid': _('Enter a Cuban province.'),
    }

    def __init__(self, **kwargs):
        if "strip" in kwargs and kwargs["strip"] is False:
            raise ImproperlyConfigured("strip cannot be set to False")
        super().__init__(**kwargs)

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return value
        try:
            return PROVINCE_NORMALIZED[value.lower()]
        except KeyError:
            pass
        raise ValidationError(self.error_messages['invalid'], code='invalid')


class CUProvinceSelect(Select):
    """
    A Select widget that uses a list of Cuban provinces as its choices.

    .. versionadded:: 1.6
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=PROVINCE_CHOICES)


class CUPostalCodeField(RegexField):
    """
    A form field for a Cuban postal Code.

    Taken from : http://mapanet.eu/Postal_Codes/?C=CU

    The Cuban postal code is a combination of 5 digits non begin with 0.

    .. versionadded:: 1.6
    """

    default_error_messages = {
        'invalid': _('Enter a valid postal code in the format XXXXX.'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^[1-9]\d{4}$', **kwargs)

    def to_python(self, value):
        value = super().to_python(value)
        if value in self.empty_values:
            return self.empty_value
        return value.strip()


class CUIdentityCardNumberField(RegexField):
    """
    A form field for a Cuban identity card number.

    Taken from : http://www.postdata.club/issues/201609/es-usted-unico-en-cuba.html

    The Cuban identity card number is generated by a mathematical algorithm following those rules:
    - Combination of 11 digits.
    - The first 6 digits represents the birthday of the owner.
        -> '%y%m%d' format, ex: `860619`
    - 7th digit represent the century.
        -> 9 for XIX
        -> 0-5 for XX
        -> 6, 7 and 8 for XXI
    - 8th, 9th and 11th aleatory.
    - 10th represent the sex of the owner. Male for the even numbers and Female for odd numbers.

    .. versionadded:: 1.6
    """

    default_error_messages = {
        'invalid': _('Enter a valid identity card number in the format XXXXXXXXXXX.'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^\d{11}$', **kwargs)
        self.validators.append(CUIdentityCardNumberBirthdayValidator())

    def to_python(self, value):
        value = super().to_python(value)
        if value in self.empty_values:
            return self.empty_value
        return value.strip()
