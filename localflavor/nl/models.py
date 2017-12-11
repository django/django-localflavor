from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import forms
from .nl_provinces import PROVINCE_CHOICES
from .validators import NLBSNFieldValidator, NLZipCodeFieldValidator


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
