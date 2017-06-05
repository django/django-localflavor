# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class CUIdentityCardNumberValidator(RegexValidator):
    """
    Validator for the cuban identity card number.

    Checks that the first 6 digits build a valid date.

    .. versionadded:: 1.6
    """
    birthday_message = _("Enter a valid date (yymmdd) for the first 6 digits of the Identity Card Number.")
    birthday_code = 'invalid_birthday'

    def __call__(self, value):
        super(CUIdentityCardNumberValidator, self).__call__(value)

        try:
            datetime.datetime.strptime(value[:6], '%y%m%d')
        except ValueError:
            raise ValidationError(self.birthday_message, code=self.birthday_code)
