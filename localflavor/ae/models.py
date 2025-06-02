"""UAE-specific Model helpers."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from .ae_emirates import EMIRATE_CHOICES
from .validators import UAEEmiratesIDValidator, UAEPostalCodeValidator, UAEPOBoxValidator


class UAEEmiratesIDField(models.CharField):
    """
    A model field for UAE Emirates ID numbers.

    Stores Emirates ID as a 15-digit string with format: 784-YYYY-NNNNNNN-N

    .. versionadded:: 5.1
    """

    description = _("UAE Emirates ID number")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 18)  # 15 digits + 3 dashes = 18 characters
        kwargs.setdefault('validators', []).append(UAEEmiratesIDValidator())
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from .forms import UAEEmiratesIDField
        defaults = {'form_class': UAEEmiratesIDField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class UAEEmirateField(models.CharField):
    """
    A model field for UAE Emirates.

    Stores emirate as a 2-character abbreviation (e.g., 'DU' for Dubai).

    .. versionadded:: 5.1
    """

    description = _("UAE Emirate")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 2)
        kwargs.setdefault('choices', EMIRATE_CHOICES)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from .forms import UAEEmirateField
        defaults = {'form_class': UAEEmirateField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class UAEPostalCodeField(models.CharField):
    """
    A model field for UAE postal codes.

    UAE doesn't use postal codes, but stores "00000" if required.

    .. versionadded:: 5.1
    """

    description = _("UAE postal code")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 5)
        kwargs.setdefault('validators', []).append(UAEPostalCodeValidator())
        kwargs.setdefault('blank', True)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from .forms import UAEPostalCodeField
        defaults = {'form_class': UAEPostalCodeField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class UAEPOBoxField(models.CharField):
    """
    A model field for UAE P.O. Box numbers.

    Stores P.O. Box numbers as strings (numeric only).

    .. versionadded:: 5.1
    """

    description = _("UAE P.O. Box number")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 10)
        kwargs.setdefault('validators', []).append(UAEPOBoxValidator())
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from .forms import UAEPOBoxField
        defaults = {'form_class': UAEPOBoxField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class UAETaxRegistrationNumberField(models.CharField):
    """
    A model field for UAE Tax Registration Numbers (TRN).

    Stores TRN as a 15-digit string for VAT purposes.

    .. versionadded:: 5.1
    """

    description = _("UAE Tax Registration Number")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 15)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from .forms import UAETaxRegistrationNumberField
        defaults = {'form_class': UAETaxRegistrationNumberField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
