from django.forms import ModelForm

from .models import CAPlace


class CAPlaceForm(ModelForm):

    class Meta:
        model = CAPlace
        fields = '__all__'
