from django.db import models

from localflavor.ua.models import UAPostalCodeField, UARegionField, UAVatNumberField


class UAFlavorTestModel(models.Model):
    postal_code = UAPostalCodeField()
    region = UARegionField()
    vat_number = UAVatNumberField()
