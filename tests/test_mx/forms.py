from __future__ import absolute_import

from django.forms import ModelForm

from .models import MXPersonProfile


class MXPersonProfileForm(ModelForm):

    class Meta:
        model = MXPersonProfile
        fields = ('state', 'rfc', 'curp', 'zip_code', 'ssn')
