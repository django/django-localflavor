"""Taiwan-specific Form helpers."""

from django.forms.fields import Select

from .tw_choices import TW_ADMINISTRATIVE_DIVISION_CHOICES

__all__ = (
    'TWAdministrativeDivisionSelect',
)


class TWAdministrativeDivisionSelect(Select):
    """
    A select widget providing the list of administrative divisions in Taiwan as choices.

    .. versionadded:: 5.1
    """

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=TW_ADMINISTRATIVE_DIVISION_CHOICES)
