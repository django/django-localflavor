from typing import Any
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from .forms import (
    KENationalIDNumberField,
    KEKRAPINField,
    KENHIFNumberField,
    KENSSFNumberField,
    KEPassportNumberField,
    KEPostalCodeField as KEPostalCodeFormField,
)


class KEPostalCodeField(CharField):
    """
    A model field that stores the Kenyan Postal Codes
    """
    description = _("Kenya Postal Code")

    def __init__(self, *args, **kwargs) -> None:
        kwargs.update(max_length=8)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs) -> Any:
        defaults = {"form_class": KEPostalCodeFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

        
        