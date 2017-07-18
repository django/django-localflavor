from django.db import models

from localflavor.ec.models import ECProvinceField


class ECPlace(models.Model):
    province = ECProvinceField(blank=True)
