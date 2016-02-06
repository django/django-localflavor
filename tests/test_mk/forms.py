from django.forms import ModelForm

from .models import MKPerson


class MKPersonForm(ModelForm):

    class Meta:
        model = MKPerson
        fields = ('first_name', 'last_name', 'umcn', 'id_number', 'municipality', 'municipality_req')
