"""Kenya-specific Form Helpers"""

import re

from django.forms import ValidationError
from django.forms.fields import CharField, RegexField, Select
from django.utils.translation import gettext_lazy as _

from .ke_counties import COUNTY_CHOICES

ke_po_box_re = re.compile(r"\A\d{5,5}\Z")
ke_kra_pin_regex = re.compile(r"^(A|P)\d{9}[A-Z]$")
ke_passport_regex = re.compile(r"^[A-Z]\d{6,7}$")
ke_national_id_regex = re.compile(r"^\d{7,8}$")


class KEPostalCodeField(CharField):
    """
    A form field that validates its input as a Kenyan Postal Code.
    .. versionadded:: 4.0
    """

    default_error_messages = {
        "invalid": _("Enter a valid Kenyan Postal code in the format 12345")
    }

    def clean(self, value: str):
        """Validates KE Postal Code

        Args:
            value (_type_): _description_

        Raises:
            ValidationError: _description_

        Returns:
            _type_: _description_
        """
        value = super().clean(value)
        if value in self.empty_values:
            return self.empty_value

        # Strip out spaces and dashes
        value = value.replace(" ", "").replace("-", "")
        match = re.match(ke_po_box_re, value)
        if not match:
            raise ValidationError(self.error_messages.get("invalid"))
        return value


class KEKRAPINField(CharField):
    """
    TODO

    A form field that validates input as a Kenya Revenue Authority PIN
    (Personal Identification Number) Number.

    A Kenyan KRA (Kenya Revenue Authority) PIN (Personal Identification Number)

    is typically 11 characters long, consisting of the letter 'A' or 'P' followed

    by 9 digits and ending with a letter (e.g., A123456789B or P987654321C).

    Validates 2 different formats:

        POXXXXXXXX - Company/Institution

        AXXXXXXXXX - Individuals

    .. versionadded:: 4.0
        
    """

    default_error_messages = {
        "invalid": _(
            "Enter a valid Kenyan KRA PIN Number in the format A123456789B or P987654321C"
        ),
    }

    def clean(self, value):
        """Runs the validation checks

        Args:
            value (_type_): _description_

        Raises:
            ValidationError: _description_

        Returns:
            _type_: _description_
        """
        value = super().clean(value)
        if value in self.empty_values:
            return self.empty_value

        # Strip out spaces and dashes
        value = value.replace(" ", "").replace("-", "")
        match = re.match(ke_kra_pin_regex, value)
        if not match:
            raise ValidationError(self.error_messages.get("invalid"))
        return value.upper()


class KENationalIDNumberField(CharField):
    """
    A form field that validates its input as a Kenyan National ID Number.
    .. versionadded:: 4.0
    """

    default_error_messages = {
        "invalid": _(
            "Enter a valid Kenyan National ID Number in the format 1234567 or 12345678"
        )
    }

    def clean(self, value):
        """Runs the validation checks for KE National ID Number"""
        value = super().clean(value)
        if value in self.empty_values:
            return self.empty_value

        # Strip out spaces and dashes
        value = value.replace(" ", "").replace("-", "")
        match = re.match(ke_national_id_regex, value)
        if not match:
            raise ValidationError(self.error_messages.get("invalid"))
        return value


class KEPassportNumberField(CharField):
    """
    A form field that validates its input as a Kenyan Passport Number.
    .. versionadded:: 4.0
    """

    default_error_messages = {
        "invalid": _(
            "Enter a valid Kenyan Passport Number in the format A123456 or B1234567"
        )
    }

    def clean(self, value):
        """Runs the validation checks for KE Passport Number"""
        value = super().clean(value)
        if value in self.empty_values:
            return self.empty_value

        # Strip out spaces and dashes
        value = value.replace(" ", "").replace("-", "")
        match = re.match(ke_passport_regex, value)
        if not match:
            raise ValidationError(self.error_messages.get("invalid"))
        return value.upper()


class KENSSFNumberField(RegexField):
    """
    TODO

    Kenya National Social Security Fund
    """

    ...


class KENHIFNumberField(RegexField):
    """
    TODO

    Kenya National Hospital Insurance Fund
    """

    ...


class KECompanyRegNumberField(RegexField):
    """
    Kenya Companies Reg. Number
    """

    ...


class KEPayBillNumber(RegexField):
    """
    MPESA PayBill
    """

    ...


class KECountySelectField(Select):
    """
    A Select widget listing Kenyan Counties as the choices
    .. versionadded:: 4.0
    """

    def __init__(self, attrs=None) -> None:
        super().__init__(attrs, choices=COUNTY_CHOICES)
