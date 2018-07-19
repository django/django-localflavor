from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField
from django.core.validators import RegexValidator

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
    """

    description = _("CPF Document")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        kwargs['validators'] = [
            RegexValidator(
                regex='^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$',
                message='CPF apenas com números ou no formato 000.000.000-00',
                code='CPF inválido',
            ),
        ]
        super(BRCPFField, self).__init__(*args, **kwargs)


class BRCNPJField(CharField):
    """
    A model field for the brazilian document named of CNPJ (Cadastro Nacional de Pessoa Jurídica)
    """

    description = _("CNPJ Document")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        kwargs['validators'] = [
            RegexValidator(
                regex='^[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}$',
                message='CNPJ apenas com números ou no formato 00.000.000/0000-00',
                code='CNPJ inválido',
            ),
        ]
        super(BRCNPJField, self).__init__(*args, **kwargs)


class BRTelephoneField(CharField):
    """
    A model field for the brazilian telephone
    """

    description = _("Telephone (with DDD)")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        kwargs['validators'] = [
            RegexValidator(
                regex='^[(]?[0-9]{2}[)]?[\s]?[0-9]{4}[-]?[0-9]{4}$',
                message='Telefone apenas com números ou no formato (00) 0000-0000',
                code='Telefone inválido',
            ),
        ]
        super(BRTelephoneField, self).__init__(*args, **kwargs)


class BRCellPhoneField(CharField):
    """
    A model field for the brazilian cell phone
    """

    description = _("Cell Phone (whith DDD)")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 15
        kwargs['validators'] = [
            RegexValidator(
                regex='^[(]?[0-9]{2}[)]?[\s]?([0-9]{1})?[0-9]{4}[-]?[0-9]{4}$',
                message='Celular apenas com números ou no formato (00) 00000-0000',
                code='Celular inválido',
            ),
        ]
        super(BRCellPhoneField, self).__init__(*args, **kwargs)


class BRZipCodeField(CharField):
    """
    A model field for the brazilian zip code
    """

    description = _("Zip Code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        kwargs['validators'] = [
            RegexValidator(
                regex='^[0-9]{5}[-]?[0-9]{3}$',
                message='CEP apenas com números ou no formato 00000-000',
                code='CEP inválido'
            ),
        ]
        super(BRZipCodeField, self).__init__(*args, **kwargs)
