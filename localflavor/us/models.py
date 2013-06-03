from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

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
    A model field that forms represent as a ``forms.USPSSelect`` field
    and stores the two-letter U.S Postal Service abbreviation in the
    database.
    """
    description = _("U.S. postal code (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = USPS_CHOICES
        kwargs['max_length'] = 2
        super(USPostalCodeField, self).__init__(*args, **kwargs)


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
