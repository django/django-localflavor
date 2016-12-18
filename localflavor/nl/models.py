from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.models import DeprecatedPhoneNumberField
from . import forms
from .nl_provinces import PROVINCE_CHOICES
from .validators import (NLBankAccountNumberFieldValidator, NLPhoneNumberFieldValidator,
                         NLSoFiNumberFieldValidator,
                         NLZipCodeFieldValidator)


class NLZipCodeField(models.CharField):
    """
    A Dutch zip code model field.

    This model field uses :class:`validators.NLZipCodeFieldValidator` for validation.

    .. versionadded:: 1.3
    """

    description = _('Dutch zipcode')

    validators = [NLZipCodeFieldValidator()]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        super(NLZipCodeField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(NLZipCodeField, self).to_python(value)
        if value is not None:
            value = value.upper().replace(' ', '')
            return '%s %s' % (value[:4], value[4:])
        return value

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.NLZipCodeField}
        defaults.update(kwargs)
        return super(NLZipCodeField, self).formfield(**defaults)


class NLProvinceField(models.CharField):
    """
    A Dutch Province field.

    .. versionadded:: 1.3
    """

    description = _('Dutch province')

    def __init__(self, *args, **kwargs):
        kwargs.update({
            'choices': PROVINCE_CHOICES,
            'max_length': 3
        })
        super(NLProvinceField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(NLProvinceField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class NLSoFiNumberField(models.CharField):
    """
    A Dutch social security number (SoFi).

    This model field uses :class:`validators.NLSoFiNumberFieldValidator` for validation.

    .. versionadded:: 1.3
    """

    description = _('Dutch social security number (SoFi)')

    validators = [NLSoFiNumberFieldValidator()]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 12)
        super(NLSoFiNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.NLSoFiNumberField}
        defaults.update(kwargs)
        return super(NLSoFiNumberField, self).formfield(**defaults)


class NLPhoneNumberField(models.CharField, DeprecatedPhoneNumberField):
    """
    Dutch phone number model field.

    This model field uses :class:`validators.NLPhoneNumberFieldValidator` for validation.

    .. versionadded:: 1.3
    """

    description = _('Dutch phone number')

    validator = [NLPhoneNumberFieldValidator()]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 12)
        super(NLPhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.NLPhoneNumberField}
        defaults.update(kwargs)
        return super(NLPhoneNumberField, self).formfield(**defaults)


class NLBankAccountNumberField(models.CharField):
    """
    A Dutch bank account model field.

    This model field uses :class:`validators.NLBankAccountNumberFieldValidator` for validation.

    .. versionadded:: 1.1
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 10)
        super(NLBankAccountNumberField, self).__init__(*args, **kwargs)
        # Ensure that only the NLBankAccountNumberFieldValidator is set.
        self.validators = [NLBankAccountNumberFieldValidator()]
