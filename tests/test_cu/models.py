# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from localflavor.cu.models import (CUIdentityCardNumberField, CUPhoneNumberField, CUProvinceField, CURegionField,
                                   CUZipCodeField)


class CUSomebody(models.Model):
    province_1 = CUProvinceField()
    province_2 = CUProvinceField()
    region_1 = CURegionField()
    region_2 = CURegionField()
    zip_code = CUZipCodeField()
    id_number = CUIdentityCardNumberField()
    phone_number = CUPhoneNumberField()
