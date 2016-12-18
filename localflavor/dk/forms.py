"""Denmark specific Form helpers."""

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.forms import fields, widgets
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.forms import DeprecatedPhoneNumberFormFieldMixin

from .dk_municipalities import DK_MUNICIPALITIES
from .dk_postalcodes import DK_POSTALCODES


def postal_code_validator(value):
    if value not in [entry[0] for entry in DK_POSTALCODES]:
        raise ValidationError(_('Enter a postal code in the format XXXX.'))


class DKPostalCodeField(fields.CharField):
    """An Input widget that uses a list of Danish postal codes as valid input."""

    default_validators = [postal_code_validator]


class DKMunicipalitySelect(widgets.Select):
    """A Select widget that uses a list of Danish municipalities (kommuner) as its choices."""

    def __init__(self, attrs=None, *args, **kwargs):
        super(DKMunicipalitySelect, self).__init__(
            attrs,
            choices=DK_MUNICIPALITIES,
            *args,
            **kwargs
        )


class DKPhoneNumberField(fields.RegexField, DeprecatedPhoneNumberFormFieldMixin):
    """
    Field with phone number validation.

    Requires a phone number with 8 digits and optional country code.
    """

    default_error_messages = {
        'invalid': _(
            'A phone number must be 8 digits and may have country code'
        ),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(DKPhoneNumberField, self).__init__(
            r'^(?:\+45)? ?(\d{2}\s?\d{2}\s?\d{2}\s?\d{2})$',
            max_length,
            min_length,
            *args,
            **kwargs
        )
