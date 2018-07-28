from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField
from localflavor.br import validators

from .br_states import STATE_CHOICES


class BRStateField(CharField):
    """A model field for states of Brazil."""

    description = _("State of Brazil (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        self.choices = STATE_CHOICES
        self.max_length = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(BRStateField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class BRCPFField(CharField):
    """
    A model field for the brazilian document named of CPF (Cadastro de Pessoa Física)
    """

    description = _("CPF Document")

    def __init__(self, *args, **kwargs):
        self.max_length = 14
        self.validators.append(validators.BRCPFValidator())
        super().__init__(*args, **kwargs)


class BRCNPJField(CharField):
    """
    A model field for the brazilian document named of CNPJ (Cadastro Nacional de Pessoa Jurídica)
    """

    description = _("CNPJ Document")

    def __init__(self, *args, **kwargs):
        self.max_length = 18
        self.validators.append(validators.BRCNPJValidator())
        super().__init__(*args, **kwargs)


class BRTelephoneField(CharField):
    """
    A model field for the brazilian telephone
    """

    description = _("Telephone (with DDD)")

    def __init__(self, *args, **kwargs):
        self.max_length = 14
        self.validators.append(validators.BRTelephoneValidator())
        super().__init__(*args, **kwargs)


class BRCellPhoneField(CharField):
    """
    A model field for the brazilian cell phone
    """

    description = _("Cell Phone (whith DDD)")

    def __init__(self, *args, **kwargs):
        self.max_length = 15
        self.validators.append(validators.BRCellPhoneValidator())
        super().__init__(*args, **kwargs)


class BRZipCodeField(CharField):
    """
    A model field for the brazilian zip code
    """

    description = _("Zip Code")

    def __init__(self, *args, **kwargs):
        self.max_length = 9
        self.validators.append(validators.BRZipCodeValidator())
        super().__init__(*args, **kwargs)
