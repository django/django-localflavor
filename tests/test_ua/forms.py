from django.forms import ModelForm

from .models import UAFlavorTestModel


class UAFlavorTestForm(ModelForm):

    class Meta:
        model = UAFlavorTestModel
        fields = '__all__'
