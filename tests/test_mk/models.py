from django.db import models

from localflavor.mk.models import MKIdentityCardNumberField, MKMunicipalityField, UMCNField


class MKPerson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    umcn = UMCNField()
    id_number = MKIdentityCardNumberField()
    municipality = MKMunicipalityField(blank=True)
    municipality_req = MKMunicipalityField(blank=False)
