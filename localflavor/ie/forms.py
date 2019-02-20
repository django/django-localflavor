"""IE-specific Form helpers."""

from __future__ import unicode_literals

import re

from django.forms import ValidationError
from django.forms.fields import Select, CharField
from django.utils.translation import ugettext_lazy as _

from .ie_counties import IE_COUNTY_CHOICES


class IECountySelect(Select):
    """A Select widget that uses a list of Irish Counties as its choices."""

    def __init__(self, attrs=None):
        super(IECountySelect, self).__init__(attrs, choices=IE_COUNTY_CHOICES)


class EircodeField(CharField):
    """
    A form field that validates its input is a valid Eircode (Irish postcode).

    The value is uppercased and has the internal space removed, if any.
    """

    default_error_messages = {"invalid": _("Enter a valid Eircode.")}
    eircode_regex = re.compile(
        r"^(D6W|[AC-FHKNPRTV-Y][0-9]{2}) ?([AC-FHKNPRTV-Y0-9]{4})$"
    )

    def clean(self, value):
        value = super(EircodeField, self).clean(value)
        if value in self.empty_values:
            return self.empty_value
        eircode = value.upper().strip()
        if not self.eircode_regex.search(eircode):
            raise ValidationError(self.error_messages["invalid"])
        return eircode.replace(" ", "")
