import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class NLBankAccountNumberFieldValidator(RegexValidator):
    """
    Validation for Dutch bank accounts.

    Validation references:
    http://www.mobilefish.com/services/elfproef/elfproef.php
    http://www.credit-card.be/BankAccount/ValidationRules.htm#NL_Validation

    .. versionadded:: 1.1
    """
    default_error_messages = {
        'invalid': _('Enter a valid bank account number'),
        'wrong_length': _('Bank account numbers have 1 - 7, 9 or 10 digits'),
    }

    def __init__(self, regex=None, message=None, code=None):
        super(NLBankAccountNumberFieldValidator, self).__init__(regex='^[0-9]+$',
                                                                message=self.default_error_messages['invalid'])
        self.no_leading_zeros_regex = re.compile('[1-9]+')

    def __call__(self, value):
        super(NLBankAccountNumberFieldValidator, self).__call__(value)

        # Need to check for values over the field's max length before the zero are stripped.
        # This check is needed to allow this validator to be used without Django's MaxLengthValidator.
        if len(value) > 10:
            raise ValidationError(self.default_error_messages['wrong_length'])

        # Strip the leading zeros.
        m = re.search(self.no_leading_zeros_regex, value)
        if not m:
            raise ValidationError(self.default_error_messages['invalid'])
        value = value[m.start():]

        if len(value) != 9 and len(value) != 10 and not 1 <= len(value) <= 7:
            raise ValidationError(self.default_error_messages['wrong_length'])

        # Perform the eleven test validation on non-PostBank numbers.
        if len(value) == 9 or len(value) == 10:
            if len(value) == 9:
                value = "0" + value

            eleven_test_sum = sum([int(a) * b for a, b in zip(value, range(1, 11))])
            if eleven_test_sum % 11 != 0:
                raise ValidationError(self.default_error_messages['invalid'])


class NLBankAccountNumberField(models.CharField):
    """
    A Dutch bank account model field.

    This model field uses :class:`.NLBankAccountNumberFieldValidator` for validation.

    .. versionadded:: 1.1
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 10)
        super(NLBankAccountNumberField, self).__init__(*args, **kwargs)
        # Ensure that only the NLBankAccountNumberFieldValidator is set.
        self.validators = [NLBankAccountNumberFieldValidator()]
