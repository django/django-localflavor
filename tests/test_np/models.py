from django.db import models

from localflavor.np.models import (NPDistrictField , NPZoneField , NPProvinceField)

class NepalianPlace(models.Model):
    district = NPDistrictField(blank = True)
    zone = NPZoneField(blank = True)
    province = NPProvinceField(blank = True)
    