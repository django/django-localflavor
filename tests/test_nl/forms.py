from __future__ import absolute_import

from django.forms import ModelForm

from .models import NLPlace


class NLPlaceForm(ModelForm):

    class Meta:
        model = NLPlace
        fields = ('zipcode', 'province', 'sofinr', 'phone', 'bankaccount')
