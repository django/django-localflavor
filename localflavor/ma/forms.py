"""MA-specific Form helpers"""
from django.forms.fields import CharField, RegexField, Select
from django.utils.translation import gettext_lazy as _

from .ma_provinces import PROVINCE_CHOICES_PER_REGION
from .ma_regions import REGION_CHOICES


class MAPostalCodeField(RegexField):
    """
    Validate local Moroccan postal code.

    The correct format is 'XXXXX' as defined in http://codepostal.ma/code_postal.aspx .

    .. versionadded:: 1.4
    """

    default_error_messages = {
        'invalid': _('Enter a postal code in the format XXXXX.'),
    }

    def __init__(self, **kwargs):
        kwargs.setdefault('label', _('Postal code'))
        kwargs['max_length'] = 5
        kwargs['min_length'] = 5
        super().__init__(r'^\d{5}$', **kwargs)


class MAProvinceSelect(Select):
    """A Select widget that uses a list of MA provinces as its choices."""

    def __init__(self, attrs=None):
        choices = [
            (province[0], '%s - %s' % (province[0], province[1]))
            for province in PROVINCE_CHOICES_PER_REGION
        ]
        super().__init__(attrs, choices=choices)


class MARegionSelect(Select):
    """A Select widget that uses a list of MA regions as its choices."""

    def __init__(self, attrs=None):
        choices = [
            (region[0], '%s - %s' % (region[0], region[1]))
            for region in REGION_CHOICES
        ]
        super().__init__(attrs, choices=choices)


class MAProvinceField(CharField):
    """
    A Select Field that uses a MAProvinceSelect widget.

    .. versionadded:: 1.4
    """

    widget = MAProvinceSelect

    def __init__(self, **kwargs):
        kwargs.setdefault('label', _('Select Province'))
        super().__init__(**kwargs)


class MARegionField(CharField):
    """
    A Select Field that uses a MARegionSelect widget.

    .. versionadded:: 1.4
    """

    widget = MARegionSelect

    def __init__(self, **kwargs):
        kwargs.setdefault('label', _('Select Region'))
        super().__init__(**kwargs)
