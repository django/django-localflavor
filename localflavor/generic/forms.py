from django import forms

from .validators import IBANValidator, IBAN_COUNTRY_CODE_LENGTH


DEFAULT_DATE_INPUT_FORMATS = (
    '%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y',  # '2006-10-25', '25/10/2006', '25/10/06'
    '%b %d %Y', '%b %d, %Y',             # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',             # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',             # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',             # '25 October 2006', '25 October, 2006'
)

DEFAULT_DATETIME_INPUT_FORMATS = (
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%d/%m/%Y %H:%M:%S',     # '25/10/2006 14:30:59'
    '%d/%m/%Y %H:%M',        # '25/10/2006 14:30'
    '%d/%m/%Y',              # '25/10/2006'
    '%d/%m/%y %H:%M:%S',     # '25/10/06 14:30:59'
    '%d/%m/%y %H:%M',        # '25/10/06 14:30'
    '%d/%m/%y',              # '25/10/06'
)

IBAN_MIN_LENGTH = min(IBAN_COUNTRY_CODE_LENGTH.values())


class DateField(forms.DateField):
    """
    A date input field which uses non-US date input formats by default.
    """
    def __init__(self, input_formats=None, *args, **kwargs):
        input_formats = input_formats or DEFAULT_DATE_INPUT_FORMATS
        super(DateField, self).__init__(input_formats=input_formats, *args, **kwargs)


class DateTimeField(forms.DateTimeField):
    """
    A date and time input field which uses non-US date and time input formats
    by default.
    """
    def __init__(self, input_formats=None, *args, **kwargs):
        input_formats = input_formats or DEFAULT_DATETIME_INPUT_FORMATS
        super(DateTimeField, self).__init__(input_formats=input_formats, *args, **kwargs)


class SplitDateTimeField(forms.SplitDateTimeField):
    """
    Split date and time input fields which use non-US date and time input
    formats by default.
    """
    def __init__(self, input_date_formats=None, input_time_formats=None, *args, **kwargs):
        input_date_formats = input_date_formats or DEFAULT_DATE_INPUT_FORMATS
        super(SplitDateTimeField, self).__init__(input_date_formats=input_date_formats,
                                                 input_time_formats=input_time_formats, *args, **kwargs)


class IBANFormField(forms.CharField):
    """
    An IBAN consists of up to 34 alphanumeric characters.

    To limit validation to specific countries, set the 'include_countries' argument with a tuple or list of ISO 3166-1
    alpha-2 codes. For example, `include_countries=('NL', 'BE, 'LU')`.

    A list of countries that use IBANs as part of SEPA is included for convenience. To use this feature, set
    `include_countries=IBAN_SEPA_COUNTRIES` as an argument to the field.

    Example:

    .. code-block:: python

        from django import forms
        from localflavor.generic.forms import IBANFormField
        from localflavor.generic.sepa_countries import IBAN_SEPA_COUNTRIES

        class MyForm(forms.Form):
            iban = IBANFormField(include_countries=IBAN_SEPA_COUNTRIES)

    In addition to validating official IBANs, this field can optionally validate unofficial IBANs that have been
    catalogued by Nordea by setting the `use_nordea_extensions` argument to True.

    https://en.wikipedia.org/wiki/International_Bank_Account_Number

    .. versionadded:: 1.1
    """
    def __init__(self, use_nordea_extensions=False, include_countries=None, *args, **kwargs):
        kwargs.setdefault('min_length', IBAN_MIN_LENGTH)
        kwargs.setdefault('max_length', 34)
        self.default_validators = [IBANValidator(use_nordea_extensions, include_countries)]
        super(IBANFormField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(IBANFormField, self).to_python(value)
        if value is not None:
            return value.replace(' ', '').replace('-', '')
        return value

    def prepare_value(self, value):
        """ The display format for IBAN has a space every 4 characters. """
        grouping = 4
        return ' '.join(value[i:i + grouping] for i in range(0, len(value), grouping))
