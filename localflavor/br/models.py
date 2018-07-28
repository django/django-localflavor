# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField
from localflavor.br import validators

from .br_states import STATE_CHOICES


class BRStateField(CharField):
    """A model field for states of Brazil."""

    description = _("State of Brazil (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
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
        kwargs['max_length'] = 14
        super().__init__(*args, **kwargs)
        self.validators.append(validators.BRCPFValidator())


class BRCNPJField(CharField):
    """
    A model field for the brazilian document named of CNPJ (Cadastro Nacional de Pessoa Jurídica)
    """

    description = _("CNPJ Document")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        super().__init__(*args, **kwargs)
        self.validators.append(validators.BRCNPJValidator())


class BRTelephoneField(CharField):
    """
    A model field for the brazilian telephone
    """

    description = _("Telephone (with DDD)")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        super().__init__(*args, **kwargs)
        self.validators.append(validators.BRTelephoneValidator())


class BRCellPhoneField(CharField):
    """
    A model field for the brazilian cell phone
    """

    description = _("Cell Phone (whith DDD)")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 15
        super().__init__(*args, **kwargs)
        self.validators.append(validators.BRCellPhoneValidator())


class BRZipCodeField(CharField):
    """
    A model field for the brazilian zip code
    """

    description = _("Zip Code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super().__init__(*args, **kwargs)
        self.validators.append(validators.BRZipCodeValidator())
