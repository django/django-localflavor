from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

from .ec_provinces import PROVINCE_CHOICES


class ECProvinceField(CharField):
    """
    A model field that represents an Ecuadorian province and stores its abbreviation.

    .. versionadded:: 1.2
    """

    description = _("Ecuadorian province")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = PROVINCE_CHOICES
        kwargs['max_length'] = 2
        super(ECProvinceField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ECProvinceField, self).deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs
