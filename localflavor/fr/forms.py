# -*- coding: utf-8 -*-
"""FR-specific Form helpers"""
from __future__ import unicode_literals

import re
from datetime import date

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.checksums import luhn
from localflavor.generic.forms import DeprecatedPhoneNumberFormFieldMixin

from .fr_department import DEPARTMENT_CHOICES_PER_REGION
from .fr_region import REGION_2016_CHOICES, REGION_CHOICES

nin_re = re.compile(
    r'^(?P<gender>[1278])(?P<year_of_birth>\d{2})(?P<month_of_birth>0[1-9]|1[0-2]|20|3[0-9]|4[0-2]|[5-9][0-9])'
    r'(?P<department_of_origin>\d{2}|2[AB])(?P<commune_of_origin>\d{3})(?P<person_unique_number>\d{3})'
    r'(?P<control_key>\d{2})$')


class FRZipCodeField(RegexField):
    """
    Validate local French zip code.

    The correct format is 'XXXXX'.
    """

    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX.'),
    }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label', _('Zip code'))
        kwargs['max_length'] = 5
        kwargs['min_length'] = 5
        super(FRZipCodeField, self).__init__(r'^\d{5}$', *args, **kwargs)


class FRPhoneNumberField(CharField, DeprecatedPhoneNumberFormFieldMixin):
    """
    Validate local French phone number (not international ones).

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
        super(FRPhoneNumberField, self).__init__(*args, **kwargs)

    def clean(self, value):
        value = super(FRPhoneNumberField, self).clean(value)
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


class FRDepartmentSelect(Select):
    """A Select widget that uses a list of FR departments as its choices."""

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
    """A Select widget that uses a list of FR Regions as its choices."""

    def __init__(self, attrs=None):
        choices = [
            (dep[0], '%s - %s' % (dep[0], dep[1]))
            for dep in REGION_CHOICES
        ]
        super(FRRegionSelect, self).__init__(
            attrs,
            choices=choices
        )


class FRRegion2016Select(Select):
    """
    A Select widget that uses a list of France's New Regions as its choices.
    """
    def __init__(self, attrs=None):
        choices = [
            (reg[0], '%s - %s' % (reg[0], reg[1]))
            for reg in REGION_2016_CHOICES
        ]
        super(FRRegion2016Select, self).__init__(attrs, choices=choices)


class FRDepartmentField(CharField):
    """A Select Field that uses a FRDepartmentSelect widget."""

    widget = FRDepartmentSelect

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label', _('Select Department'))
        super(FRDepartmentField, self).__init__(*args, **kwargs)


class FRRegionField(CharField):
    """A Select Field that uses a FRRegionSelect widget."""

    widget = FRRegionSelect

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label', _('Select Region'))
        super(FRRegionField, self).__init__(*args, **kwargs)


class FRNationalIdentificationNumber(CharField):
    """
    Validates input as a French National Identification number.

    Validation of the Number, and checksum calculation is detailed at http://en.wikipedia.org/wiki/INSEE_code

    .. versionadded:: 1.1
    """

    default_error_messages = {
        'invalid': _('Enter a valid French National Identification number.'),
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

        # Get current year
        current_year = int(str(date.today().year)[2:])

        commune_of_origin, department_of_origin = self._clean_department_and_commune(commune_of_origin, current_year,
                                                                                     department_of_origin,
                                                                                     year_of_birth)

        if person_unique_number == '000':
            raise ValidationError(self.error_messages['invalid'])

        if control_key > 97:
            raise ValidationError(self.error_messages['invalid'])

        control_number = int(gender + year_of_birth + month_of_birth +
                             department_of_origin.replace('A', '0').replace('B', '0') +
                             commune_of_origin + person_unique_number)
        if (97 - control_number % 97) == control_key:
            return value
        else:
            raise ValidationError(self.error_messages['invalid'])

    def _clean_department_and_commune(self, commune_of_origin, current_year, department_of_origin, year_of_birth):
        # Department number 98 is for Monaco
        if department_of_origin == '98':
            raise ValidationError(self.error_messages['invalid'])

        # Departments number 20, 2A and 2B represent Corsica
        if department_of_origin in ['20', '2A', '2B']:
            # For people born before 1976, Corsica number was 20
            if current_year < int(year_of_birth) < 76 and department_of_origin != '20':
                raise ValidationError(self.error_messages['invalid'])
            # For people born from 1976, Corsica dep number is either 2A or 2B
            if (int(year_of_birth) > 75 and department_of_origin not in ['2A', '2B']):
                raise ValidationError(self.error_messages['invalid'])

        # Overseas department numbers starts with 97 and are 3 digits long
        if department_of_origin == '97':
            department_of_origin += commune_of_origin[:1]
            if int(department_of_origin) not in range(971, 976):
                raise ValidationError(self.error_messages['invalid'])
            commune_of_origin = commune_of_origin[1:]
            if int(commune_of_origin) < 1 or int(commune_of_origin) > 90:
                raise ValidationError(self.error_messages['invalid'])
        elif int(commune_of_origin) < 1 or int(commune_of_origin) > 990:
            raise ValidationError(self.error_messages['invalid'])
        return commune_of_origin, department_of_origin


class FRSIRENENumberMixin(object):
    """Abstract class for SIREN and SIRET numbers, from the SIRENE register."""

    def clean(self, value):
        super(FRSIRENENumberMixin, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        value = value.replace(' ', '').replace('-', '')
        if not self.r_valid.match(value) or not luhn(value):
            raise ValidationError(self.error_messages['invalid'])
        return value


class FRSIRENField(FRSIRENENumberMixin, CharField):
    """
    SIREN stands for "Système d'identification du répertoire des entreprises".

    It's under authority of the INSEE.
    See http://fr.wikipedia.org/wiki/Système_d'identification_du_répertoire_des_entreprises for more information.

    .. versionadded:: 1.1
    """

    r_valid = re.compile(r'^\d{9}$')

    default_error_messages = {
        'invalid': _('Enter a valid French SIREN number.'),
    }

    def prepare_value(self, value):
        if value is None:
            return value
        value = value.replace(' ', '').replace('-', '')
        return ' '.join((value[:3], value[3:6], value[6:]))


class FRSIRETField(FRSIRENENumberMixin, CharField):
    """
    SIRET stands for "Système d'identification du répertoire des établissements".

    It's under authority of the INSEE.
    See http://fr.wikipedia.org/wiki/Système_d'identification_du_répertoire_des_établissements for more information.

    .. versionadded:: 1.1
    """

    r_valid = re.compile(r'^\d{14}$')

    default_error_messages = {
        'invalid': _('Enter a valid French SIRET number.'),
    }

    def clean(self, value):
        if value not in EMPTY_VALUES:
            value = value.replace(' ', '').replace('-', '')

        ret = super(FRSIRETField, self).clean(value)

        if not luhn(ret[:9]):
            raise ValidationError(self.error_messages['invalid'])
        return ret

    def prepare_value(self, value):
        if value is None:
            return value
        value = value.replace(' ', '').replace('-', '')
        return ' '.join((value[:3], value[3:6], value[6:9], value[9:]))
