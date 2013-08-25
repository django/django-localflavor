from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

from .in_states import STATE_CHOICES


class INStateField(CharField):
    """
    A model field that forms represent as a ``forms.INStateField`` field and
    stores the two-letter Indian state abbreviation in the database.
    """
    description = _("Indian state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(INStateField, self).__init__(*args, **kwargs)
