from django.db.models import CharField
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

    def deconstruct(self):
        name, path, args, kwargs = super(PKStateField, self).deconstruct()
        del kwargs['choices']
        del kwargs['max_length']
        return name, path, args, kwargs


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

    def deconstruct(self):
        name, path, args, kwargs = super(PKPostCodeField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

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

    def deconstruct(self):
        name, path, args, kwargs = super(PKPhoneNumberField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.PKPhoneNumberField}
        defaults.update(kwargs)
        return super(PKPhoneNumberField, self).formfield(**defaults)
