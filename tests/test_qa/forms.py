from django import forms

from .models import QAPlace


class QAPlaceForm(forms.ModelForm):
    """Test form for Qatar localflavor fields."""

    class Meta:
        model = QAPlace
        fields = '__all__'
