from django.forms import ModelForm

from .models import UseIncludedCountriesModel, UseNordeaExtensionsModel


class UseNordeaExtensionsForm(ModelForm):
    class Meta:
        model = UseNordeaExtensionsModel
        fields = ('iban',)


class UseIncludedCountriesForm(ModelForm):
    class Meta:
        model = UseIncludedCountriesModel
        fields = ('iban',)
