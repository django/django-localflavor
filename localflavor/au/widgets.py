"""
Australian specific form widgets
"""

from django.forms import MultiWidget
from django.utils.translation import ugettext_lazy as _

try:
    from django.forms import NumberInput
except ImportError:
    # for older Django
    from django.forms import TextInput

    class NumberInput(TextInput):
        input_type = 'number'


class AUMedicareNumberWidget(MultiWidget):
    """
    A widget for capturing an Australian Medicare number

    .. versionadded:: 1.1
    """

    def __init__(self, *args, **kwargs):
        widgets = (
            NumberInput(attrs={
                'placeholder': _('Card number'),
                'class': 'au-medicare-card-number',
            }),
            NumberInput(attrs={
                'placeholder': _('IRN'),
                'class': 'au-medicare-irn',
            }),
        )

        super(AUMedicareNumberWidget, self).__init__(widgets=widgets,
                                                     *args, **kwargs)

    def decompress(self, value):
        if value:
            return value
        else:
            return (None, None)
