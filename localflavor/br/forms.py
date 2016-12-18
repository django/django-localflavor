# -*- coding: utf-8 -*-
"""BR-specific Form helpers."""

from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Field, RegexField, Select
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from localflavor.generic.forms import DeprecatedPhoneNumberFormFieldMixin

from .br_states import STATE_CHOICES

phone_digits_re = re.compile(r'^(\d{2})[-\.]?(\d{4,5})[-\.]?(\d{4})$')
cpf_digits_re = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')
cnpj_digits_re = re.compile(
    r'^(\d{2})[.-]?(\d{3})[.-]?(\d{3})/(\d{4})-(\d{2})$'
)
process_digits_re = re.compile(
    r'^(\d{7})-?(\d{2})\.?(\d{4})\.?(\d)\.?(\d{2})\.?(\d{4})$'
)


class BRZipCodeField(RegexField):
    """A form field that validates input as a Brazilian zip code, with the format XXXXX-XXX."""

    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX-XXX.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(BRZipCodeField, self).__init__(r'^\d{5}-\d{3}$',
                                             max_length, min_length, *args, **kwargs)


class BRPhoneNumberField(Field, DeprecatedPhoneNumberFormFieldMixin):
    """
    A form field that validates input as a Brazilian phone number.

    The phone number must be in either of the following formats: XX-XXXX-XXXX or XX-XXXXX-XXXX.
    """

    default_error_messages = {
        'invalid': _(('Phone numbers must be in either of the following '
                      'formats: XX-XXXX-XXXX or XX-XXXXX-XXXX.')),
    }

    def clean(self, value):
        super(BRPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\(|\)|\s+)', '', force_text(value))
        m = phone_digits_re.search(value)
        if m:
            return '%s-%s-%s' % (m.group(1), m.group(2), m.group(3))
        raise ValidationError(self.error_messages['invalid'])


class BRStateSelect(Select):
    """A Select widget that uses a list of Brazilian states/territories as its choices."""

    def __init__(self, attrs=None):
        super(BRStateSelect, self).__init__(attrs, choices=STATE_CHOICES)


class BRStateChoiceField(Field):
    """A choice field that uses a list of Brazilian states as its choices."""

    widget = Select
    default_error_messages = {
        'invalid': _('Select a valid brazilian state. That state is not one of the available states.'),
    }

    def __init__(self, required=True, widget=None, label=None, initial=None, help_text=None):
        super(BRStateChoiceField, self).__init__(required, widget, label, initial, help_text)
        self.widget.choices = STATE_CHOICES

    def clean(self, value):
        value = super(BRStateChoiceField, self).clean(value)
        if value in EMPTY_VALUES:
            value = ''
        value = force_text(value)
        if value == '':
            return value
        valid_values = set([force_text(entry[0]) for entry in self.widget.choices])
        if value not in valid_values:
            raise ValidationError(self.error_messages['invalid'])
        return value


def dv_maker(v):
    if v >= 2:
        return 11 - v
    return 0


# TODO deprecate function because it's name is not PEP8 compliant, issue #258
def DV_maker(v):  # noqa
    return dv_maker(v)


class BRCPFField(CharField):
    """
    A form field that validates a CPF number or a CPF string.

    A CPF number is compounded by XXX.XXX.XXX-VD. The two last digits are check digits.

    More information:
    http://en.wikipedia.org/wiki/Cadastro_de_Pessoas_F%C3%ADsicas
    """

    default_error_messages = {
        'invalid': _("Invalid CPF number."),
        'max_digits': _("This field requires at most 11 digits or 14 characters."),
    }

    def __init__(self, max_length=14, min_length=11, *args, **kwargs):
        super(BRCPFField, self).__init__(max_length, min_length, *args, **kwargs)

    def clean(self, value):
        """Value can be either a string in the format XXX.XXX.XXX-XX or an 11-digit number."""
        value = super(BRCPFField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        orig_value = value[:]
        if not value.isdigit():
            cpf = cpf_digits_re.search(value)
            if cpf:
                value = ''.join(cpf.groups())
            else:
                raise ValidationError(self.error_messages['invalid'])

        if len(value) != 11:
            raise ValidationError(self.error_messages['max_digits'])
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
            raise ValidationError(self.error_messages['invalid'])
        if value.count(value[0]) == 11:
            raise ValidationError(self.error_messages['invalid'])
        return orig_value


class BRCNPJField(CharField):
    """
    A form field that validates input as `Brazilian CNPJ`_.

    Input can either be of the format XX.XXX.XXX/XXXX-XX or be a group of 14
    digits.

    If you want to use the long format only, you can specify:
        brcnpj_field = BRCNPJField(min_length=16)

    If you want to use the short format, you can specify:
        brcnpj_field = BRCNPJField(max_length=14)

    Otherwise both formats will be valid.

    .. _Brazilian CNPJ: http://en.wikipedia.org/wiki/National_identification_number#Brazil
    .. versionchanged:: 1.4
    """

    default_error_messages = {
        'invalid': _("Invalid CNPJ number."),
        'max_digits': _("This field requires at least 14 digits"),
    }

    def __init__(self, min_length=14, max_length=18, *args, **kwargs):
        super(BRCNPJField, self).__init__(max_length, min_length, *args, **kwargs)

    def clean(self, value):
        """Value can be either a string in the format XX.XXX.XXX/XXXX-XX or a group of 14 characters."""
        value = super(BRCNPJField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        orig_value = value[:]
        if not value.isdigit():
            cnpj = cnpj_digits_re.search(value)
            if cnpj:
                value = ''.join(cnpj.groups())
            else:
                raise ValidationError(self.error_messages['invalid'])

        if len(value) != 14:
            raise ValidationError(self.error_messages['max_digits'])
        orig_dv = value[-2:]

        new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(5, 1, -1)) + list(range(9, 1, -1)))])
        new_1dv = dv_maker(new_1dv % 11)
        value = value[:-2] + str(new_1dv) + value[-1]
        new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(6, 1, -1)) + list(range(9, 1, -1)))])
        new_2dv = dv_maker(new_2dv % 11)
        value = value[:-1] + str(new_2dv)
        if value[-2:] != orig_dv:
            raise ValidationError(self.error_messages['invalid'])

        return orig_value


def mod_97_base10(value):
    return 98 - ((value * 100 % 97) % 97)


class BRProcessoField(CharField):
    """
    A form field that validates a Legal Process(Processo) number or a Legal Process string.

    A Processo number is compounded by NNNNNNN-DD.AAAA.J.TR.OOOO. The two DD digits are check digits.
    More information:
    http://www.cnj.jus.br/busca-atos-adm?documento=2748

    .. versionadded:: 1.2
    """

    default_error_messages = {'invalid': _("Invalid Process number.")}

    def __init__(self, max_length=25, min_length=20, *args, **kwargs):
        super(BRProcessoField, self).__init__(max_length, min_length, *args, **kwargs)

    def clean(self, value):
        """Value can be either a string in the format NNNNNNN-DD.AAAA.J.TR.OOOO or an 20-digit number."""
        value = super(BRProcessoField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        orig_value = value[:]
        if not value.isdigit():
            process_number = process_digits_re.search(value)
            if process_number:
                value = ''.join(process_number.groups())
            else:
                raise ValidationError(self.error_messages['invalid'])

        orig_dv = value[7:9]

        value_without_digits = int(value[0:7] + value[9:])

        if str(mod_97_base10(value_without_digits)).zfill(2) != orig_dv:
            raise ValidationError(self.error_messages['invalid'])

        return orig_value
