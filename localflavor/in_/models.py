import re
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .in_states import STATE_CHOICES
from .forms import INPANCardNumberFormField

class INStateField(models.CharField):
    """
    A model field that stores the two-letter Indian state abbreviation in the database.

    Forms represent it as a ``forms.INStateField`` field.
    """

    description = _("Indian state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs

class INPANCardNumberValidator(RegexValidator):
    """
    A validator for Indian Permanent Account Number(PAN) Card field.

    Rules:
        It should be ten characters long.
        The first five characters should be any upper case alphabets.
        The next four-characters should be any number from 0 to 9.
        The last(tenth) character should be any upper case alphabet.
    """
    default_error_messages = {
        'invalid': _('Please enter a valid Indian PAN card number.'),
    }

    def __init__(self,*args, **kwargs):
        super().__init__(regex = re.compile('[A-Z]{5}[0-9]{4}[A-Z]{1}'), *args,**kwargs)

class INPANCardNumberField(models.CharField):
    """
        A model field that accepts indian PAN Card number.
        Source: https://en.wikipedia.org/wiki/Permanent_account_number
        .. versionadded:: 4.0
    """
    description = _("PAN Card number field")
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super().__init__(*args, **kwargs)
        self.validators.append(INPANCardNumberValidator())

    def formfield(self, **kwargs):
        defaults = {'form_class': INPANCardNumberFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)