from django.core.exceptions import ValidationError
from django.forms.fields import CharField, ChoiceField
from django.utils.translation import gettext_lazy as _

from .qa_municipalities import MUNICIPALITY_CHOICES, resolve_municipality
from .validators import QANationalIDValidator


class QANationalIDNumberField(CharField):
    """
    A form field for validating Qatari National ID numbers.

    .. versionadded:: 5.1
    """

    default_error_messages = {
        'invalid': _('Enter a valid Qatari National ID number'),
    }

    def __init__(self, max_length=11, min_length=11, **kwargs):
        super().__init__(max_length=max_length, min_length=min_length, **kwargs)
        self.validators.append(
            QANationalIDValidator(self.error_messages['invalid'])
        )  


class QAMunicipalityField(ChoiceField):
    """
    A choice field for Qatar municipalities.

    The field accepts both the 2-letter ISO 3166-2:QA abbreviation (e.g. ``'DA'``), 
    common English names and Arabic names, and always returns the abbreviation.

    .. versionadded:: 5.1
    """

    def __init__(self, **kwargs):
        kwargs.pop('coerce', None)
        kwargs.pop('empty_value', None)
        kwargs.setdefault('choices', MUNICIPALITY_CHOICES)
        super().__init__(**kwargs)

    def clean(self, value):
        if value in self.empty_values:
            return super().clean(value)

        normalized_value = resolve_municipality(str(value))
        if not normalized_value:
            raise ValidationError(
                self.error_messages['invalid_choice'],
                code='invalid_choice',
                params={'value': value},
            )

        return super().clean(normalized_value)
