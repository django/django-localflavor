from django.db import models

from localflavor.nl.models import NLBSNField, NLLicensePlateField, NLProvinceField, NLZipCodeField


class NLPlace(models.Model):

    zipcode = NLZipCodeField()
    province = NLProvinceField(default='ZH')
    bsn = NLBSNField()

    class Meta:
        app_label = 'test_nl'


class NLCar(models.Model):

    license_plate = NLLicensePlateField()

    class Meta:
        app_label = 'test_nl'
