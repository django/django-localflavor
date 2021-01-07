"""Kenya-specific Form Helpers"""

import re

from django.forms import ValidationError
from django.forms.fields import RegexField, Select
from django.utils.translation import gettext_lazy as _

from .ke_counties import COUNTY_CHOICES

ke_id_re = re.compile(r"^\d{7}(?:\d{1})?$")
ke_po_box_re = re.compile(r"\A\d{5,5}\Z")

class KEPostalCodeField(RegexField):
    """
    A form field that validates its input as a Kenyan Postal Code.

    """

    default_error_messages = {
        "invalid": _("Enter a valid Kenyan Postal code in the format 12345")
    }

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return self.empty_value

        # Strip out spaces and dashes
        value = value.replace(" ", "").replace("-", "")
        match = re.match(ke_po_box_re, value)
        if not match:
            raise ValidationError(self.error_messages.get("invalid"))
        return value




class KEKraPinNumber(RegexField):
    """
    TODO

    A form field that validates input as a Kenya Revenue Authority PIN Number

    Validates 2 different formats:

        POXXXXXXXX - Company/Institutions

        AXXXXXXXXX - Individuals
    """

    ...


class KEIDNumber(RegexField):
    """
    TODO

    Kenya National ID Number

    8 Digits

    """

    default_error_messages = {
        "invalid": _("Enter a valid Kenyan ID Number"),
    }

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return self.empty_value

        # Strip out spaces and dashes
        value = value.replace(" ", "").replace("-", "")
        match = re.match(ke_id_re, value)

        if not match:
            raise ValidationError(self.error_messages.get("invalid"))
        return value


class KEPassportNumber(RegexField):
    """
    TODO

    Kenya Passport Number
    """

    ...


class KENSSFNumber(RegexField):
    """
    TODO

    Kenya National Social Security Fund
    """

    ...


class KENHIFNumber(RegexField):
    """
    TODO

    Kenya National Hospital Insurance Fund
    """

    ...


class KECompanyRegNumber(RegexField):
    """
    Kenya Companies Reg. Number
    """

    ...


class KEPayBillNumber(RegexField):
    """
    MPESA PayBill
    """

    ...


class KECountySelect(Select):
    """
    A Select widget listing Kenyan Counties as the choices
    """

    def __init__(self, attrs=None) -> None:
        super().__init__(attrs, choices=COUNTY_CHOICES)
