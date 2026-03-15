from django.db import models
from django.utils.translation import gettext_lazy as _

from .qa_municipalities import MUNICIPALITY_CHOICES
from .validators import QANationalIDValidator


class QANationalIDField(models.CharField):
    """
    A model field for Qatari National ID numbers.

    .. versionadded:: 5.1
    """

    description = _('Qatari National ID number')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 11)
        super().__init__(*args, **kwargs)
        self.validators.append(QANationalIDValidator()) 

    def formfield(self, **kwargs):
        from .forms import QANationalIDNumberField
        defaults = {'form_class': QANationalIDNumberField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class QAMunicipalityField(models.CharField):
    """
    A model field for Qatar municipalities.

    Stores the municipality as a 2-character ISO 3166-2:QA code
    (e.g. ``'DA'`` for Ad Dawhah / Doha).

    .. versionadded:: 5.1
    """

    description = _('Qatar municipality')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 2)
        kwargs.setdefault('choices', MUNICIPALITY_CHOICES)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from .forms import QAMunicipalityField as QAMunicipalityFormField
        defaults = {'choices_form_class': QAMunicipalityFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs
