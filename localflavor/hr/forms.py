# -*- coding: utf-8 -*-
"""HR-specific Form helpers."""
from __future__ import unicode_literals

import datetime
import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.checksums import luhn

from .hr_choices import HR_COUNTY_CHOICES, HR_LICENSE_PLATE_PREFIX_CHOICES

jmbg_re = re.compile(r'^(?P<dd>\d{2})(?P<mm>\d{2})(?P<yyy>\d{3})' +
                     r'(?P<rr>\d{2})(?P<bbb>\d{3})(?P<k>\d{1})$')
oib_re = re.compile(r'^\d{11}$')
plate_re = re.compile(r'^(?P<prefix>[A-ZČŠŽ]{2})' +
                      r'(?P<number>\d{3,4})' +
                      r'(?P<suffix>[ABCDEFGHIJKLMNOPRSTUVZ]{1,2})$')
postal_code_re = re.compile(r'^\d{5}$')
jmbag_re = re.compile(r'^601983(?P<copy>\d{1})1(?P<jmbag>\d{10})(?P<k>\d{1})$')


class HRCountySelect(Select):
    """A Select widget that uses a list of counties of Croatia as its choices."""

    def __init__(self, attrs=None):
        super(HRCountySelect, self).__init__(attrs, choices=HR_COUNTY_CHOICES)


class HRLicensePlatePrefixSelect(Select):
    """A Select widget that uses a list of vehicle license plate prefixes of Croatia as its choices."""

    def __init__(self, attrs=None):
        super(HRLicensePlatePrefixSelect, self).__init__(attrs,
                                                         choices=HR_LICENSE_PLATE_PREFIX_CHOICES)


class HRJMBGField(Field):
    """
    Unique Master Citizen Number (JMBG) field.

    The number is still in use in Croatia, but it is being replaced by OIB.

    Source: http://en.wikipedia.org/wiki/Unique_Master_Citizen_Number

    For who might be reimplementing:
    The "area" regular expression group is used to calculate the region where a
    person was registered. Additional validation can be implemented in
    accordance with it, however this could result in exclusion of legit
    immigrated citizens. Therefore, this field works for any ex-Yugoslavia
    country.
    """

    default_error_messages = {
        'invalid': _('Enter a valid 13 digit JMBG'),
        'date': _('Error in date segment'),
    }

    def clean(self, value):
        super(HRJMBGField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        value = value.strip()

        matches = jmbg_re.search(value)
        if matches is None:
            raise ValidationError(self.error_messages['invalid'])

        # Make sure the date part is correct.
        dd = int(matches.group('dd'))
        mm = int(matches.group('mm'))
        yyy = int(matches.group('yyy'))
        try:
            datetime.date(yyy, mm, dd)
        except ValueError:
            raise ValidationError(self.error_messages['date'])

        # Validate checksum.
        k = matches.group('k')
        checksum = 0
        for i, j in zip(range(7, 1, -1), range(6)):
            checksum += i * (int(value[j]) + int(value[13 - i]))
        m = 11 - checksum % 11
        if m == 10:
            raise ValidationError(self.error_messages['invalid'])
        if m == 11 and k != '0':
            raise ValidationError(self.error_messages['invalid'])
        if not str(m) == k:
            raise ValidationError(self.error_messages['invalid'])

        return '%s' % (value, )


class HROIBField(RegexField):
    """
    Personal Identification Number of Croatia (OIB) field.

    http://www.oib.hr/
    """

    default_error_messages = {
        'invalid': _('Enter a valid 11 digit OIB'),
    }

    def __init__(self, min_length=11, max_length=11, *args, **kwargs):
        super(HROIBField, self).__init__(
            r'^\d{11}$', max_length=max_length, min_length=min_length,
            *args, **kwargs
        )

    def clean(self, value):
        super(HROIBField, self).clean(value)
        if value in self.empty_values:
            return self.empty_value

        return '%s' % (value, )


class HRLicensePlateField(Field):
    """
    Vehicle license plate of Croatia field.

    Normalizes to the specific format
    below. Suffix is constructed from the shared letters of the Croatian and
    English alphabets.

    Format examples:
        SB 123-A
        (but also supports more characters)
        ZG 1234-AA

    Used for standardized license plates only.
    """

    default_error_messages = {
        'invalid': _('Enter a valid vehicle license plate number'),
        'area': _('Enter a valid location code'),
        'number': _('Number part cannot be zero'),
    }

    def clean(self, value):
        super(HRLicensePlateField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        value = re.sub(r'[\s\-]+', '', force_text(value.strip())).upper()

        matches = plate_re.search(value)
        if matches is None:
            raise ValidationError(self.error_messages['invalid'])

        # Make sure the prefix is in the list of known codes.
        prefix = matches.group('prefix')
        if prefix not in [choice[0] for choice in HR_LICENSE_PLATE_PREFIX_CHOICES]:
            raise ValidationError(self.error_messages['area'])

        # Make sure the number portion is not zero.
        number = matches.group('number')
        if int(number) == 0:
            raise ValidationError(self.error_messages['number'])

        return '%s %s-%s' % (prefix, number, matches.group('suffix'))


class HRPostalCodeField(Field):
    """
    Postal code of Croatia field.

    It consists of exactly five digits ranging from 10000 to possibly less than 60000.

    http://www.posta.hr/main.aspx?id=66
    """

    default_error_messages = {
        'invalid': _('Enter a valid 5 digit postal code'),
    }

    def clean(self, value):
        super(HRPostalCodeField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        value = value.strip()
        if not postal_code_re.search(value):
            raise ValidationError(self.error_messages['invalid'])

        # Make sure the number is in valid range.
        if not 9999 < int(value) < 60000:
            raise ValidationError(self.error_messages['invalid'])

        return '%s' % value


class HRJMBAGField(Field):
    """
    Unique Master Academic Citizen Number of Croatia (JMBAG) field.

    This number is used by college students and professors in Croatia.

    http://www.cap.srce.hr/IzgledX.aspx
    """

    default_error_messages = {
        'invalid': _('Enter a valid 19 digit JMBAG starting with 601983'),
        'copy': _('Card issue number cannot be zero'),
    }

    def clean(self, value):
        super(HRJMBAGField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        value = re.sub(r'[\-\s]', '', value.strip())

        matches = jmbag_re.search(value)
        if matches is None:
            raise ValidationError(self.error_messages['invalid'])

        # Make sure the issue number is not zero.
        if matches.group('copy') == '0':
            raise ValidationError(self.error_messages['copy'])

        # Validate checksum using Luhn algorithm.
        if not luhn(value):
            raise ValidationError(self.error_messages['invalid'])

        return '%s' % value
