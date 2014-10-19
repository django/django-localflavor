from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField


class FRSIRENField(CharField):
    """
    A :class:`~django.db.models.CharField` that checks that the value
    is a valid French SIREN number
    """
    description = _("SIREN Number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super(FRSIRENField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from localflavor.fr.forms import (FRSIRENField as
                                          FRSIRENFormField)
        defaults = {'form_class': FRSIRENFormField}
        defaults.update(kwargs)
        return super(FRSIRENField, self).formfield(**defaults)


class FRSIRETField(CharField):
    """
    A :class:`~django.db.models.CharField` that checks that the value
    is a valid French SIRET number
    """
    description = _("SIRET Number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        super(FRSIRETField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from localflavor.fr.forms import (FRSIRETField as
                                          FRSIRETFormField)
        defaults = {'form_class': FRSIRETFormField}
        defaults.update(kwargs)
        return super(FRSIRETField, self).formfield(**defaults)
