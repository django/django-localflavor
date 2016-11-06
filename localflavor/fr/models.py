from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _


class FRSIRENField(CharField):
    """
    A :class:`~django.db.models.CharField` that checks that the value is a valid French SIREN number.

    .. versionadded:: 1.1
    """

    description = _("SIREN Number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super(FRSIRENField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from . import forms
        defaults = {'form_class': forms.FRSIRENField}
        defaults.update(kwargs)
        return super(FRSIRENField, self).formfield(**defaults)


class FRSIRETField(CharField):
    """
    A :class:`~django.db.models.CharField` that checks that the value is a valid French SIRET number.

    .. versionadded:: 1.1
    """

    description = _("SIRET Number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        super(FRSIRETField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from . import forms
        defaults = {'form_class': forms.FRSIRETField}
        defaults.update(kwargs)
        return super(FRSIRETField, self).formfield(**defaults)
