# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.forms import Field, RegexField, Select
from django.utils.translation import ugettext as _

from localflavor.compat import EmptyValueCompatMixin

from .choices import PROVINCE_CHOICES, PROVINCE_NORMALIZED, REGION_CHOICES, REGION_NORMALIZED
from .validators import CUIdentityCardNumberBirthdayValidator


class CURegionField(Field):
    """
    A form field for a cuban region.
    The input is validated against a dictionary which includes names and abbreviations.

    It normalizes the input to the standard abbreviation for the given region.

    .. versionadded:: 1.6
    """

    default_error_messages = {
        'invalid': _('Enter a cuban region.'),
    }

    def clean(self, value):
        super(CURegionField, self).clean(value)
        if value in self.empty_values:
            return ''
        try:
            return REGION_NORMALIZED[value.strip().lower()]
        except KeyError:
            pass
        raise ValidationError(self.error_messages['invalid'])


class CURegionSelect(Select):
    """
    A Select widget that uses a list of cuban regions as its choices.

    .. versionadded:: 1.6
    """

    def __init__(self, attrs=None):
        super(CURegionSelect, self).__init__(attrs, choices=REGION_CHOICES)


class CUProvinceField(Field):
    """
    A form field for a cuban province.
    The input is validated against a dictionary which includes names and abbreviations.

    It normalizes the input to the standard abbreviation for the given province.

    .. versionadded:: 1.6
    """

    default_error_messages = {
        'invalid': _('Enter a cuban province.'),
    }

    def clean(self, value):
        super(CUProvinceField, self).clean(value)
        if value in self.empty_values:
            return ''
        try:
            return PROVINCE_NORMALIZED[value.strip().lower()]
        except KeyError:
            pass
        raise ValidationError(self.error_messages['invalid'])


class CUProvinceSelect(Select):
    """
    A Select widget that uses a list of cuban provinces as its choices.

    .. versionadded:: 1.6
    """

    def __init__(self, attrs=None):
        super(CUProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)


class CUPostalCodeField(EmptyValueCompatMixin, RegexField):
    """
    A form field for a cuban postal Code.

    Taken from : http://mapanet.eu/Postal_Codes/?C=CU

    The cuban postal code is a combination of 5 digits non begin with 0.

    .. versionadded:: 1.6
    """

    default_error_messages = {
        'invalid': _('Enter a valid postal code in the format XXXXX.'),
    }

    def __init__(self, *args, **kwargs):
        super(CUPostalCodeField, self).__init__(r'^[1-9]\d{4}$', *args, **kwargs)

    def to_python(self, value):
        value = super(CUPostalCodeField, self).to_python(value)
        if value in self.empty_values:
            return self.empty_value
        return value.strip()


class CUIdentityCardNumberField(EmptyValueCompatMixin, RegexField):
    """
    A form field for a cuban identity card number.

    Taken from : http://www.postdata.club/issues/201609/es-usted-unico-en-cuba.html

    The cuban identity card number is generated by a mathematical algorithm following those rules:
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

    def __init__(self, *args, **kwargs):
        super(CUIdentityCardNumberField, self).__init__(r'^\d{11}$', *args, **kwargs)
        self.validators.append(CUIdentityCardNumberBirthdayValidator())

    def to_python(self, value):
        value = super(CUIdentityCardNumberField, self).to_python(value)
        if value in self.empty_values:
            return self.empty_value
        return value.strip()
