from django.db import models

from localflavor.cu.models import CUIdentityCardNumberField, CUPostalCodeField, CUProvinceField, CURegionField


class CUSomebody(models.Model):
    province_1 = CUProvinceField()
    province_2 = CUProvinceField(blank=True)
    region_1 = CURegionField()
    region_2 = CURegionField(blank=True)
    postal_code = CUPostalCodeField()
    id_number = CUIdentityCardNumberField()
