from django.db import models

from localflavor.nl.models import (NLBankAccountNumberField, NLBSNField, NLPhoneNumberField, NLProvinceField,
                                   NLSoFiNumberField, NLZipCodeField)


class NLPlace(models.Model):

    zipcode = NLZipCodeField()
    province = NLProvinceField(default='ZH')

    sofinr = NLSoFiNumberField()
    bsn = NLBSNField()
    phone = NLPhoneNumberField()
    bankaccount = NLBankAccountNumberField()

    class Meta:
        app_label = 'test_nl'
