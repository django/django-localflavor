from django.db import models

from localflavor.nl.models import NLBSNField, NLProvinceField, NLZipCodeField


class NLPlace(models.Model):

    zipcode = NLZipCodeField()
    province = NLProvinceField(default='ZH')
    bsn = NLBSNField()

    class Meta:
        app_label = 'test_nl'
