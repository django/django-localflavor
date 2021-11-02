from django.db import models

from localflavor.np.models import (NPPostalCodeField , NPDistrictField , NPZoneField , NPProvinceField)

class NepalianPlace(models.Model):
    postal = NPPostalCodeField(blank = True)
    district = NPDistrictField(blank = True)
    zone = NPZoneField(blank = True)
    province = NPProvinceField(blank = True)
    