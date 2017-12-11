# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class NLZipCodeFieldValidator(RegexValidator):
    """
    Validation for Dutch zip codes.

    .. versionadded:: 1.3
    """

    error_message = _('Enter a valid zip code.')

    def __init__(self):
        super(NLZipCodeFieldValidator, self).__init__(regex='^\d{4} ?[A-Z]{2}$',
                                                      message=self.error_message)

    def __call__(self, value):
        super(NLZipCodeFieldValidator, self).__call__(value)

        if int(value[:4]) < 1000:
            raise ValidationError(self.error_message)


class NLBSNFieldValidator(RegexValidator):
    """
    Validation for Dutch social security numbers (BSN).

    .. versionadded:: 1.6
    """

    error_message = _('Enter a valid BSN.')

    def __init__(self):
        super(NLBSNFieldValidator, self).__init__(regex='^\d{9}$', message=self.error_message)

    def bsn_checksum_ok(self, value):
        checksum = 0
        for i in range(9, 1, -1):
            checksum += int(value[9 - i]) * i
        checksum -= int(value[-1])

        return checksum % 11 == 0

    def __call__(self, value):
        super(NLBSNFieldValidator, self).__call__(value)

        if int(value) == 0:
            raise ValidationError(self.error_message)

        if not self.bsn_checksum_ok(value):
            raise ValidationError(self.error_message)
