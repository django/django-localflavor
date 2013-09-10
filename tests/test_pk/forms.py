from __future__ import absolute_import

from django.forms import ModelForm

from .models import PakistaniPlace


class PakistaniPlaceForm(ModelForm):
    """ Form for storing an Pakistani place. """
    class Meta:
        model = PakistaniPlace
