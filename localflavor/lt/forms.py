from __future__ import unicode_literals

import re
from datetime import date

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select
from django.utils.six import text_type
from django.utils.translation import ugettext_lazy as _

from .lt_choices import COUNTY_CHOICES, MUNICIPALITY_CHOICES

postalcode = re.compile(r'^(LT\s?-\s?)?(?P<code>\d{5})$', re.IGNORECASE)


class LTCountySelect(Select):
    """A select field with the Lithuanian counties as choices"""

    def __init__(self, attrs=None):
        super(LTCountySelect, self).__init__(attrs, choices=COUNTY_CHOICES)


class LTMunicipalitySelect(Select):
    """A select field with the Lithuanian municipalities as choices"""

    def __init__(self, attrs=None):
        super(LTMunicipalitySelect, self).__init__(attrs,
                                                   choices=MUNICIPALITY_CHOICES)


class LTIDCodeField(RegexField):
    """
    A form field that validates as Lithuanian ID Code.

    Checks:
        * Made of exactly 11 decimal numbers.
        * Checksum is correct.
        * ID contains valid date.
    """

    default_error_messages = {
        'invalid': _('ID Code consists of exactly 11 decimal digits.'),
        'checksum': _('Wrong ID Code checksum.'),
        'date': _('ID Code contains invalid date.')
    }

    def __init__(self, *args, **kwargs):
        super(LTIDCodeField, self).__init__(r'^\d{11}$', *args, **kwargs)

    def clean(self, value):
        super(LTIDCodeField, self).clean(value)

        if value in EMPTY_VALUES:
            return ''

        if not self.valid_date(value):
            raise ValidationError(self.error_messages['date'])

        if not self.valid_checksum(value):
            raise ValidationError(self.error_messages['checksum'])
        return value

    def valid_checksum(self, value):
        first_sum = 0
        second_sum = 0

        for i in range(10):
            first_sum += int(value[i]) * (i % 9 + 1)
            second_sum += int(value[i]) * ((i + 2) % 9 + 1)

        k = first_sum % 11
        if k == 10:
            k = second_sum % 11
            k = 0 if k == 10 else k

        return True if k == int(value[-1]) else False

    def valid_date(self, value):
        """
        Check if date in ID code is valid.

        We won't check for dates in future as it would become too restrictive.
        """
        try:
            year = {'1': 1800, '2': 1800, '3': 1900, '4': 1900, '5': 2000,
                    '6': 2000}[value[0]] + int(value[1:3])
            date(year, int(value[3:5]), int(value[5:7]))
            return True
        except (ValueError, KeyError):
            return False


class LTPostalCodeField(Field):
    """
    A form field that validates and normalizes Lithanuan postal codes.

    Lithuanian postal codes in following forms accepted:
        * XXXXX
        * LT-XXXXX
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in the format XXXXX or LT-XXXXX.'),
    }

    def clean(self, value):
        value = super(LTPostalCodeField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        match = re.match(postalcode, value)
        if not match:
            raise ValidationError(self.error_messages['invalid'])

        return 'LT-' + match.group('code')


class LTPhoneField(Field):
    """
    Form field that validates as Lithuanian phone number.

    You can accept any permutation of following phone numbers:

        * Emergency (01, 02, 03, 04, 112)
        * Mobile (370 600 00 000)
        * Landline
        * Service numbers

    If you accept landline numbers, you can opt in to accepting local landline
    numbers too. Local landline numbers are numbers without area code.

    This field does not accept multiple numbers (as separated by /).

    The field tries its best to convert the number into one you can call to
    internationally. Currently emergency and most of landline_local numbers are
    not converted.

    .. versionadded:: 1.1
    """

    # Order dependent (shorter codes cannot go before longer ones)
    _area_codes = tuple(map(text_type,
                            [425, 315, 381, 319, 450, 313, 528, 386, 349, 426, 447, 346, 427, 347,
                             445, 459, 318, 343, 443, 383, 469, 421, 460, 451, 448, 319, 422, 428,
                             458, 440, 345, 380, 449, 441, 382, 387, 446, 444, 528, 340, 389, 310,
                             342, 386, 385, 45, 46, 41, 37, 5]))
    _stripable = re.compile(r'[\+()~ ]')
    default_error_messages = {
        'non-digit': _('Phone number can only contain digits'),
        'no-parse': _('Could not validate the phone number'),
    }

    def __init__(self, mobile=True, landline=True, emergency=False,
                 landline_local=False, service=False, **kwargs):
        self._checks = []
        if mobile:
            self._checks.append(self._clean_mobile)
        if landline:
            self._checks.append(self._clean_landline)
        if service:
            self._checks.append(self._clean_service)
        if emergency:
            self._checks.append(self._clean_emergency)

        if landline_local and not landline:
            raise ValueError("Cannot accept local landline numbers if " +
                             "regular landline numbers are not accepted")
        elif landline_local:
            self._checks.append(self._clean_landline_local)

        super(LTPhoneField, self).__init__(**kwargs)

    def clean(self, value):
        value = super(LTPhoneField, self).clean(value)

        if value in EMPTY_VALUES:
            return ''

        value = self._stripable.sub('', value.strip())
        if not value.isdigit():
            raise ValidationError(self.error_messages['non-digit'],
                                  code='invalid')

        results = list(filter(lambda x: x is not None,
                              map(lambda fn: fn(value), self._checks)))
        if results:
            # TODO: More than one result means code error, check for it.
            return results[0]
        raise ValidationError(self.error_messages['no-parse'], code='invalid')

    def _clean_emergency(self, value):
        if value in ["112", "01", "02", "03", "04"]:
            return value

    def _clean_mobile(self, value):
        if len(value) == 9 and value[:2] == "86":
            return "+370" + value[1:]
        elif len(value) == 11 and value[:4] == "3706":
            return "+" + value

    def _clean_service(self, value):
        if len(value) == 9 and value[:4] == "8800":
            return "+370" + value[1:]
        elif len(value) == 11 and value[:6] == "370800":
            return "+" + value

    # Now these two are most complex ones.
    def _clean_landline_local(self, value):
        # The landline phone number must always be 8 digits in length when the
        # number contains an area code. Now area codes can range from 1 to 3
        # digits (ex. 5 for Vilnius district or 389 for Utena). For local
        # (in district) calling you don't have to include the area code,
        # therefore local numbers can range from 5 to 7 digits in length.
        #
        # We cannot prepend area code or country code to those numbers because
        # there's more than one possibility in almost all cases with a
        # single exception being Vilnius district. As Vilnius is the only
        # district that has a single digit code, we can safely assume the
        # number is for Vilnius.

        if 5 <= len(value) <= 6:
            return value
        elif len(value) == 7:
            return "+3705" + value

    def _clean_landline(self, value):
        if len(value) == 9 and value[0] == "8":
            number = value[1:]
        elif len(value) == 11 and value[:3] == "370":
            number = value[3:]
        else:
            return None
        if number.startswith(self._area_codes):
            return "+370" + number
