from django.forms import ModelForm

from .models import NLPlace


class NLPlaceForm(ModelForm):

    class Meta:
        model = NLPlace
        fields = ('zipcode', 'province', 'sofinr', 'bsn', 'phone', 'bankaccount')
