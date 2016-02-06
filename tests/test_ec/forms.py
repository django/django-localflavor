from django.forms import ModelForm

from .models import ECPlace


class ECPlaceForm(ModelForm):
    class Meta:
        model = ECPlace
        fields = ('province',)
