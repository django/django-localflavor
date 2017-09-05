from django.forms import ModelForm

from .models import MDPlaceModel


class MDPlaceForm(ModelForm):
    class Meta:
        model = MDPlaceModel
        fields = ('idno', 'company_type_1', 'company_type_2', 'license_plate')
