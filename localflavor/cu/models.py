# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import CharField
from django.utils.translation import ugettext as _

from .choices import PROVINCE_CHOICES, REGION_CHOICES
from .forms import CUIdentityCardNumberField as CUIdentityCardNumberFormField
from .forms import CUPostalCodeField as CUPostalCodeFormField


class CURegionField(CharField):
    """
    A model field for the three-letter of the Cuban region abbreviation.

    Forms represent it as a ``forms.CURegionField``.

    .. versionadded:: 1.6
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
    A model field for the three-letter of the Cuban province abbreviation in the database.

    Forms represent it as a ``forms.CUProvinceField``.

    .. versionadded:: 1.6
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


class CUPostalCodeField(CharField):
    """
    A model field for the Cuban postal code.

    Forms represent it as a ``forms.CUPostalCodeField``.

    .. versionadded:: 1.6
    """

    description = _("Cuban postal code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super(CUPostalCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': CUPostalCodeFormField}
        defaults.update(kwargs)
        return super(CUPostalCodeField, self).formfield(**defaults)


class CUIdentityCardNumberField(CharField):
    """
    A model field for the Cuban identity card number.

    Forms represent it as a ``forms.CUIdentityCardNumberField``.

    .. versionadded:: 1.6
    """

    description = _("Cuban identity card number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super(CUIdentityCardNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': CUIdentityCardNumberFormField}
        defaults.update(kwargs)
        return super(CUIdentityCardNumberField, self).formfield(**defaults)
