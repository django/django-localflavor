from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _

from . import forms
from .pk_states import STATE_CHOICES


class PKStateField(CharField):
    """
    A model field that is represented with
    :data:`~localflavor.pk.pk_states.STATE_CHOICES`` choices and
    stores the five-letter Pakistani state abbreviation in the database.
    """
    description = _("Pakistani State")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 5
        super(PKStateField, self).__init__(*args, **kwargs)


class PKPostCodeField(CharField):
    """
    A model field that forms represent as a
    :class:`~localflavor.pk.forms.PKPostCodeField` field and stores the
    five-digit Pakistani postcode in the database.
    """
    description = _("Pakistani Postcode")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super(PKPostCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.PKPostCodeField}
        defaults.update(kwargs)
        return super(PKPostCodeField, self).formfield(**defaults)


class PKPhoneNumberField(CharField):
    """
    A model field that checks that the value is a valid Pakistani phone
    number (nine to eleven digits).
    """
    description = _("Pakistani Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(PKPhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.PKPhoneNumberField}
        defaults.update(kwargs)
        return super(PKPhoneNumberField, self).formfield(**defaults)
