"""Nepal specific Model fields"""

import re
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .forms import PostalCodeFormField
from .np_zones import ZONES
from .np_provinces import PROVINCES
from .np_districts import ALL_DISTRICTS

class PostalCodeValidator(RegexValidator):
    """
    A validator for Nepali Postal Codes.
    """
    default_error_messages = {
        'invalid': _('Enter a postal code in format XXXXX'),
    }

    def __init__(self,*args, **kwargs):
        super().__init__(re.compile(r'^\d{5}$'), *args,**kwargs)

class PostalCodeField(models.CharField):
    """
        A modelfield which accepts a Nepali postal code of length five.
        Format: XXXXX
        Source: https://en.wikipedia.org/wiki/List_of_postal_codes_in_Nepal
    """
    description = _("Postal Code")
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super().__init__(*args, **kwargs)
        self.validators.append(PostalCodeValidator())

    def formfield(self, **kwargs):
        defaults = {'form_class': PostalCodeFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

class NPDistrictField(models.CharField):
    """
        A Modelfield which provides an option to select 
        a district from the list of all Nepali districts
    """

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = ALL_DISTRICTS
        kwargs['max_length'] = 255
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs
        
class NPZoneField(models.CharField):
    """
        A Modelfield which provides an option to select 
        a zone from the list of all Nepali zones.
    """

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = ZONES
        kwargs['max_length'] = 255
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs

class NPProvinceField(models.CharField):
    """
        A Modelfield which provides an option to select 
        a province from the list of all Nepali provinces
    """

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = PROVINCES
        kwargs['max_length'] = 255
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs