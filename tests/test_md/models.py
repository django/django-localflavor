from django.db import models

from localflavor.md.models import MDCompanyTypeField, MDIDNOField, MDLicensePlateField


class MDPlaceModel(models.Model):
    idno = MDIDNOField()
    company_type_1 = MDCompanyTypeField()
    company_type_2 = MDCompanyTypeField()
    license_plate = MDLicensePlateField()
