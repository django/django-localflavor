# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .choices import COMPANY_TYPES_CHOICES, REGION_CHOICES_2002_2015
from .validators import MDIDNOFieldValidator, MDLicensePlateValidator


class MDIDNOField(forms.CharField):
    """
    A form field for the Moldavian company identification number (IDNO).

    .. versionadded:: 2.1
    """

    default_validators = [MDIDNOFieldValidator()]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        super(MDIDNOField, self).__init__(*args, **kwargs)


class MDLicensePlateField(forms.CharField):
    """
    A form field for the Moldavian license plate number.

    .. versionadded:: 2.1
    """

    default_validators = [MDLicensePlateValidator()]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        super(MDLicensePlateField, self).__init__(*args, **kwargs)


class MDCompanyTypesSelect(forms.Select):
    """
    A Select widget that uses a list of Moldavian company types as its choices.

    .. versionadded:: 2.1
    """

    def __init__(self, attrs=None):
        super(MDCompanyTypesSelect, self).__init__(attrs, choices=COMPANY_TYPES_CHOICES)


class MDRegionSelect(forms.Select):
    """
    A Select widget that uses a list of Moldavian regions as its choices.

    .. versionadded:: 2.1
    """

    def __init__(self, attrs=None):
        super(MDRegionSelect, self).__init__(attrs, choices=REGION_CHOICES_2002_2015)
