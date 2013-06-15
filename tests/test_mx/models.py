from django.db import models

from localflavor.mx.models import (MXStateField, MXRFCField, MXCURPField,
                                   MXZipCodeField, MXSocialSecurityNumberField)


class MXPersonProfile(models.Model):
    state = MXStateField()
    rfc = MXRFCField()
    curp = MXCURPField()
    zip_code = MXZipCodeField()
    ssn = MXSocialSecurityNumberField()
