"""IT-specific Form helpers."""

from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Field, RegexField, Select
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.forms import DeprecatedPhoneNumberFormFieldMixin

from .it_province import PROVINCE_CHOICES
from .it_region import REGION_CHOICES, REGION_PROVINCE_CHOICES
from .util import ssn_validation, vat_number_validation

phone_digits_re = re.compile(r'^(?:\+?39)?((0\d{1,3})(\d{4,8})|(3\d{2})(\d{6,8}))$')


class ITZipCodeField(RegexField):
    """
    A form field that validates input as an Italian zip code.

    Valid codes must have five digits.
    """

    default_error_messages = {
        'invalid': _('Enter a valid zip code.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(ITZipCodeField, self).__init__(r'^\d{5}$',
                                             max_length, min_length, *args, **kwargs)


class ITRegionSelect(Select):
    """A Select widget that uses a list of IT regions as its choices."""

    def __init__(self, attrs=None):
        super(ITRegionSelect, self).__init__(attrs, choices=REGION_CHOICES)


class ITRegionProvinceSelect(Select):
    """A Select widget that uses a named group list of IT regions mapped to regions as its choices."""

    def __init__(self, attrs=None):
        super(ITRegionProvinceSelect, self).__init__(attrs, choices=REGION_PROVINCE_CHOICES)


class ITProvinceSelect(Select):
    """A Select widget that uses a list of IT provinces as its choices."""

    def __init__(self, attrs=None):
        super(ITProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)


class ITSocialSecurityNumberField(RegexField):
    """
    A form field that validates Italian Tax code (codice fiscale) for both persons and entities.

    For reference see http://www.agenziaentrate.it/ and search for:

    * 'Informazioni sulla codificazione delle persone fisiche' for persons' SSN
    * 'Codice fiscale Modello AA5/6' for entities' SSN

    .. versionchanged:: 1.1

    The ``ITSocialSecurityNumberField`` now also accepts SSN values for
    entities (numeric-only form).
    """

    default_error_messages = {
        'invalid': _('Enter a valid Tax code.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(ITSocialSecurityNumberField, self).__init__(r'^\w{3}\s*\w{3}\s*\w{5}\s*\w{5}$|\d{10}',
                                                          max_length, min_length,
                                                          *args, **kwargs)

    def clean(self, value):
        value = super(ITSocialSecurityNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('\s', '', value).upper()
        # Entities SSN are numeric-only
        if value.isdigit():
            try:
                return vat_number_validation(value)
            except ValueError:
                raise ValidationError(self.error_messages['invalid'])
        # Person SSN
        else:
            try:
                return ssn_validation(value)
            except (ValueError, IndexError):
                raise ValidationError(self.error_messages['invalid'])


class ITVatNumberField(Field):
    """A form field that validates Italian VAT numbers (partita IVA)."""

    default_error_messages = {
        'invalid': _('Enter a valid VAT number.'),
    }

    def clean(self, value):
        value = super(ITVatNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        try:
            return vat_number_validation(value)
        except ValueError:
            raise ValidationError(self.error_messages['invalid'])


class ITPhoneNumberField(CharField, DeprecatedPhoneNumberFormFieldMixin):
    """
    A form field that validates input as an Italian phone number.

    Will strip any +39 country prefix from the number.

    .. versionadded:: 1.1
    """

    default_error_messages = {
        'invalid': _('Enter a valid Italian phone number.'),
    }

    def clean(self, value):
        super(ITPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub(r'[^\+\d]', '', force_text(value))
        m = phone_digits_re.match(value)
        if m:
            return '%s %s' % tuple(group for group in m.groups()[1:] if group)
        raise ValidationError(self.error_messages['invalid'])
