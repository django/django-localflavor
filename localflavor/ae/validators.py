"""UAE-specific validation helpers."""

import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UAEEmiratesIDValidator:
    """
    Validator for UAE Emirates ID numbers.

    UAE Emirates ID is a 15-digit number with format: 784-YYYY-NNNNNNN-N
    where:
    - 784 is the UAE country code
    - YYYY is an identification block assigned by ICP
    - NNNNNNN is a unique 7-digit number
    - N is a check digit
    """

    message = _('Enter a valid UAE Emirates ID number.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        """Validate UAE Emirates ID."""
        if not value:
            return

        # Remove any dashes or spaces
        clean_value = re.sub(r'[\s\-]', '', str(value))

        # Check if it's exactly 15 digits
        if not re.match(r'^\d{15}$', clean_value):
            raise ValidationError(self.message, code=self.code)

        # Check if it starts with 784 (UAE country code)
        if not clean_value.startswith('784'):
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.message == other.message and
            self.code == other.code
        )


@deconstructible
class UAEPostalCodeValidator:
    """
    Validator for UAE postal codes.

    UAE doesn't use postal codes, but some systems require "00000" format.
    """

    message = _('Enter a valid UAE postal code. Use 00000 if postal code is required.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        """Validate UAE postal code."""
        if not value:
            return

        clean_value = str(value).strip()

        # UAE postal code should be 00000 or empty
        if clean_value and clean_value != '00000':
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.message == other.message and
            self.code == other.code
        )


@deconstructible
class UAEPOBoxValidator:
    """
    Validator for UAE P.O. Box numbers.

    P.O. Box format is commonly used in UAE.
    """

    message = _('Enter a valid P.O. Box number.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        """Validate P.O. Box number."""
        if not value:
            return

        clean_value = str(value).strip().upper()

        # Remove "P.O. BOX", "PO BOX", or "POB" prefix if present
        clean_value = re.sub(r'^(?:P\.?\s*O\.?\s*B(?:OX)?\.?\s*)', '', clean_value)

        # Check if remaining value is numeric and reasonable length
        if not re.match(r'^\d{1,10}$', clean_value):
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.message == other.message and
            self.code == other.code
        )


@deconstructible
class UAETaxRegistrationNumberValidator:
    """
    Validator for UAE Tax Registration Numbers (TRN).

    UAE TRN is a 15-digit number used for VAT registration.
    """

    message = _('Enter a valid UAE Tax Registration Number (15 digits).')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not value:
            return

        clean_value = re.sub(r'\s', '', str(value))
        if not re.match(r'^\d{15}$', clean_value):
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.message == other.message and
            self.code == other.code
        )
