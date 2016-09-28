from django.db import models

from .validators import egn_validator, eik_validator


class BGEGNField(models.CharField):
    """
    Field that stores Bulgarian unique citizenship number (EGN)

    This is shortcut for::

        models.CharField(max_length=10, validators=[localflavor.bg.validators.egn_validator])
    """
    default_validators = models.CharField.default_validators + [egn_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(BGEGNField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(BGEGNField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs


class BGEIKField(models.CharField):
    """
    Field that stores Bulgarian EIK/BULSTAT codes

    This is shortcut for::

        models.CharField(max_length=13, validators=[localflavor.bg.validators.eik_validator])
    """
    default_validators = models.CharField.default_validators + [eik_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        super(BGEIKField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(BGEIKField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs
