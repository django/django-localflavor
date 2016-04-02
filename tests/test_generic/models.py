from django.db import models

from localflavor.generic.models import IBANField


class UseNordeaExtensionsModel(models.Model):
    iban = IBANField(use_nordea_extensions=True)


class UseIncludedCountriesModel(models.Model):
    iban = IBANField(include_countries=['NL'])
