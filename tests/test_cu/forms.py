from django import forms

from localflavor.cu.forms import CUProvinceField, CURegionField

from .models import CUSomebody


class CUSomewhereForm(forms.ModelForm):
    province_1 = CUProvinceField()
    region_1 = CURegionField()

    class Meta:
        model = CUSomebody
        fields = ('province_1', 'province_2', 'region_1', 'region_2', 'postal_code', 'id_number')
