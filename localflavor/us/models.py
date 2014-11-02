from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

from . import forms
from .us_states import STATE_CHOICES, USPS_CHOICES


class USStateField(CharField):
    """
    A model field that forms represent as a ``forms.USStateField`` field and
    stores the two-letter U.S. state abbreviation in the database.
    """
    description = _("U.S. state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(USStateField, self).__init__(*args, **kwargs)


class USPostalCodeField(CharField):
    """"
    A model field that forms represent as a
    :class:`~localflavor.us.forms.USPSSelect`` field and stores the two-letter
    U.S. Postal Service abbreviation in the database.

    .. note::

        If you are looking for a model field that validates U.S. ZIP codes
        please use :class:`~localflavor.us.models.USZipCodeField`.
    """
    description = _("U.S. postal code (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = USPS_CHOICES
        kwargs['max_length'] = 2
        super(USPostalCodeField, self).__init__(*args, **kwargs)


class USZipCodeField(CharField):
    """
    A model field that forms represent as a
    :class:`~localflavor.us.forms.USZipCodeField` field and stores the
    U.S. ZIP code in the database.

    .. note::

        If you are looking for a model field with a list of U.S. Postal Service
        locations please use :class:`~localflavor.us.models.USPostalCodeField`.

    .. versionadded:: 1.1

    """
    description = _("U.S. ZIP code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(USZipCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.USZipCodeField}
        defaults.update(kwargs)
        return super(USZipCodeField, self).formfield(**defaults)


class PhoneNumberField(CharField):
    """
    A :class:`~django.db.models.CharField` that checks that the value
    is a valid U.S.A.-style phone number (in the format ``XXX-XXX-XXXX``).
    """
    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from localflavor.us.forms import USPhoneNumberField
        defaults = {'form_class': USPhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)


class USSocialSecurityNumberField(CharField):
    """
    A model field that forms represent as ``forms.USSocialSecurityNumberField``
    and stores in the format ``XXX-XX-XXXX``.

    .. versionadded:: 1.1
    """
    description = _("Social security number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super(USSocialSecurityNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from localflavor.us.forms import (USSocialSecurityNumberField as
            USSocialSecurityNumberFieldFormField)
        defaults = {'form_class': USSocialSecurityNumberFieldFormField}
        defaults.update(kwargs)
        return super(USSocialSecurityNumberField, self).formfield(**defaults)
