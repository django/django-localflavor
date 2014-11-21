# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .se_counties import COUNTY_CHOICES, NUMERICAL_COUNTY_CODE_CHOICES, FULL_COUNTY_NAME_CHOICES


class SECountyField(models.CharField):
    """
    A standard `CharField` with `choices` defaulting to `localflavor.se.se_counties.COUNTY_CHOICES`.

    As the Swedish counties can be named in at least two ways (e.g. "Stockholm" vs. "Stockholm County"),
    and there has historically been at least two numeric systems used for counties, this field adds the
    following accessors to let you access all of this data:

    * `get_county_numerical_code()` - Numiercal code (01-25)
    * `get_county_full_name()` - Full Name (e.g. Stockholm County)
    * `get_county_short_name()`- Short name (e.g. Stockholm)

    Example:

    .. code-block:: python

        from django.db import models
        from localflavor.se.models import SECountyField
        from .se_counties import COUNTY_CHOICES, NUMERICAL_COUNTY_CODE_CHOICES, FULL_COUNTY_NAME_CHOICES

        class MyModel(models.Model):
            county = SECountyField()

        obj = MyModel(county='AB')

        obj.get_county_numerical_code() # '01'
        obj.get_county_full_name()      # 'Stockholm County'
        obj.get_county_short_name()     # 'Stockholm'
        obj.get_county_display()        # 'Stockholm'
        obj.county                      # 'AB'

    https://sv.wikipedia.org/wiki/Sveriges_län
    https://en.wikipedia.org/wiki/Counties_of_Sweden
    """
    description = _('A Swedish County')

    def __init__(self, *args, **kwargs):

        if not 'choices' in kwargs:
            kwargs['choices'] = COUNTY_CHOICES

        if not 'max_length' in kwargs:
            kwargs['max_length'] = 2

        super(SECountyField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        if not cls._meta.abstract:
            _get_numerical_code = lambda self: dict(NUMERICAL_COUNTY_CODE_CHOICES).get(getattr(self, name), None)
            _get_full_name = lambda self: dict(FULL_COUNTY_NAME_CHOICES).get(getattr(self, name), None)
            _get_short_name = lambda self: dict(COUNTY_CHOICES).get(getattr(self, name), None)

            cls.add_to_class("get_" + name + "_numerical_code", _get_numerical_code)
            cls.add_to_class("get_" + name + "_full_name", _get_full_name)
            cls.add_to_class("get_" + name + "_short_name", _get_short_name)

        super(SECountyField, self).contribute_to_class(cls, name)
