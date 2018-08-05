# -*- encoding: utf-8 -*-

from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _
from localflavor.br import validators
from .br_states import STATE_CHOICES


class BRStateField(CharField):
    """A model field for states of Brazil."""

    description = _("State of Brazil (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(BRStateField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(BRStateField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class BRCPFField(CharField):
    """
    A model field for the brazilian document named of CPF (Cadastro de Pessoa Física)

    .. versionadded:: 2.1
    """

    description = _("CPF Document")

    def __init__(self, *args, **kwargs):
        kwargs['min_length'] = 11
        kwargs['max_length'] = 14
        super(BRCPFField, self).__init__(*args, **kwargs)
        self.validators.append(validators.BRCPFValidator())


class BRCNPJField(CharField):
    """
    A model field for the brazilian document named of CNPJ (Cadastro Nacional de Pessoa Jurídica)

    .. versionadded:: 2.1
    """

    description = _("CNPJ Document")

    def __init__(self, *args, **kwargs):
        kwargs['min_length'] = 14
        kwargs['max_length'] = 18
        super(BRCNPJField, self).__init__(*args, **kwargs)
        self.validators.append(validators.BRPostalCodeValidator())


class BRPostalCodeField(CharField):
    """
    A model field for the brazilian zip code

    .. versionadded:: 2.1
    """

    description = _("Postal Code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super(BRPostalCodeField, self).__init__(*args, **kwargs)
        self.validators.append(validators.BRPostalCodeValidator())
