from django.db import models

from localflavor.us.models import USStateField, USPostalCodeField


class USPlace(models.Model):
    state = USStateField(blank=True)
    state_req = USStateField()
    state_default = USStateField(default="CA", blank=True)
    postal_code = USPostalCodeField(blank=True)
    name = models.CharField(max_length=20)
