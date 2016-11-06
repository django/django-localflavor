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
        weighting_factors = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        weighted = [digit * weight for digit, weight in zip(digits, weighting_factors)]

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


class AUTaxFileNumberFieldValidator(RegexValidator):
    """
    Validation for Australian Tax File Numbers.

    .. versionadded:: 1.4
    """

    error_message = _('Enter a valid TFN.')

    def __init__(self):
        """Regex for 8 to 9 digits."""
        super(AUTaxFileNumberFieldValidator, self).__init__(
            regex='^\d{8,9}$', message=self.error_message)

    def _is_valid(self, value):
        """
        Return whether the given value is a valid TFN.

        See http://www.mathgen.ch/codes/tfn.html for a description of the
        validation algorithm.

        """
        # 1. Multiply each digit by its weighting factor.
        digits = [int(i) for i in list(value)]
        weighting_factors = [1, 4, 3, 7, 5, 8, 6, 9, 10]
        weighted = [digit * weight for digit, weight in zip(digits, weighting_factors)]

        # 2. Sum the resulting values.
        total = sum(weighted)

        # 3. Divide the total by 11, noting the remainder.
        remainder = total % 11

        # 4. If the remainder is zero, then it's a valid TFN.
        return remainder == 0

    def __call__(self, value):
        value = value.replace(' ', '')
        super(AUTaxFileNumberFieldValidator, self).__call__(value)
        if not self._is_valid(value):
            raise ValidationError(self.error_message)
