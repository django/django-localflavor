from django import forms

from .models import FranceModel


class FranceForm(forms.ModelForm):
    class Meta:
        model = FranceModel
        fields = ("siren", "siret", "rna")
