# -*- coding: utf-8 -*-

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


nin_re = re.compile(r'^(?P<gender>[1278])(?P<year_of_birth>\d{2})(?P<month_of_birth>0[1-9]|1[0-2]|20)' +
                    '(?P<department_of_origin>\d{2}|2[AB])(?P<commune_of_origin>\d{3})(?P<person_unique_number>\d{3})' +
                    '(?P<control_key>\d{2})$')


class FRZipCodeField(RegexField):
    """
    Validate local French zip code.
    The correct format is 'XXXXX'.
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


class FRNationalIdentificationNumber(CharField):
    """
    Validates input as a French National Identification number.
    Validation of the Number, and checksum calculation is detailed at http://en.wikipedia.org/wiki/INSEE_code

    .. versionadded:: 1.1
    """
    default_error_messages = {
        'invalid': _('Enter a valid French French National Identification number.'),
    }

    def clean(self, value):
        super(FRNationalIdentificationNumber, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        value = value.replace(' ', '').replace('-', '')

        match = nin_re.match(value)
        if not match:
            raise ValidationError(self.error_messages['invalid'])

        # Extract all parts of social number
        gender = match.group('gender')
        year_of_birth = match.group('year_of_birth')
        month_of_birth = match.group('month_of_birth')
        department_of_origin = match.group('department_of_origin')
        commune_of_origin = match.group('commune_of_origin')
        person_unique_number = match.group('person_unique_number')
        control_key = int(match.group('control_key'))

        #Department number 98 is for Monaco, 20 doesn't exist
        if department_of_origin in ['98', '20']:
            raise ValidationError(self.error_messages['invalid'])

        #Overseas department numbers starts with 97 and are 3 digits long
        if department_of_origin == '97':
            department_of_origin += commune_of_origin[:1]
            if int(department_of_origin) not in range(971, 976):
                raise ValidationError(self.error_messages['invalid'])
            commune_of_origin = commune_of_origin[1:]
            if int(commune_of_origin) < 1 or int(commune_of_origin) > 90:
                raise ValidationError(self.error_messages['invalid'])
        elif int(commune_of_origin) < 1 or int(commune_of_origin) > 990:
            raise ValidationError(self.error_messages['invalid'])

        if person_unique_number == '000':
            raise ValidationError(self.error_messages['invalid'])

        if control_key > 97:
            raise ValidationError(self.error_messages['invalid'])

        control_number = int(gender + year_of_birth + month_of_birth +
                             department_of_origin.replace('A', '0').replace('B', '0')
                             + commune_of_origin + person_unique_number)
        if (97 - control_number % 97) == control_key:
            return value
        else:
            raise ValidationError(self.error_messages['invalid'])
