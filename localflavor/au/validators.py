# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class AUBusinessNumberFieldValidator(RegexValidator):
    """
    Validation for Australian Business Numbers.

    .. versionadded:: 1.3
    """

    error_message = _('Enter a valid ABN.')

    def __init__(self):
        eleven_digits = '^\d{11}$'
        super(AUBusinessNumberFieldValidator, self).__init__(
            regex=eleven_digits, message=self.error_message)

    def _is_valid(self, value):
        """
        Return whether the given value is a valid ABN.

        See http://www.clearwater.com.au/code for a description of the
        validation algorithm.

        """
        # 1. Subtract 1 from the first digit.
        digits = [int(i) for i in list(value)]
        digits[0] -= 1

        # 2. Multiply each digit by its weighting factor.
        WEIGHTING_FACTORS = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        weighted = [digit * weight for digit, weight in zip(digits, WEIGHTING_FACTORS)]

        # 3. Sum the resulting values.
        total = sum(weighted)

        # 4. Divide the total by 89, noting the remainder.
        remainder = total % 89

        # 5. If the remainder is zero, then it's a valid ABN.
        return remainder == 0

    def __call__(self, value):
        super(AUBusinessNumberFieldValidator, self).__call__(value)
        if not self._is_valid(value):
            raise ValidationError(self.error_message)
