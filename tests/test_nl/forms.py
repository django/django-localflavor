from django.forms import ModelForm

from .models import NLCar, NLPlace


class NLPlaceForm(ModelForm):

    class Meta:
        model = NLPlace
        fields = ('zipcode', 'province', 'bsn')


class NLCarForm(ModelForm):

    class Meta:
        model = NLCar
        fields = ('license_plate', )
