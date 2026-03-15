from django.db import models

from localflavor.qa.models import QAMunicipalityField, QANationalIDField


class QAPlace(models.Model):
    """Test model for Qatar localflavor fields."""

    name = models.CharField(max_length=50)
    national_id = QANationalIDField(blank=True)
    municipality = QAMunicipalityField(blank=True)

    class Meta:
        app_label = 'test_qa'
