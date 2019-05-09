import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from .choices import (LICENSE_PLATE_DIPLOMATIC, LICENSE_PLATE_GOVERNMENT_TYPE, LICENSE_PLATE_POLICE,
                      REGION_CHOICES_2002_2015)


class MDIDNOFieldValidator(RegexValidator):
    """
    Validation for Moldavian IDNO.

    .. versionadded:: 2.1
    """

    error_message = _('Enter a valid IDNO number.')
    regex = '^\d{13}$'
    message = error_message


class MDLicensePlateValidator(RegexValidator):
    """
    Validation for `Moldavian License Plates`_.

    .. _Moldavian License Plates: https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Moldova
    .. versionadded:: 2.1
    """

    error_message = _('Enter a valid license plate.')
    regex = '^\d{13}$'
    message = error_message

    def __call__(self, value):
        value = value.upper()
        if not self._is_valid(value):
            raise ValidationError(self.error_message)

    def _is_valid(self, value):
        return any([
            self._is_old_format(value),
            self._is_new_format(value),
            self._is_president_format(value),
            self._is_diplomatic_format(value),
            self._is_police_format(value),
            self._is_foreign_format(value),
            self._is_state_security_format(value),
            self._is_gov_format(value)
        ])

    @staticmethod
    def _is_old_format(value):
        regions = "|".join([code for code, desc in REGION_CHOICES_2002_2015])
        pattern = '({regions}) [A-Z]{{2}} \d{{1,3}}'.format(regions=regions)
        return re.match(pattern, value) is not None

    @staticmethod
    def _is_new_format(value):
        if not any(x in value for x, y in LICENSE_PLATE_POLICE):
            pattern = '^[A-Z]{3} \d{1,3}$'
            return re.match(pattern, value) is not None

    @staticmethod
    def _is_gov_format(value):
        types = "|".join([code for code, desc in LICENSE_PLATE_GOVERNMENT_TYPE])
        pattern = '^RM ({types}) \d{{3}}$'.format(types=types)
        return re.match(pattern, value) is not None

    @staticmethod
    def _is_diplomatic_format(value):
        types = "|".join([code for code, desc in LICENSE_PLATE_DIPLOMATIC])
        pattern = '^({types}) \d{{3}} A{{1,2}}$'.format(types=types)
        return re.match(pattern, value) is not None

    @staticmethod
    def _is_police_format(value):
        types = "|".join([code for code, desc in LICENSE_PLATE_POLICE])
        gov_format = '^({types}) \d{{4}}$'.format(types=types)
        return re.match(gov_format, value) is not None

    @staticmethod
    def _is_president_format(value):
        pattern = '^RM \d{4}$'
        return re.match(pattern, value) is not None

    @staticmethod
    def _is_state_security_format(value):
        pattern = '^SP \d{3}$'
        return re.match(pattern, value) is not None

    @staticmethod
    def _is_foreign_format(value):
        pattern = '^H \d{4}$'
        return re.match(pattern, value) is not None
