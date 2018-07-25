from django.db import models

from localflavor.au.models import (AUBusinessNumberField, AUCompanyNumberField, AUPostCodeField, AUStateField,
                                   AUTaxFileNumberField)


class AustralianPlace(models.Model):
    state = AUStateField(blank=True)
    state_required = AUStateField()
    state_default = AUStateField(default="NSW", blank=True)
    postcode = AUPostCodeField(blank=True)
    postcode_required = AUPostCodeField()
    postcode_default = AUPostCodeField(default="2500", blank=True)
    name = models.CharField(max_length=20)
    abn = AUBusinessNumberField()
    acn = AUCompanyNumberField()
    tfn = AUTaxFileNumberField()
