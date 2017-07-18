from django.db import models

from localflavor.mx.models import (MXCLABEField, MXCURPField, MXRFCField, MXSocialSecurityNumberField, MXStateField,
                                   MXZipCodeField)


class MXPersonProfile(models.Model):
    state = MXStateField(blank=True)
    rfc = MXRFCField()
    curp = MXCURPField()
    zip_code = MXZipCodeField()
    ssn = MXSocialSecurityNumberField()
    clabe = MXCLABEField()
