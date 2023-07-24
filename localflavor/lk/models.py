"""Sri Lanka specific Model fields"""

import re

from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .forms import LKPostalCodeFormField


class LKPostalCodeValidator(RegexValidator):
    """
    A validator for Sri Lanka Postal Codes.
    """
    default_error_messages = {
        'invalid': _('Enter a postal code in format XXXXX'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(re.compile(r'^\d{5}$'), *args, **kwargs)


class LKPostalCodeField(models.CharField):
    """
        A model field that accepts Sri Lanka postal codes.
        Format: XXXXX
        Source: https://en.wikipedia.org/wiki/Postal_codes_in_Sri_Lanka
        .. versionadded:: 4.0
    """
    description = _("Postal Code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super().__init__(*args, **kwargs)
        self.validators.append(LKPostalCodeValidator())

    def formfield(self, **kwargs):
        defaults = {'form_class': LKPostalCodeFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
