"""
Ukrainian-specific forms helpers
"""
from __future__ import absolute_import, unicode_literals
from .ua_regions import UA_REGIONS_CHOICES

from django.forms.fields import RegexField, Select
from django.utils.translation import ugettext_lazy as _


class UARegionSelect(Select):
    """
    A Select widget that uses a list of Ukrainian Regions as its choices.
    """
    def __init__(self, attrs=None):
        super(UARegionSelect, self).__init__(attrs, choices=UA_REGIONS_CHOICES)


class UAPostalCodeField(RegexField):
    """
    Ukraine Postal code field.
    Format: XXXXX, where X is any digit, first two digits can change from 01 to 99.
    More info: http://en.wikipedia.org/wiki/Postal_codes_in_Ukraine
    """
    default_error_messages = {
        'invalid': _('Enter a postal code in the format XXXXX.'),
    }

    def __init__(self, *args, **kwargs):
        pattern = r'^(?:(?:[1-9]\d)|(?:\d[1-9]))\d{3}$'
        super(UAPostalCodeField, self).__init__(pattern, *args, **kwargs)
