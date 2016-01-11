import re

from django import forms
from django.core.validators import EMPTY_VALUES
import phonenumbers
from phonenumbers.phonenumberutil import number_type

from .validators import IBANValidator, BICValidator, IBAN_COUNTRY_CODE_LENGTH


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
        from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES

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
        return value.upper().replace(' ', '').replace('-', '')

    def prepare_value(self, value):
        """ The display format for IBAN has a space every 4 characters. """
        if value is None:
            return value
        grouping = 4
        value = value.upper().replace(' ', '').replace('-', '')
        return ' '.join(value[i:i + grouping] for i in range(0, len(value), grouping))


class BICFormField(forms.CharField):
    """
    A BIC consists of 8 (BIC8) or 11 (BIC11) alphanumeric characters.

    BICs are also known as SWIFT-BIC, BIC code, SWIFT ID, SWIFT code or ISO 9362.

    https://en.wikipedia.org/wiki/ISO_9362

    .. versionadded:: 1.1
    """
    default_validators = [BICValidator()]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 11)
        super(BICFormField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        # BIC is always written in upper case.
        # https://www2.swift.com/uhbonline/books/public/en_uk/bic_policy/bic_policy.pdf
        value = super(BICFormField, self).to_python(value)
        return value.upper()

    def prepare_value(self, value):
        # BIC is always written in upper case.
        value = super(BICFormField, self).prepare_value(value)
        if value is not None:
            return value.upper()
        return value


class PhoneNumberField(forms.CharField):
    """
    A field that uses libphonenumbers for validation and formatting
    """
    region = None

    default_error_messages = {
        'invalid': 'Enter a valid phone number.',
        'international_only': 'International numbers are not allowed.',
        'wrong_type': 'This number type is not allowed.'
    }

    def __init__(self, *args, **kwargs):
        """
        Initialise some settings
        """
        self.allow_international = kwargs.pop('allow_international', True)

        self.allowed_types = kwargs.pop('allowed_types', set())

        self.region = kwargs.pop('region', self.region)

        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def clean(self, value):
        """
        Validate a phone number and strip any non digits from it. Numbers not
        from the chosen region are prefixed with + as per E.164
        """
        value = super(PhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''

        try:
            number = phonenumbers.parse(value, self.region)
        except phonenumbers.NumberParseException:
            raise forms.ValidationError(self.error_messages['invalid'])

        if not phonenumbers.is_valid_number(number):
            raise forms.ValidationError(self.error_messages['invalid'])

        expected_country_code = phonenumbers.PhoneMetadata\
            .metadata_for_region(self.region).country_code

        if number.country_code == expected_country_code:
            number_format = phonenumbers.PhoneNumberFormat.NATIONAL
        elif self.allow_international:
            number_format = phonenumbers.PhoneNumberFormat.E164
        else:
            raise forms.ValidationError(
                self.error_messages['international_only'])

        if self.allowed_types and \
                number_type(number) not in self.allowed_types:
            raise forms.ValidationError(self.error_messages['wrong_type'])

        number = phonenumbers.format_number(number, number_format)

        number = re.sub(r'[^+\d+]+', '', number)

        return number
