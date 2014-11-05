from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _

from . import forms
from .au_states import STATE_CHOICES


class AUStateField(CharField):
    """
    A model field that is represented with
    :data:`~localflavor.au.au_states.STATE_CHOICES`` choices and
    stores the three-letter Australian state abbreviation in the database.
    """
    description = _("Australian State")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 3
        super(AUStateField, self).__init__(*args, **kwargs)


class AUPostCodeField(CharField):
    """
    A model field that forms represent as a
    :class:`~localflavor.au.forms.AUPostCodeField` field and stores the
    four-digit Australian postcode in the database.
    """
    description = _("Australian Postcode")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 4
        super(AUPostCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.AUPostCodeField}
        defaults.update(kwargs)
        return super(AUPostCodeField, self).formfield(**defaults)


class AUPhoneNumberField(CharField):
    """
    A model field that checks that the value is a valid Australian phone
    number (ten digits).
    """
    description = _("Australian Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(AUPhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.AUPhoneNumberField}
        defaults.update(kwargs)
        return super(AUPhoneNumberField, self).formfield(**defaults)
