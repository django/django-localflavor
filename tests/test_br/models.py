from django.db import models

from localflavor.br.models import BRCNPJField, BRCPFField, BRPostalCodeField


class BRPersonProfile(models.Model):
    cpf = BRCPFField()
    cnpj = BRCNPJField()
    postal_code = BRPostalCodeField()
