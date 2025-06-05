from django import forms

from localflavor.ae.forms import UAEEmirateSelect

from .models import UAEPlace


class UAEPlaceForm(forms.ModelForm):
    """Test form for UAE localflavor fields."""

    emirate_select = forms.CharField(widget=UAEEmirateSelect(), required=False)

    class Meta:
        model = UAEPlace
        fields = '__all__'
