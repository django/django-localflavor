from django.db import models

from localflavor.lk.models import (LKDistrictField, LKProvinceField)


class LKPlace(models.Model):
    district = LKDistrictField(blank=True)
    province = LKProvinceField(blank=True)
