from django.forms import ModelForm

from .models import BRPersonProfile


class BRPersonProfileForm(ModelForm):

    class Meta:
        model = BRPersonProfile
        fields = ('cpf', 'cnpj', 'postal_code')
