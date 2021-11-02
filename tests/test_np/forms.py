from django.forms import ModelForm

from .models import NepalianPlace

class NepaliPlaceForm(ModelForm):

    """Form for storing a Nepali place."""

    class Meta:
        model = NepalianPlace
        fields = '__all__'