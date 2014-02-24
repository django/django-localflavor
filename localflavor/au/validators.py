"""
Australian-specific validation functions
"""

import re

from django.forms import ValidationError
from django.utils.encoding import smart_text


def validate_medicare_number(value):
    """
    Validate the medicare number

    The first digit must be between 2 and 6.

    The first 8 numbers as a weighted sum modulo 10 gives the check
    digit.

    The 10th digit (issue number) and IRN are ignored for the purposes of
    the validation.

    .. versionadded:: 1.1
    """

    # remove spaces and hyphens
    value = re.sub(r'\s+|-', '', smart_text(value))

    if not re.match(r'\d{10}', smart_text(value)):
        raise ValidationError("Medicare number must be 10 digits.")

    if not (2 <= int(value[0]) <= 6):
        raise ValidationError("Medicare number is not valid.")

    weightings = (1, 3, 7, 9, 1, 3, 7, 9)
    check_bit = sum(int(a) * b for (a, b) in zip(value, weightings)) % 10

    if check_bit != int(value[8]):
        raise ValidationError("Medicare number is not valid.")
