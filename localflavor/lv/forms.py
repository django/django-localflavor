from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, Select
from django.utils.translation import ugettext_lazy as _

from .lv_choices import MUNICIPALITY_CHOICES


zipcode = re.compile(r'^(LV\s?-\s?)?(?P<code>[1-5]\d{3})$', re.IGNORECASE)


class LVPostalCodeField(Field):
    """
    A form field that validates and normalizes Latvian postal codes.

    Latvian postal codes in following forms accepted:
        * XXXX
        * LV-XXXX
    """
    default_error_messages = {
        'invalid': _('Enter a postal code in the format XXXX or LV-XXXX.'),
    }

    def clean(self, value):
        value = super(LVPostalCodeField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        match = re.match(zipcode, value)
        if not match:
            raise ValidationError(self.error_messages['invalid'])

        return 'LV-' + match.group('code')


class LVMunicipalitySelect(Select):
    """A select field of Latvian municipalities."""

    def __init__(self, attrs=None):
        super(LVMunicipalitySelect, self).__init__(attrs, choices=MUNICIPALITY_CHOICES)
