from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

from . import forms
from .au_states import STATE_CHOICES
from .validators import AUBusinessNumberFieldValidator, AUCompanyNumberFieldValidator, AUTaxFileNumberFieldValidator


class AUStateField(CharField):
    """
    A model field that stores the three-letter Australian state abbreviation in the database.

    It is represented with :data:`~localflavor.au.au_states.STATE_CHOICES`` choices.
    """

    description = _("Australian State")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 3
        super(AUStateField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(AUStateField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class AUPostCodeField(CharField):
    """
    A model field that stores the four-digit Australian postcode in the database.

    This field is represented by forms as a :class:`~localflavor.au.forms.AUPostCodeField` field.
    """

    description = _("Australian Postcode")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 4
        super(AUPostCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.AUPostCodeField}
        defaults.update(kwargs)
        return super(AUPostCodeField, self).formfield(**defaults)


class AUBusinessNumberField(CharField):
    """
    A model field that checks that the value is a valid Australian Business Number (ABN).

    .. versionadded:: 1.3
    """

    description = _("Australian Business Number")

    validators = [AUBusinessNumberFieldValidator()]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super(AUBusinessNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.AUBusinessNumberField}
        defaults.update(kwargs)
        return super(AUBusinessNumberField, self).formfield(**defaults)

    def to_python(self, value):
        """Ensure the ABN is stored without spaces."""
        value = super(AUBusinessNumberField, self).to_python(value)

        if value is not None:
            return ''.join(value.split())

        return value


class AUCompanyNumberField(CharField):
    """
    A model field that checks that the value is a valid Australian Company Number (ACN).

    .. versionadded:: 1.5
    """

    description = _("Australian Company Number")

    validators = [AUCompanyNumberFieldValidator()]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super(AUCompanyNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.AUCompanyNumberField}
        defaults.update(kwargs)
        return super(AUCompanyNumberField, self).formfield(**defaults)

    def to_python(self, value):
        """Ensure the ACN is stored without spaces."""
        value = super(AUCompanyNumberField, self).to_python(value)

        if value is not None:
            return ''.join(value.split())

        return value


class AUTaxFileNumberField(CharField):
    """
    A model field that checks that the value is a valid Tax File Number (TFN).

    A TFN is a number issued to a person by the Commissioner of Taxation and
    is used to verify client identity and establish their income levels.
    It is a eight or nine digit number without any embedded meaning.

    .. versionadded:: 1.4
    """

    description = _("Australian Tax File Number")

    validators = [AUTaxFileNumberFieldValidator()]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super(AUTaxFileNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.AUTaxFileNumberField}
        defaults.update(kwargs)
        return super(AUTaxFileNumberField, self).formfield(**defaults)

    def to_python(self, value):
        """Ensure the TFN is stored without spaces."""
        value = super(AUTaxFileNumberField, self).to_python(value)

        if value is not None:
            return ''.join(value.split())

        return value
