from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

from .forms import MXCLABEField as MXCLABEFormField
from .forms import MXCURPField as MXCURPFormField
from .forms import MXRFCField as MXRFCFormField
from .forms import MXSocialSecurityNumberField as MXSocialSecurityNumberFormField
from .forms import MXZipCodeField as MXZipCodeFormField
from .mx_states import STATE_CHOICES


class MXStateField(CharField):
    """A model field that stores the three-letter Mexican state abbreviation in the database."""

    description = _("Mexico state (three uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 3
        super(MXStateField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(MXStateField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class MXZipCodeField(CharField):
    """A model field that forms represent as a forms.MXZipCodeField field and stores the five-digit Mexican zip code."""

    description = _("Mexico zip code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super(MXZipCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': MXZipCodeFormField}
        defaults.update(kwargs)
        return super(MXZipCodeField, self).formfield(**defaults)


class MXRFCField(CharField):
    """A model field that forms represent as a forms.MXRFCField field and stores the value of a valid Mexican RFC."""

    description = _("Mexican RFC")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        super(MXRFCField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': MXRFCFormField}
        defaults.update(kwargs)
        return super(MXRFCField, self).formfield(**defaults)


class MXCLABEField(CharField):
    """
    A model field that forms represent as a forms.MXCURPField field and stores the value of a valid Mexican CLABE.

    .. versionadded:: 1.4
    """

    description = _("Mexican CLABE")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        super(MXCLABEField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': MXCLABEFormField}
        defaults.update(kwargs)
        return super(MXCLABEField, self).formfield(**defaults)


class MXCURPField(CharField):
    """A model field that forms represent as a forms.MXCURPField field and stores the value of a valid Mexican CURP."""

    description = _("Mexican CURP")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        super(MXCURPField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': MXCURPFormField}
        defaults.update(kwargs)
        return super(MXCURPField, self).formfield(**defaults)


class MXSocialSecurityNumberField(CharField):
    """
    A model field that forms represent as a forms.MXSocialSecurityNumberField field.

    It stores the value of a valid Mexican Social Security Number.
    """

    description = _("Mexican Social Security Number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super(MXSocialSecurityNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': MXSocialSecurityNumberFormField}
        defaults.update(kwargs)
        return super(MXSocialSecurityNumberField, self).formfield(**defaults)
