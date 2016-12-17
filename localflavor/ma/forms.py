# -*- coding: utf-8 -*-
"""MA-specific Form helpers"""
from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from .ma_provinces import PROVINCE_CHOICES_PER_REGION
from .ma_regions import REGION_CHOICES


class MAZipCodeField(RegexField):
    """
    Validate local Moroccan zip code.

    The correct format is 'XXXXX' as defined in http://codepostal.ma/code_postal.aspx .
    """

    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX.'),
    }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label', _('Zip code'))
        kwargs['max_length'] = 5
        kwargs['min_length'] = 5
        super(MAZipCodeField, self).__init__(r'^\d{5}$', *args, **kwargs)


class MAPhoneNumberField(CharField):
    """
    Validate local Moroccan phone number (not international ones).

    The correct format is '0X XX XX XX XX'.
    '0X.XX.XX.XX.XX' and '0XXXXXXXXX' validate but are corrected to
    '0X XX XX XX XX'.
    """

    phone_digits_re = re.compile(r'^0\d(\s|\.)?(\d{2}(\s|\.)?){3}\d{2}$')

    default_error_messages = {
        'invalid': _('Phone numbers must be in 0X XX XX XX XX format.'),
    }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label', _('Phone number'))
        kwargs['max_length'] = 14
        kwargs['min_length'] = 10
        super(MAPhoneNumberField, self).__init__(*args, **kwargs)

    def clean(self, value):
        value = super(MAPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\.|\s)', '', force_text(value))
        m = self.phone_digits_re.search(value)
        if m:
            return '%s %s %s %s %s' % (
                value[0:2],
                value[2:4],
                value[4:6],
                value[6:8],
                value[8:10]
            )
        raise ValidationError(self.error_messages['invalid'])


class MAProvinceSelect(Select):
    """A Select widget that uses a list of MA provinces as its choices."""

    def __init__(self, attrs=None):
        choices = [
            (province[0], '%s - %s' % (province[0], province[1]))
            for province in PROVINCE_CHOICES_PER_REGION
        ]
        super(MAProvinceSelect, self).__init__(
            attrs,
            choices=choices
        )


class MARegionSelect(Select):
    """A Select widget that uses a list of MA regions as its choices."""

    def __init__(self, attrs=None):
        choices = [
            (region[0], '%s - %s' % (region[0], region[1]))
            for region in REGION_CHOICES
        ]
        super(MARegionSelect, self).__init__(
            attrs,
            choices=choices
        )


class MAProvinceField(CharField):
    """A Select Field that uses a MAProvinceSelect widget."""

    widget = MAProvinceSelect

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label', _('Select Province'))
        super(MAProvinceField, self).__init__(*args, **kwargs)


class MARegionField(CharField):
    """A Select Field that uses a MARegionSelect widget."""

    widget = MARegionSelect

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label', _('Select Region'))
        super(MARegionField, self).__init__(*args, **kwargs)
