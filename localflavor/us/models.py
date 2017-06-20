from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.models import DeprecatedPhoneNumberField

from .forms import USPhoneNumberField as USPhoneNumberFormField
from .forms import USSocialSecurityNumberField as USSocialSecurityNumberFieldFormField
from .forms import USZipCodeField as USZipCodeFormField
from .us_states import STATE_CHOICES, USPS_CHOICES


class USStateField(CharField):
    """
    A model field that stores the two-letter U.S. state abbreviation in the database.

    Forms represent it as a ``forms.USStateField`` field.
    """

    description = _("U.S. state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(USStateField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(USStateField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class USPostalCodeField(CharField):
    """
    A model field that stores the two-letter U.S. Postal Service abbreviation in the database.

    Forms represent it as a :class:`~localflavor.us.forms.USPSSelect`` field.

    .. note::

        If you are looking for a model field that validates U.S. ZIP codes
        please use :class:`~localflavor.us.models.USZipCodeField`.
    """

    description = _("U.S. postal code (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = USPS_CHOICES
        kwargs['max_length'] = 2
        super(USPostalCodeField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(USPostalCodeField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class USZipCodeField(CharField):
    """
    A model field that stores the U.S. ZIP code in the database.

    Forms represent it as a :class:`~localflavor.us.forms.USZipCodeField` field.

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
        defaults = {'form_class': USZipCodeFormField}
        defaults.update(kwargs)
        return super(USZipCodeField, self).formfield(**defaults)


class PhoneNumberField(CharField, DeprecatedPhoneNumberField):
    """
    A :class:`~django.db.models.CharField` that checks that the value is a valid U.S.A.-style phone number.

    (in the format ``XXX-XXX-XXXX``).
    """

    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': USPhoneNumberFormField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)


class USSocialSecurityNumberField(CharField):
    """
    A model field that stores  the security number in the format ``XXX-XX-XXXX``.

    Forms represent it as ``forms.USSocialSecurityNumberField`` field.

    .. versionadded:: 1.1
    """

    description = _("Social security number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super(USSocialSecurityNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': USSocialSecurityNumberFieldFormField}
        defaults.update(kwargs)
        return super(USSocialSecurityNumberField, self).formfield(**defaults)
