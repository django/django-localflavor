from django.db import models

from localflavor.ae.models import (
    UAEEmiratesIDField, UAEEmirateField, UAEPostalCodeField,
    UAEPOBoxField, UAETaxRegistrationNumberField
)


class UAEPlace(models.Model):
    """Test model for UAE localflavor fields."""

    name = models.CharField(max_length=50)
    emirate = UAEEmirateField()
    emirates_id = UAEEmiratesIDField(blank=True)
    postal_code = UAEPostalCodeField(blank=True)
    po_box = UAEPOBoxField(blank=True)
    tax_number = UAETaxRegistrationNumberField(blank=True)

    class Meta:
        app_label = 'test_ae'
