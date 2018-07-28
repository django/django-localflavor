from django.core.validators import RegexValidator


class BRCellPhoneValidator(RegexValidator):
    """A validator for Brazilian Cell Phone Numbers."""

    def __init__(self, *args, **kwargs):
        self.regex = '^[(]?[0-9]{2}[)]?[\s]?([0-9]{1})?[0-9]{4}[-]?[0-9]{4}$'
        self.message = 'Celular apenas com números ou no formato (00) 00000-0000'
        self.code = 'Celular inválido'
        super().__init__(*args, **kwargs)


class BRTelephoneValidator(RegexValidator):
    """A validator for Brazilian Telephone Numbers."""

    def __init__(self, *args, **kwargs):
        self.regex = '^[(]?[0-9]{2}[)]?[\s]?[0-9]{4}[-]?[0-9]{4}$'
        self.message = 'Telefone apenas com números ou no formato (00) 0000-0000'
        self.code = 'Telefone inválido'
        super().__init__(*args, **kwargs)


class BRZipCodeValidator(RegexValidator):
    """A validator for Brazilian Zip Codes (CEP)."""

    def __init__(self, *args, **kwargs):
        self.regex = '^[0-9]{5}[-]?[0-9]{3}$'
        self.message = 'CEP apenas com números ou no formato 00000-000'
        self.code = 'CEP inválido'
        super().__init__(*args, **kwargs)


class BRCNPJValidator(RegexValidator):
    def __init__(self, *args, **kwargs):
        self.regex = '^[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}$'
        self.message = 'CNPJ apenas com números ou no formato 00.000.000/0000-00'
        self.code = 'CNPJ inválido'
        super().__init__(*args, **kwargs)


class BRCPFValidator(RegexValidator):
    def __init__(self, *args, **kwargs):
        self.regex = '^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$'
        self.message = 'CPF apenas com números ou no formato 000.000.000-00'
        self.code = 'CPF inválido'
        super().__init__(*args, **kwargs)
