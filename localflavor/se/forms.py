# -*- coding: utf-8 -*-
"""Swedish specific Form helpers."""
from __future__ import unicode_literals

import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from .se_counties import COUNTY_CHOICES
from .utils import (format_organisation_number, format_personal_id_number, id_number_checksum, valid_organisation,
                    validate_id_birthday)

__all__ = ('SECountySelect', 'SEOrganisationNumberField',
           'SEPersonalIdentityNumberField', 'SEPostalCodeField')

SWEDISH_ID_NUMBER = re.compile(r'^(?P<century>\d{2})?(?P<year>\d{2})(?P<month>\d{2})(?P<day>\d{2})'
                               r'(?P<sign>[\-+])?(?P<serial>\d{3}|[A-Za-z]\d{2})(?P<checksum>\d)$')
SE_POSTAL_CODE = re.compile(r'^[1-9]\d{2} ?\d{2}$')


class SECountySelect(forms.Select):
    """
    A Select form widget that uses a list of the Swedish counties (län) as its choices.

    The cleaned value is the official county code -- see
    http://en.wikipedia.org/wiki/Counties_of_Sweden for a list.
    """

    def __init__(self, attrs=None):
        super(SECountySelect, self).__init__(attrs=attrs,
                                             choices=COUNTY_CHOICES)


class SEOrganisationNumberField(forms.CharField):
    """
    A form field that validates input as a Swedish organisation number (organisationsnummer).

    It accepts the same input as SEPersonalIdentityField (for sole
    proprietorships (enskild firma). However, co-ordination numbers are not
    accepted.

    It also accepts ordinary Swedish organisation numbers with the format
    NNNNNNNNNN.

    The return value will be YYYYMMDDXXXX for sole proprietors, and NNNNNNNNNN
    for other organisations.
    """

    default_error_messages = {
        'invalid': _('Enter a valid Swedish organisation number.'),
    }

    def clean(self, value):
        value = super(SEOrganisationNumberField, self).clean(value)

        if value in self.empty_values:
            return self.empty_value

        match = SWEDISH_ID_NUMBER.match(value)
        if not match:
            raise forms.ValidationError(self.error_messages['invalid'])

        gd = match.groupdict()

        # Compare the calculated value with the checksum
        if id_number_checksum(gd) != int(gd['checksum']):
            raise forms.ValidationError(self.error_messages['invalid'])

        # First: check if this is a real organisation_number
        if valid_organisation(gd):
            return format_organisation_number(gd)

        # Is this a single properitor (enskild firma)?
        try:
            birth_day = validate_id_birthday(gd, False)
            return format_personal_id_number(birth_day, gd)
        except ValueError:
            raise forms.ValidationError(self.error_messages['invalid'])


class SEPersonalIdentityNumberField(forms.CharField):
    """
    A form field that validates input as a Swedish personal identity number (personnummer).

    The correct formats are YYYYMMDD-XXXX, YYYYMMDDXXXX, YYMMDD-XXXX,
    YYMMDDXXXX and YYMMDD+XXXX.

    A + indicates that the person is older than 100 years, which will be taken
    into consideration when the date is validated.

    The checksum will be calculated and checked. The birth date is checked to
    be a valid date.

    By default, co-ordination numbers (samordningsnummer) will be accepted. To
    only allow real personal identity numbers, pass the keyword argument
    coordination_number=False to the constructor.

    Interim numbers (interimspersonnummer), used by educational institutions
    within the Ladok system, are supported but not accepted by default, since
    they are not considered valid outside Ladok. They have the same format and
    semantics as real personal identity numbers, except that the first control
    digit is replaced by a letter (A-Z). To allow the use of interim numbers,
    pass the keyword argument interim_numbers=True to the constructor.

    The cleaned value will always have the format YYYYMMDDXXXX.
    """

    def __init__(self, coordination_number=True, interim_number=False, *args, **kwargs):
        self.coordination_number = coordination_number
        self.interim_number = interim_number
        super(SEPersonalIdentityNumberField, self).__init__(*args, **kwargs)

    default_error_messages = {
        'invalid': _('Enter a valid Swedish personal identity number.'),
        'coordination_number': _('Co-ordination numbers are not allowed.'),
    }

    def clean(self, value):
        value = super(SEPersonalIdentityNumberField, self).clean(value)

        if value in self.empty_values:
            return self.empty_value

        match = SWEDISH_ID_NUMBER.match(value)
        if match is None:
            raise forms.ValidationError(self.error_messages['invalid'])

        gd = match.groupdict()
        is_coordination_number = int(gd['day']) > 60
        is_interim_number = gd['serial'][0].isalpha()

        # compare the calculated value with the checksum
        if id_number_checksum(gd) != int(gd['checksum']):
            raise forms.ValidationError(self.error_messages['invalid'])

        # check for valid birthday
        try:
            birth_day = validate_id_birthday(gd)
        except ValueError:
            raise forms.ValidationError(self.error_messages['invalid'])

        # make sure that co-ordination numbers do not pass if not allowed
        if not self.coordination_number and is_coordination_number:
            raise forms.ValidationError(self.error_messages['coordination_number'])

        # make sure that interim numbers do not pass if not allowed. This is
        # reported as the number being plain invalid, as most people don't know
        # what an interim number is.
        if not self.interim_number and is_interim_number:
            raise forms.ValidationError(self.error_messages['invalid'])

        # Combining the concepts of coordination and interim numbers is invalid.
        if is_coordination_number and is_interim_number:
            raise forms.ValidationError(self.error_messages['invalid'])

        return format_personal_id_number(birth_day, gd)


class SEPostalCodeField(forms.RegexField):
    """
    A form field that validates input as a Swedish postal code (postnummer).

    Valid codes consist of five digits (XXXXX). The number can optionally be
    formatted with a space after the third digit (XXX XX).

    The cleaned value will never contain the space.
    """

    default_error_messages = {
        'invalid': _('Enter a Swedish postal code in the format XXXXX.'),
    }

    def __init__(self, *args, **kwargs):
        super(SEPostalCodeField, self).__init__(SE_POSTAL_CODE, *args, **kwargs)

    def clean(self, value):
        value = super(SEPostalCodeField, self).clean(value)
        if value in self.empty_values:
            return self.empty_value
        return value.replace(' ', '')
