"""Sri Lanka specific Form helpers."""

from django.forms.fields import RegexField
from django.utils.translation import gettext_lazy as _


class LKPostalCodeFormField(RegexField):
    """
        A form field that accepts Sri Lanka postal code.
        Format : XXXXX

        Postal codes: https://en.wikipedia.org/wiki/Postal_codes_in_Sri_Lanka
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in format XXXXX'),
    }

    def __init__(self, **kwargs):
        super().__init__(r'^\d{5}$', **kwargs)
