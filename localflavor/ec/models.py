from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

from .ec_provinces import PROVINCE_CHOICES


class ECProvinceField(CharField):
    """
    A model field that represents an Ecuadorian province and stores its
    abbreviation.

    .. versionadded:: 1.2
    """
    description = _("Ecuadorian province")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = PROVINCE_CHOICES
        kwargs['max_length'] = 2
        super(ECProvinceField, self).__init__(*args, **kwargs)
