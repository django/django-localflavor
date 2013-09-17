"""
Denmark specific form helpers.
"""

from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import Select
from django.forms.fields import RegexField

from .dk_postalcodes import DK_POSTALCODES
from .dk_municipalities import DK_MUNICIPALITIES


class DKPostalCodeSelect(Select):
    """
    A Select widget that uses a list of Danish postal codes as its choices.
    """
    def __init__(self, attrs=None):
        super(DKPostalCodeSelect, self).__init__(
            attrs,
            choices=DK_POSTALCODES
        )


class DKMunicipalitySelect(Select):
    """
    A Select widget that uses a list of Norwegian municipalities (fylker)
    as its choices.
    """
    def __init__(self, attrs=None):
        super(DKMunicipalitySelect, self).__init__(
            attrs,
            choices=DK_MUNICIPALITIES
        )


class DKPhoneNumberField(RegexField):
    """
    Field with phone number validation. Requires a phone number with
    8 digits and optional country code
    """
    default_error_messages = {
        'invalid': _(
            'A phone number must be 8 digits and may have country code'
        ),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(DKPhoneNumberField, self).__init__(
            r'^(?:\+47)? ?(\d{3}\s?\d{2}\s?\d{3}|\d{2}\s?\d{2}\s?\d{2}\s?\d{2})$',
            max_length,
            min_length,
            *args,
            **kwargs
        )
