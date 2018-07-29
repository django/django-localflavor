from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class BRCellPhoneValidator(RegexValidator):
    """A validator for Brazilian Cell Phone Numbers."""

    def __init__(self, *args, **kwargs):
        self.regex = '^[(]?[0-9]{2}[)]?[\s]?([0-9]{1})?[0-9]{4}[-]?[0-9]{4}$'
        self.message = _('Enter a phone number in the format 0000000000 or (00) 00000-0000')
        self.code = _('Invalid phone')
        super(BRCellPhoneValidator, self).__init__(*args, **kwargs)


class BRTelephoneValidator(RegexValidator):
    """A validator for Brazilian Telephone Numbers."""

    def __init__(self, *args, **kwargs):
        self.regex = '^[(]?[0-9]{2}[)]?[\s]?[0-9]{4}[-]?[0-9]{4}$'
        self.message = _('Enter a telephone in the format 0000000000 or (00) 0000-0000')
        self.code = 'Invalid telephone'
        super(BRTelephoneValidator, self).__init__(*args, **kwargs)


class BRZipCodeValidator(RegexValidator):
    """A validator for Brazilian Zip Codes (CEP)."""

    def __init__(self, *args, **kwargs):
        self.regex = '^[0-9]{5}[-]?[0-9]{3}$'
        self.message = _('Enter a zip code in the format 00000000 or 00000-000.')
        self.code = _('Invalid Zip Code')
        super(BRZipCodeValidator, self).__init__(*args, **kwargs)


class BRCNPJValidator(RegexValidator):
    def __init__(self, *args, **kwargs):
        self.regex = '^[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}$'
        self.message = _('Enter a CNPJ in the format 00000000000000 or 00.000.000/0000-00')
        self.code = _('Invalid CNPJ')
        super(BRCNPJValidator, self).__init__(*args, **kwargs)


class BRCPFValidator(RegexValidator):
    def __init__(self, *args, **kwargs):
        self.regex = '^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$'
        self.message = _('Enter a CPF in the format 00000000000 or 000.000.000-00')
        self.code = _('Invalid CPF')
        super(BRCPFValidator, self).__init__(*args, **kwargs)
