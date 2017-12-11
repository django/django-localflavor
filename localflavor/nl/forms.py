# -*- coding: utf-8 -*-
"""NL-specific Form helpers."""

from __future__ import unicode_literals

from django import forms
from django.utils import six

from .nl_provinces import PROVINCE_CHOICES
from .validators import NLBSNFieldValidator, NLZipCodeFieldValidator


class NLZipCodeField(forms.CharField):
    """A Dutch zip code field."""

    default_validators = [NLZipCodeFieldValidator()]

    def clean(self, value):
        if isinstance(value, six.string_types):
            value = value.upper().replace(' ', '')

            if len(value) == 6:
                value = '%s %s' % (value[:4], value[4:])

        return super(NLZipCodeField, self).clean(value)


class NLProvinceSelect(forms.Select):
    """A Select widget that uses a list of provinces of the Netherlands as it's choices."""

    def __init__(self, attrs=None):
        super(NLProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)


class NLBSNFormField(forms.CharField):
    """
    A Dutch social security number (BSN) field.

    http://nl.wikipedia.org/wiki/Sofinummer

    .. versionadded:: 1.6
    """

    default_validators = [NLBSNFieldValidator()]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super(NLBSNFormField, self).__init__(*args, **kwargs)
