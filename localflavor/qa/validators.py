import re
from datetime import date

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from localflavor.generic.countries.iso_3166 import ISO_3166_1_NUMERIC_COUNTRY_CODES


@deconstructible
class QANationalIDValidator:
    """
    Validate Qatari National ID numbers.

    Format: ``CYYNNNSSSSS``

    Where:
    - ``C`` is the century digit (2 or 3)
    - ``YY`` is the last two digits of the year of birth
    - ``NNN`` is an ISO 3166-1 numeric nationality code
    - ``SSSSS`` is a unique serial number           

    Checks the following rules to determine the validity of the number:
        1. The number consists of 11 digits.
        2. The century digit is valid (2 or 3).
        3. The year of birth is not in the future.
        4. The nationality code is a valid ISO 3166-1 numeric country code.
    
    .. versionadded:: 5.1
    """

    message = _('Enter a valid Qatari National ID number')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not value:
            return

        clean_value = str(value).strip()
        if not re.match(r'^\d{11}$', clean_value):
            raise ValidationError(self.message, code=self.code)

        century = clean_value[0]
        year = clean_value[1:3]
        nationality_code = clean_value[3:6]

        if century not in ('2', '3'):
            raise ValidationError(self.message, code=self.code)

        full_year = (int(century) + 17) * 100 + int(year)
        if full_year > date.today().year:
            raise ValidationError(self.message, code=self.code)

        if nationality_code not in ISO_3166_1_NUMERIC_COUNTRY_CODES:
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.message == other.message and
            self.code == other.code
        )
