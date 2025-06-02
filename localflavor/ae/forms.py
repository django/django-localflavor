"""UAE-specific Form helpers."""

import re

from django.forms.fields import CharField, RegexField, Select, ChoiceField
from django.utils.translation import gettext_lazy as _

from .ae_emirates import EMIRATE_CHOICES
from .validators import UAEEmiratesIDValidator, UAEPostalCodeValidator, UAEPOBoxValidator


class UAEEmiratesIDField(CharField):
    """
    A field for validating UAE Emirates ID numbers.

    UAE Emirates ID format: 784-YYYY-NNNNNNN-N
    Where:
    - 784 is the UAE country code
    - YYYY is the year of birth (1900-current year)
    - NNNNNNN is a 7-digit sequence number
    - N is a single check digit

    .. versionadded:: 5.1
    """

    default_error_messages = {
        'invalid': _('Enter a valid UAE Emirates ID number in format 784-YYYY-NNNNNNN-N.'),
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.validators.append(UAEEmiratesIDValidator())

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return value

        # Remove any dashes or spaces and return clean 15-digit format
        clean_value = re.sub(r'[\s\-]', '', str(value))

        # Format as 784-YYYY-NNNNNNN-N for consistency
        if len(clean_value) == 15:
            formatted = f"{clean_value[:3]}-{clean_value[3:7]}-{clean_value[7:14]}-{clean_value[14]}"
            return formatted

        return clean_value


class UAEEmirateField(ChoiceField):
    """
    A choice field that uses a list of UAE Emirates as its choices.

    .. versionadded:: 5.1
    """

    def __init__(self, **kwargs):
        kwargs.setdefault('choices', EMIRATE_CHOICES)
        super().__init__(**kwargs)


class UAEEmirateSelect(Select):
    """
    A Select widget that uses a list of UAE Emirates as its choices.

    .. versionadded:: 5.1
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=EMIRATE_CHOICES)


class UAEPostalCodeField(CharField):
    """
    A field for validating UAE postal codes.

    UAE doesn't use postal codes, but some systems require "00000".
    This field accepts "00000" or empty values.

    .. versionadded:: 5.1
    """

    default_error_messages = {
        'invalid': _('Enter a valid UAE postal code. Use 00000 if postal code is required.'),
    }

    def __init__(self, **kwargs):
        kwargs.setdefault('required', False)
        super().__init__(**kwargs)
        self.validators.append(UAEPostalCodeValidator())

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return self.empty_value

        # Normalize to 00000 if needed
        clean_value = str(value).strip()
        if clean_value in ('00000', ''):
            return clean_value

        return value


class UAEPOBoxField(CharField):
    """
    A field for validating UAE P.O. Box numbers.

    Accepts formats: "P.O. Box XXXXX", "PO Box XXXXX", "POB XXXXX", or just "XXXXX"

    .. versionadded:: 5.1
    """

    default_error_messages = {
        'invalid': _('Enter a valid P.O. Box number.'),
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.validators.append(UAEPOBoxValidator())

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return value

        # Clean up the value
        clean_value = str(value).strip().upper()

        # Remove "P.O. BOX" or "PO BOX" prefix if present
        clean_value = re.sub(r'^(P\.?O\.?\s*BOX\s*)', '', clean_value)

        # Return just the number part
        if re.match(r'^\d{1,10}$', clean_value):
            return clean_value

        return value


class UAETaxRegistrationNumberField(RegexField):
    """
    A field for validating UAE Tax Registration Numbers (TRN).

    UAE TRN is a 15-digit number used for VAT registration.

    .. versionadded:: 5.1
    """

    default_error_messages = {
        'invalid': _('Enter a valid UAE Tax Registration Number (15 digits).'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^\d{15}$', **kwargs)

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return value

        # Remove any spaces or formatting
        clean_value = re.sub(r'\s', '', str(value))
        return clean_value
