from django.forms import ModelForm

from .models import PakistaniPlace


class PakistaniPlaceForm(ModelForm):
    """Form for storing a Pakistani place."""

    class Meta:
        model = PakistaniPlace
        fields = ('state', 'state_required', 'state_default', 'postcode', 'postcode_required', 'postcode_default',
                  'name')
