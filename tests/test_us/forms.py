from django.forms import ModelForm

from .models import USPlace


class USPlaceForm(ModelForm):

    class Meta:
        model = USPlace
        fields = ('state', 'state_req', 'state_default', 'postal_code', 'name',
                  'ssn', 'zip_code')
