# -*- coding: utf-8 -*-
"""New Zealand specific form helpers."""
from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select
from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.forms import DeprecatedPhoneNumberFormFieldMixin

from .nz_councils import NORTH_ISLAND_COUNCIL_CHOICES, SOUTH_ISLAND_COUNCIL_CHOICES
from .nz_provinces import PROVINCE_CHOICES
from .nz_regions import REGION_CHOICES

PHONE_08_RE = re.compile(r'^((0800\d{6})|(0800\w{6,10}))$')
PHONE_IN_RE = re.compile(r'^((0064|064|\+64|\+\+64)((\d{8})|(2\d{7,9})))$')
PHONE_NZ_RE = re.compile(r'^((0\d{8})|(02\d{7,9}))$')

BANK_ACCOUNT_NUMBER_RE = re.compile(r'^(\d{2})(\d{4})(\d{7})(\d{2,3})$')


class NZRegionSelect(Select):
    """A select widget with list of New Zealand regions as its choices."""

    def __init__(self, attrs=None):
        super(NZRegionSelect, self).__init__(attrs, choices=REGION_CHOICES)


class NZProvinceSelect(Select):
    """A select widget with list of New Zealand provinces as its choices."""

    def __init__(self, attrs=None):
        super(NZProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)


class NZNorthIslandCouncilSelect(Select):
    """A select widget with list of New Zealand North Island city and district councils as its choices."""

    def __init__(self, attrs=None):
        super(NZNorthIslandCouncilSelect, self).__init__(attrs, choices=NORTH_ISLAND_COUNCIL_CHOICES)


class NZSouthIslandCouncilSelect(Select):
    """A select widget with list of New Zealand South Island city and district councils as its choices."""

    def __init__(self, attrs=None):
        super(NZSouthIslandCouncilSelect, self).__init__(attrs, choices=SOUTH_ISLAND_COUNCIL_CHOICES)


class NZPostCodeField(RegexField):
    """A form field that validates its input as New Zealand postal code."""

    default_error_messages = {
        'invalid': _('Invalid post code.'),
    }

    def __init__(self, *args, **kwargs):
        super(NZPostCodeField, self).__init__(r'^\d{4}$',
                                              *args, **kwargs)


class NZPhoneNumberField(Field, DeprecatedPhoneNumberFormFieldMixin):
    """A form field that validates its input as New Zealand phone number."""

    default_error_messages = {'invalid': _('Invalid phone number.')}

    def clean(self, value):
        super(NZPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\(|\)|\s+|_|-)', '', smart_str(value))
        value = re.sub('^(\+\+)', '00', smart_str(value))
        value = re.sub('^(\+)', '00', smart_str(value))
        phone_08_match = PHONE_08_RE.search(value)
        if phone_08_match:
            return '%s' % phone_08_match.group(0)
        phone_nz_match = PHONE_NZ_RE.search(value)
        if phone_nz_match:
            return '%s' % phone_nz_match.group(0)
        phone_in_match = PHONE_IN_RE.search(value)
        if phone_in_match:
            return '%s' % phone_in_match.group(0)
        raise ValidationError(self.error_messages['invalid'])


class NZBankAccountNumberField(Field):
    """
    A form field that validates its input as New Zealand bank account number.

    Formats:

        XX-XXXX-XXXXXXX-XX

        XX-XXXX-XXXXXXX-XXX


    Where:

    * the first two digits is the bank ID

    * the next four digits are the branch number where the account was opened

    * the next 7 digits are the account numbers

    * the last two or three digits define type of the account.

    """

    default_error_messages = {
        'invalid': _('Invalid bank account number.'),
    }

    def clean(self, value):
        super(NZBankAccountNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\s+|-)', '', smart_str(value))
        match = BANK_ACCOUNT_NUMBER_RE.search(value)
        if match:
            # normalize the last part
            last = '0%s' % match.group(4) if len(match.group(4)) == 2 else match.group(4)
            return '%s-%s-%s-%s' % (match.group(1),
                                    match.group(2), match.group(3), last)
        raise ValidationError(self.error_messages['invalid'])
