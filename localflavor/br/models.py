from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

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
