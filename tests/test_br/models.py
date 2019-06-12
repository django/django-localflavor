from django.db import models

from localflavor.br.models import BRCNPJField, BRCPFField, BRPostalCodeField, BRBankField


class BRPersonProfile(models.Model):
    cpf = BRCPFField()
    cnpj = BRCNPJField()
    postal_code = BRPostalCodeField()
    #bank = BRBankField()

class BankingDataBR(models.Model):
    bank = BRBankField()
