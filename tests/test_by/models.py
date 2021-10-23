from django.db import models

from localflavor.by import models as md


class BYTestModel(models.Model):
    region = md.BYRegionField(null=True, blank=True)
    pass_num = md.BYPassNumberField(null=True, blank=True)
    pass_id = md.BYPassIdNumberField(null=True, blank=True)
    postal_code = md.BYPostalCodeField(null=True, blank=True)
