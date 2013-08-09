from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

from .br_states import STATE_CHOICES


class BRStateField(CharField):
    """
    A model field for states of Brazil
    """
    description = _("State of Brazil (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(BRStateField, self).__init__(*args, **kwargs)


class ZipCodeField(CharField):
    """
    A :class:`~django.db.models.CharField` that checks that the value
    is a valid BR-style Zip Code (in the format ``xxxxx-xxx``).
    """
    description = _("Zip Code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super(ZipCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from localflavor.br.forms import BRZipCodeField
        defaults = {'form_class': BRZipCodeField}
        defaults.update(kwargs)
        return super(ZipCodeField, self).formfield(**defaults)
