from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField
from django.core.validators import RegexValidator

from .br_states import STATE_CHOICES


class BRStateField(CharField):
    """
    A model field for states of Brazil
    """
    description = _("State of Brazil (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(BRStateField, self).__init__(*args, **kwargs)


class BRCPFField(CharField):
    """
    A model field for the brazilian document named of CPF (Cadastro de Pessoa Física)
    """

    description = _("CPF with 11 numbers")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        kwargs['validators'] = [
            RegexValidator(
                regex='^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$',
                message='CPF apenas com números, ou no formato 000.000.000-00',
                code='CPF inválido',
            ),
        ]
        super(BRCPFField, self).__init__(*args, **kwargs)

