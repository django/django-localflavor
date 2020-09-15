from django.core.validators import BaseValidator


class RangeValidator(BaseValidator):
    '''
    A validator which ensures that the value is in the provided range.

    The tuple of min value and max value (not included in range) must be
    specified in the validator's __init__.
    '''

    def compare(self, a, values):
        return a in range(*values)