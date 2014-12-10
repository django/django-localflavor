from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

from . import forms
from .nys_detail import NYS_COUNTY_CHOICES


class NYSCountyField(CharField):
    """
    A model field that forms represent as a ``forms.NYSCountyField`` field and
    stores the three-digit county code.
    """
    description = _("New York State County Three-Digit Codes")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = NYS_COUNTY_CHOICES
        kwargs['max_length'] = 3
        super(NYSCountyField, self).__init__(*args, **kwargs)
