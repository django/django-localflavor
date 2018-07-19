from django.forms import ModelForm

from .models import AustralianPlace


class AustralianPlaceForm(ModelForm):
    """Form for storing an Australian place."""

    class Meta:
        model = AustralianPlace
        fields = ('state', 'state_required', 'state_default', 'postcode', 'postcode_required', 'postcode_default',
                  'name', 'abn', 'tfn')
