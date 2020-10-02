from django.forms import ModelForm

from .models import BYTestModel


class BYTestForm(ModelForm):

    class Meta:
        model = BYTestModel
        fields = ('region', 'pass_num', 'pass_id', 'postal_code')
