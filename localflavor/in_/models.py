from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

from .in_states import STATE_CHOICES


class INStateField(CharField):
    """
    A model field that stores the two-letter Indian state abbreviation in the database.

    Forms represent it as a ``forms.INStateField`` field.
    """

    description = _("Indian state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(INStateField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(INStateField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs
