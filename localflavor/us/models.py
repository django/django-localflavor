from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

from .us_states import STATE_CHOICES, USPS_CHOICES


class USStateField(CharField):
    description = _("U.S. state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(USStateField, self).__init__(*args, **kwargs)


class USPostalCodeField(CharField):
    description = _("U.S. postal code (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = USPS_CHOICES
        kwargs['max_length'] = 2
        super(USPostalCodeField, self).__init__(*args, **kwargs)


class PhoneNumberField(CharField):
    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from localflavor.us.forms import USPhoneNumberField
        defaults = {'form_class': USPhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)


# Add South introspection rules
try:
    from south.modelsinspector import add_introspection_rules
except:
    pass
else:
    add_introspection_rules([], ["^localflavor\.us\.models\.USStateField"])
    add_introspection_rules([], ["^localflavor\.us\.models\.USPostalCodeField"])
    add_introspection_rules([], ["^localflavor\.us\.models\.PhoneNumberField"])
    add_introspection_rules([], ["^localflavor\.us\.models\.USZipCodeField"])
