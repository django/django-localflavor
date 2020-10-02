from django import forms
from django.utils.translation import ugettext_lazy as _

from .by_regions import BY_REGIONS_CHOICES


class BaseKwargsUpdatedField:
    """
    Abstract base class made to conform the DRY principle.

    The initial_options is overrided by the dict in the subclasses and then
    automatically passed to kwargs in the FormField.__init__() method.
    """

    initial_options = None

    def __init__(self, *args, **kwargs):
        kwargs.update(self.initial_options)
        super().__init__(*args, **kwargs)


class UpperValueMixin:
    """
    Mixin made to conform the DRY principle.

    Overrides the to_python methods to return the value.upper()
    """

    def to_python(self, value):
        value = super().to_python(value)
        if value is None:
            return value
        else:
            return value.upper()


class BYRegionField(BaseKwargsUpdatedField, forms.TypedChoiceField):
    """
    A form field that ensures the input is a number representing the region.
    """

    initial_options = {
        'choices': BY_REGIONS_CHOICES,
        'empty_value': None
    }


class BYPassNumberField(BaseKwargsUpdatedField, UpperValueMixin, forms.RegexField):
    """
    A form field that validates its input is a pass number in a right format.

    Apart from that, it tries to convert all characters to uppercase as
    the format of belarussian pass number needs that to be right.

    The valid input format is: XX1234567.
    """

    initial_options = {
        'regex': r'[A-Z]{2}\d{7}',
        'max_length': 9,
        'error_messages': {
            'invalid': _('Passport number format is: XX1234567')
        },
        'empty_value': None,
    }


class BYPassIdNumberField(BaseKwargsUpdatedField, UpperValueMixin, forms.RegexField):
    """
    A form field that validates its input is a ID number in a right format.

    Apart from that, it tries to convert all characters of the input
    to uppercase as the format of belarussian pass id needs those
    to be valid.

    The valid input format is: 1234567X123XX1.
    """

    initial_options = {
        'regex': r'\d{7}[A-Z]\d{3}[A-Z]{2}\d',
        'max_length': 14,
        'error_messages': {
            'invalid': _('ID format is: 1234567X123XX1')
        },
        'empty_value': None
    }


class ByPostalCodeField(BaseKwargsUpdatedField, forms.CharField):
    """
    A form field that validates its input is a valid Postal code (6 digits).
    """

    initial_options = {
        'max_length': 6,
        'min_length': 6,
        'empty_value': None,
        'error_messages': {
            'max_length': _('Postal code length must not be more than 6 digits.'),
            'min_length': _('Postal code length must not be less than 6 digits.')
        }
    }
