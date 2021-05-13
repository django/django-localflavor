import warnings

from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from .in_states import STATE_CHOICES


class INStateField(CharField):
    """
    A model field that stores the two-letter Indian state abbreviation in the database.

    Forms represent it as a ``forms.INStateField`` field.
    """

    description = _("Indian state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        warnings.warn("Choices have changed for INStateField in localflavor 3.1. See changelog for details.")
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs
