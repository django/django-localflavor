import itertools
import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

postal_code_re = re.compile(r'^\d{5}-\d{3}$')
cpf_digits_re = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')


def dv_maker(v):
    if v >= 2:
        return 11 - v
    return 0


class BRPostalCodeValidator(RegexValidator):
    """
    A validator for Brazilian Postal Codes (CEP).

    .. versionadded:: 2.2
    """

    def __init__(self, *args, **kwargs):
        self.message = _('Enter a postal code in the format 00000-000.')
        super().__init__(postal_code_re, *args, **kwargs)


class BRCNPJValidator(RegexValidator):
    """
    Validator for brazilian CNPJ.

    .. versionadded:: 2.2
    """

    CNPJ_RE = re.compile(r'^([A-Z0-9]{2}).?([A-Z0-9]{3}).?([A-Z0-9]{3})\/?([A-Z0-9]{4})-?(\d{2})$')

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            regex=self.CNPJ_RE,
            message=_("Invalid CNPJ number."),
            **kwargs
        )

    def _get_check_digit(self, cnpj):
        '''
        Based on official documentation at:
        https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/documentos-tecnicos/cnpj
        '''
        def _get_digit(value):
            values = [ord(c) - 48 for c in value][::-1]
            remainder = (
                sum(
                    [x * y for x, y in list(zip(values, itertools.cycle(range(2, 10))))]
                )
                % 11
            )
            check_digit = 0 if remainder in (0, 1) else 11 - remainder
            return str(check_digit)

        first_check_digit = _get_digit(cnpj)
        second_check_digit = _get_digit(cnpj + first_check_digit)
        return f"{first_check_digit}{second_check_digit}"

    def __call__(self, value):
        super().__call__(value)

        # After this point, only digits and uppercase letters are important
        cleaned_value = re.sub(r"[^A-Z0-9]", "", value)

        input_check_digit = cleaned_value[-2:]
        calculated_check_digit = self._get_check_digit(cleaned_value[:-2])
        if input_check_digit != calculated_check_digit:
            raise ValidationError(self.message, code="invalid")


class BRCPFValidator(RegexValidator):
    """
    Validator for brazilian CPF.

    .. versionadded:: 2.2
    """

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            regex=cpf_digits_re,
            message=_("Invalid CPF number."),
            **kwargs
        )

    def __call__(self, value):
        if not value.isdigit():
            cpf = cpf_digits_re.search(value)
            if cpf:
                value = ''.join(cpf.groups())
            else:
                raise ValidationError(self.message, code='invalid')

        if len(value) != 11:
            raise ValidationError(self.message, code='max_digits')

        orig_dv = value[-2:]
        new_1dv = sum([i * int(value[idx])
                       for idx, i in enumerate(range(10, 1, -1))])
        new_1dv = dv_maker(new_1dv % 11)
        value = value[:-2] + str(new_1dv) + value[-1]
        new_2dv = sum([i * int(value[idx])
                       for idx, i in enumerate(range(11, 1, -1))])
        new_2dv = dv_maker(new_2dv % 11)
        value = value[:-1] + str(new_2dv)
        if value[-2:] != orig_dv:
            raise ValidationError(self.message, code='invalid')
        if value.count(value[0]) == 11:
            raise ValidationError(self.message, code='invalid')
