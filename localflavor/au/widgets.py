"""
Australian specific form widgets
"""

from django.forms import MultiWidget

try:
    from django.forms import NumberInput
except ImportError:
    # for older Django
    from django.forms import TextInput

    class NumberInput(TextInput):
        def __init__(self, attrs=None, *args, **kwargs):
            if not attrs:
                attrs = {}

            attrs['type'] = 'number'

            super(NumberInput, self).__init__(attrs=attrs, *args, **kwargs)


class AUMedicareNumberWidget(MultiWidget):
    """
    A widget for capturing an Australian Medicare number
    """

    def __init__(self, *args, **kwargs):
        widgets = (
            NumberInput(attrs={
                'placeholder': "Card Number",
                'class': 'au-medicare-card-number',
            }),
            NumberInput(attrs={
                'placeholder': "IRN",
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
