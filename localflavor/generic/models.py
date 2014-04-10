from django.db import models

from .validators import IBANValidator


class IBANField(models.CharField):
    """
    An IBAN consists of up to 34 alphanumeric characters.

    In addition to validating official IBANs, this field can optionally validate unofficial IBANs that have been
    catalogued by Nordea.

    https://en.wikipedia.org/wiki/International_Bank_Account_Number

    .. versionadded:: 1.1
    """
    def __init__(self, use_nordea_extensions=False, *args, **kwargs):
        kwargs.setdefault('max_length', 34)
        super(IBANField, self).__init__(*args, **kwargs)
        self.validators.append(IBANValidator(use_nordea_extensions))
