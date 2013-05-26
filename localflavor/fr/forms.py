"""
FR-specific Form helpers
"""
from __future__ import absolute_import, unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

from .fr_department import DEPARTMENT_CHOICES_PER_REGION
from .fr_region import REGION_CHOICES


class FRZipCodeField(RegexField):
    """
    Validate local French zip code.
    The correct format is 'XXXX'.
    """
    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX.'),
    }

    def __init__(self, max_length=5, min_length=5, *args, **kwargs):
        kwargs['label'] = _('Zip code')
        kwargs['max_length'] = max_length
        kwargs['min_length'] = min_length
        super(FRZipCodeField, self).__init__(
            r'^\d{5}$', *args, **kwargs)


class FRPhoneNumberField(CharField):
    """
    Validate local French phone number (not international ones)
    The correct format is '0X XX XX XX XX'.
    '0X.XX.XX.XX.XX' and '0XXXXXXXXX' validate but are corrected to
    '0X XX XX XX XX'.
    """
    phone_digits_re = re.compile(r'^0\d(\s|\.)?(\d{2}(\s|\.)?){3}\d{2}$')

    default_error_messages = {
        'invalid': _('Phone numbers must be in 0X XX XX XX XX format.'),
    }

    def __init__(self, max_length=14, min_length=10, *args, **kwargs):
        kwargs['label'] = _('Phone number')
        kwargs['max_length'] = max_length
        kwargs['min_length'] = min_length
        super(FRPhoneNumberField, self).__init__(*args, **kwargs)

    def clean(self, value):
        value = super(FRPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\.|\s)', '', smart_text(value))
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


class FRDepartmentSelect(Select):
    """
    A Select widget that uses a list of FR departments as its choices.
    """
    def __init__(self, attrs=None):
        choices = [
            (dep[0], '%s - %s' % (dep[0], dep[1]))
            for dep in DEPARTMENT_CHOICES_PER_REGION
        ]
        super(FRDepartmentSelect, self).__init__(
            attrs,
            choices=choices
        )


class FRRegionSelect(Select):
    """
    A Select widget that uses a list of FR Regions as its choices.
    """
    def __init__(self, attrs=None):
        choices = [
            (dep[0], '%s - %s' % (dep[0], dep[1]))
            for dep in REGION_CHOICES
        ]
        super(FRRegionSelect, self).__init__(
            attrs,
            choices=choices
        )


class FRDepartmentField(CharField):
    """
    A Select Field that uses a FRDepartmentSelect widget.
    """
    widget = FRDepartmentSelect

    def __init__(self, *args, **kwargs):
        kwargs['label'] = _('Select Department')
        super(FRDepartmentField, self).__init__(*args, **kwargs)


class FRRegionField(CharField):
    """
    A Select Field that uses a FRRegionSelect widget.
    """
    widget = FRRegionSelect

    def __init__(self, *args, **kwargs):
        kwargs['label'] = _('Select Region')
        super(FRRegionField, self).__init__(*args, **kwargs)
