from __future__ import absolute_import

from django.forms import ModelForm, Form

from localflavor.au.forms import AUMedicareNumberField
from .models import AustralianPlace


class AustralianPlaceForm(ModelForm):
    """ Form for storing an Australian place. """
    class Meta:
        model = AustralianPlace
        fields = ('state', 'state_required', 'state_default', 'postcode', 'postcode_required', 'postcode_default',
                  'phone', 'name')


class MedicareForm(Form):
    """Form for capturing Medicare info"""

    medicare_no = AUMedicareNumberField()
