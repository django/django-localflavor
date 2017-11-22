from __future__ import unicode_literals

import warnings

from django.db import models
from django.utils.translation import ugettext_lazy as _

from localflavor.deprecation import DeprecatedPhoneNumberField, RemovedInLocalflavor20Warning

from . import forms
from .nl_provinces import PROVINCE_CHOICES
from .validators import (NLBankAccountNumberFieldValidator, NLBSNFieldValidator, NLPhoneNumberFieldValidator,
                         NLSoFiNumberFieldValidator, NLZipCodeFieldValidator)


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
        if value:
            value = value.upper().replace(' ', '')
            if len(value) == 6:
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


class NLBSNField(models.CharField):
    """
    A Dutch social security number (BSN).

    This model field uses :class:`validators.NLBSNFieldValidator` for validation.

    .. versionadded:: 1.6
    """

    description = _('Dutch social security number (BSN)')

    validators = [NLBSNFieldValidator()]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 12)
        super(NLBSNField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.NLBSNFormField}
        defaults.update(kwargs)
        return super(NLBSNField, self).formfield(**defaults)


class NLSoFiNumberField(NLBSNField):
    """
    A Dutch social security number (SoFi).

    This model field uses :class:`validators.NLSoFiNumberFieldValidator` for validation.

    .. versionadded:: 1.3
    .. deprecated:: 1.6
        Use `NLBSNField` instead.
    """

    description = _('Dutch social security number (SoFi)')

    validators = [NLSoFiNumberFieldValidator()]

    def __init__(self, *args, **kwargs):
        warnings.warn('NLSoFiNumberField is deprecated. Please use NLBSNField instead.',
                      RemovedInLocalflavor20Warning)
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
    .. deprecated:: 1.4
        Use the django-phonenumber-field_ library instead.

    .. _django-phonenumber-field: https://github.com/stefanfoulis/django-phonenumber-field
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

    .. deprecated:: 1.6
        Use `localflavor.generic.models.IBANField` with included_countries=('nl') option instead.
        Note that a data migration is required to move the data from this field to a new IBANField:
        it needs to calculate check digits, add the bank identifier and zero-pad the bank number
        into a proper IBAN.
    """

    def __init__(self, *args, **kwargs):
        self.system_check_deprecated_details = {
            'msg': self.__class__.__name__ + ' is deprecated.',
            'hint': "Use `localflavor.generic.models.IBANField` with included_countries=('nl') option instead."
        }

        kwargs.setdefault('max_length', 10)
        super(NLBankAccountNumberField, self).__init__(*args, **kwargs)
        # Ensure that only the NLBankAccountNumberFieldValidator is set.
        self.validators = [NLBankAccountNumberFieldValidator()]
