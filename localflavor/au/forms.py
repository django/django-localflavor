"""
Australian-specific Form helpers
"""

from __future__ import absolute_import, unicode_literals

import re

from django.core.validators import EMPTY_VALUES, RegexValidator
from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select, MultiValueField
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

from .au_states import STATE_CHOICES
from .widgets import AUMedicareNumberWidget

PHONE_DIGITS_RE = re.compile(r'^(\d{10})$')


class AUPostCodeField(RegexField):
    """ Australian post code field.

    Assumed to be 4 digits.
    Northern Territory 3-digit postcodes should have leading zero.
    """
    default_error_messages = {
        'invalid': _('Enter a 4 digit postcode.'),
    }

    def __init__(self, max_length=4, min_length=None, *args, **kwargs):
        super(AUPostCodeField, self).__init__(r'^\d{4}$',
                                              max_length, min_length, *args, **kwargs)


class AUPhoneNumberField(CharField):
    """
    A form field that validates input as an Australian phone number.

    Valid numbers have ten digits.
    """
    default_error_messages = {
        'invalid': 'Phone numbers must contain 10 digits.',
    }

    def clean(self, value):
        """
        Validate a phone number. Strips parentheses, whitespace and hyphens.
        """
        super(AUPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\(|\)|\s+|-)', '', smart_text(value))
        phone_match = PHONE_DIGITS_RE.search(value)
        if phone_match:
            return '%s' % phone_match.group(1)
        raise ValidationError(self.error_messages['invalid'])


class AUStateSelect(Select):
    """
    A Select widget that uses a list of Australian states/territories as its
    choices.
    """
    def __init__(self, attrs=None):
        super(AUStateSelect, self).__init__(attrs, choices=STATE_CHOICES)


class AUMedicareNumberField(MultiValueField):
    """
    A composed field for capturing a patient's medicare number and IRN

    The format of a medicare number is documented in
    http://www.medicareaustralia.gov.au/provider/vendors/files/acir-immunisation-document-formats.pdf
    on page 14.
    """

    def __init__(self, widget=AUMedicareNumberWidget, *args, **kwargs):
        error_messages = {
            'incomplete': "Enter a medicare card number and IRN.",
        }

        fields = (
            CharField(
                validators=[
                    RegexValidator(r'^\d{10}$',
                                   "Medicare number must be 10 digits."),
                    self._validate_medicare_checksum,
                ],
                error_messages={
                    'incomplete': "Enter a medicare card number.",
                }
            ),
            CharField(
                validators=[
                    RegexValidator(r'^\d$', "IRN must be a single digit."),
                ],
                error_messages={
                    'incomplete': "Enter an IRN (the number next to the name).",
                }
            ),
        )

        super(AUMedicareNumberField, self).__init__(
            fields=fields,
            error_messages=error_messages,
            widget=widget,
            *args, **kwargs)

    def compress(self, values):
        mcn, irn = values

        mcn = re.sub(r'\s+|-', '', smart_text(mcn))

        return (mcn, irn)

    @staticmethod
    def _validate_medicare_checksum(value):
        """
        Validate the medicare number

        The first digit must be between 2 and 6.

        The first 8 numbers as a weighted sum modulo 10 gives the check
        digit.

        The 10th digit and IRN are ignored for the purposes of the validation.
        """

        # remove spaces and hyphens
        value = re.sub(r'\s+|-', '', smart_text(value))

        if 2 <= int(value[0]) <= 6:
            raise ValidationError("Medicare number is not valid.")

        weightings = (1, 3, 7, 9, 1, 3, 7, 9)
        check_bit = sum(int(a) * b for (a, b) in zip(value, weightings)) % 10

        if check_bit != value[8]:
            raise ValidationError("Medicare number is not valid.")
