from django.db import models

from localflavor.br.models import BRCNPJField, BRCPFField, BRPostalCodeField,
BR
# from localflavor.br.models import BRBankField


class BRPersonProfile(models.Model):
    cpf = BRCPFField()
    cnpj = BRCNPJField()
    postal_code = BRPostalCodeField()
    #bank = BRBankField()
