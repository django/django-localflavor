from __future__ import absolute_import

from django.forms import ModelForm

from .models import ECPlace


class ECPlaceForm(ModelForm):
    class Meta:
        model = ECPlace
        fields = ('province',)
