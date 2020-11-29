"""Kenya-specific Form Helpers"""

from django.forms import ValidationError
from django.forms.fields import RegexField, Select
from django.utils.translation import gettext_lazy as _

from .ke_counties import COUNTY_CHOICES


class KEPostalCodeField(RegexField):
    """
    A form field that validates its input as a Kenyan Postal Code.

    """

    default_error_messages = {
        "invalid": _("Enter a valid Postal code in the format XXXXX")
    }

    def __init__(self, **kwargs) -> None:
        """
        TODO
        """
        super().__init__(r"()", **kwargs)


class KEKraPinNumber(RegexField):
    """
    TODO

    Kenya Revenue Authority PIN Number

    Validates 2 different formats:

        POXXXXXXXX - Company/Institutions

        AXXXXXXXXX - Individuals
    """

    ...


class KEIDNumber(RegexField):
    """
    TODO

    Kenya National ID Number

    """

    ...


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


class KECountySelect(Select):
    """
    A Select widget listing Kenyan Counties as the choices
    """

    def __init__(self, attrs=None) -> None:
        super().__init__(attrs, choices=COUNTY_CHOICES)