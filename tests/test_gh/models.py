from django.db import models

from localflavor.gh.models import GHRegionField


class GHPlace(models.Model):
    region = GHRegionField(blank=True)