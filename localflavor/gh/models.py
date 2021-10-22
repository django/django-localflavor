"""Ghana specific Model fields"""

import re
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .forms import GHPostalCodeFormField
from .gh_regions import REGIONS


class GHPostalCodeValidator(RegexValidator):
    """
    A validator for Ghana Postal Codes.
    """
    default_error_messages = {
        'invalid': _('Enter a postal code in format XXXXX'),
    }

    def __init__(self,*args, **kwargs):
        super().__init__(re.compile(r'^\d{5}$'), *args,**kwargs)

class GHPostalCodeField(models.CharField):
    """
        A model field that accepts Ghana postal codes.
        Format: XXXXX
        Source: https://yen.com.gh/139831-ghana-zip-code-number-list-post-tracking.html
        .. versionadded:: 4.0
    """
    description = _("Postal Code")
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super().__init__(*args, **kwargs)
        self.validators.append(GHPostalCodeValidator())

    def formfield(self, **kwargs):
        defaults = {'form_class': GHPostalCodeFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class GHRegionField(models.CharField):
    """
        A model field that provides an option to select 
        a region from the list of all Ghana regions.
        .. versionadded:: 4.0
    """

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = REGIONS
        kwargs['max_length'] = 13
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs