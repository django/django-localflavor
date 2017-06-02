# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import CharField
from django.utils.translation import ugettext as _

from .choices import PROVINCE_CHOICES, REGION_CHOICES
from .forms import (
    CUZipCodeField as CUZipCodeFormField,
    CUIdentityCardNumberField as CUIdentityCardNumberFormField,
    CUPhoneNumberField as CUPhoneNumberFormField
)


class CURegionField(CharField):
    """
    A model field for the three-letter of the cuban region abbreviation.

    Forms represent it as a ``forms.CURegionField``.
    """

    description = _("Cuban regions (three uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = REGION_CHOICES
        kwargs['max_length'] = 3
        super(CURegionField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CURegionField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class CUProvinceField(CharField):
    """
    A model field for the three-letter of the cuban province abbreviation in the database.

    Forms represent it as a ``forms.CUProvinceField``.
    """

    description = _("Cuban provinces (three uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = PROVINCE_CHOICES
        kwargs['max_length'] = 3
        super(CUProvinceField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CUProvinceField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class CUZipCodeField(CharField):
    """
    A model field for the cuban ZIP code.

    Forms represent it as a ``forms.CUZipCodeField``.
    """

    description = _("Cuban ZIP code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super(CUZipCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': CUZipCodeFormField}
        defaults.update(kwargs)
        return super(CUZipCodeField, self).formfield(**defaults)


class CUIdentityCardNumberField(CharField):
    """
    A model field for the cuban identity card number.

    Forms represent it as a ``forms.CUIdentityCardNumberField``.
    """

    description = _("Cuban identity card number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super(CUIdentityCardNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': CUIdentityCardNumberFormField}
        defaults.update(kwargs)
        return super(CUIdentityCardNumberField, self).formfield(**defaults)


class CUPhoneNumberField(CharField):
    """
    A model field for the cuban phone number.

    Forms represent it as a ``forms.CUIdentityCardNumberField``.
    """

    description = _("Cuban phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 8
        super(CUPhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': CUPhoneNumberFormField}
        defaults.update(kwargs)
        return super(CUPhoneNumberField, self).formfield(**defaults)
