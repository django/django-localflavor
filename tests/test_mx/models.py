from django.db import models

from localflavor.mx.models import MXCURPField, MXRFCField, MXSocialSecurityNumberField, MXStateField, MXZipCodeField


class MXPersonProfile(models.Model):
    state = MXStateField()
    rfc = MXRFCField()
    curp = MXCURPField()
    zip_code = MXZipCodeField()
    ssn = MXSocialSecurityNumberField()
