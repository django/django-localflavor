from django import forms as forms
from localflavor.fr.forms import FRDepartmentField, FRRegionField
#from .models import FRPlace


class FRPlaceForm(forms.Form):
    department = FRDepartmentField()
    region = FRRegionField()

    #class Meta:
    #    model = FRPlace
