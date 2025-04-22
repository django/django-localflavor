from django.db import models

from localflavor.fr.models import FRRNAField, FRSIRENField, FRSIRETField


class FranceModel(models.Model):
    siren = FRSIRENField(null=True, default=None, blank=True)
    siret = FRSIRETField(null=True, default=None, blank=True)
    rna = FRRNAField(null=True, default=None, blank=True)
