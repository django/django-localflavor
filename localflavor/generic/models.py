from django.db import models

from .validators import IBANValidator


class IBANField(models.CharField):
    """
    An IBAN consists of up to 34 alphanumeric characters.

    To limit validation to specific countries, set the include_countries argument with a tuple or list of ISO 3166-1
    alpha-2 codes. For example, `limit_countries=('NL', 'BE, 'LU')`.

    In addition to validating official IBANs, this field can optionally validate unofficial IBANs that have been
    catalogued by Nordea by setting the use_nordea_extensions argument to True.

    https://en.wikipedia.org/wiki/International_Bank_Account_Number

    .. versionadded:: 1.1
    """
    def __init__(self, use_nordea_extensions=False, include_countries=None, *args, **kwargs):
        kwargs.setdefault('max_length', 34)
        super(IBANField, self).__init__(*args, **kwargs)
        self.validators.append(IBANValidator(use_nordea_extensions, include_countries))

    def to_python(self, value):
        value = super(IBANField, self).to_python(value)
        return value.replace(' ', '')
