from django.db import models
from localflavor.mx.models import MXStateField


# Create your models here.
class MyModel(models.Model):
    state = MXStateField()
