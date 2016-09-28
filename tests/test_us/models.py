from django.db import models

from localflavor.us.models import USPostalCodeField, USSocialSecurityNumberField, USStateField, USZipCodeField


class USPlace(models.Model):
    state = USStateField(blank=True)
    state_req = USStateField()
    state_default = USStateField(default="CA", blank=True)
    postal_code = USPostalCodeField(blank=True)
    name = models.CharField(max_length=20)
    ssn = USSocialSecurityNumberField(blank=True)
    zip_code = USZipCodeField(blank=True)
