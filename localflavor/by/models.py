from django.core.validators import RegexValidator
from django.db.models import CharField, IntegerField
from django.utils.translation import ugettext_lazy as _

from .by_regions import BY_REGIONS_CHOICES
from .validators import RangeValidator


class BYRegionField(IntegerField):
    '''
    A model field that stores the numeric value of regions in Belarus.

    The data is represented in ``by_regions.BY_REGIONS_CHOICES``.

    Form represent it as a 
    '''

    description = _('Belarus Regions (one integer value in range 1-7).')

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = BY_REGIONS_CHOICES
        kwargs['validators'] = (
            RangeValidator(
                (1, 8), message=_('The value must be at least 1 and at most 7')
            )
        )
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        del kwargs['validators']
        return name, path, args, kwargs

    
class BYPassNumberField(CharField):
    '''
    A model field that stores the number of Belarus passport.
    
    Form represent it as ...
    '''

    description = _('Belarus passport number (2 letters followed by 7 digits')

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        kwargs['validators'] = (
            RegexValidator(
            r'[A-Z]{2}[1-9]{7}',
            message=_('Passport number format is: XX1234567')
        )
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        del kwargs['validators']
        return name, path, args, kwargs


class BYPassIdNumberField(CharField):
    '''
    A model field that stores the ID number.

    Form represents it as ...
    '''

    description = _('Belarus passport ID number (14 digits and numbers).')

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        kwargs['validators'] = (
            RegexValidator(
                r'',
                message=_()
            )
        )
