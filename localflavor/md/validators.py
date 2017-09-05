# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class MDIDNOFieldValidator(RegexValidator):
    """
    Validation for Moldavian IDNO.

    .. versionadded:: 1.6
    """

    error_message = _('Enter a valid IDNO number.')

    def __init__(self):
        super(MDIDNOFieldValidator, self).__init__(regex='^\d{13}$',
                                                   message=self.error_message)

    def __call__(self, value):
        super(MDIDNOFieldValidator, self).__call__(value)


# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Moldova
class MDLicensePlateValidator(RegexValidator):
    """
    Validation for Moldavian License Plates.

    .. versionadded:: 1.6
    """

    error_message = _('Enter a valid license plate.')

    def __init__(self):
        super(MDLicensePlateValidator, self).__init__(regex='^\d{9}$',
                                                      message=self.error_message)

    def __call__(self, value):
        value = value.upper()
        if not self._is_valid(value):
            raise ValidationError(self.error_message)

    def _is_valid(self, value):
        return self._is_old_format(value) or \
               self._is_new_format(value) or \
               self._is_president_format(value) or \
               self._is_diplomatic_format(value) or \
               self._is_police_format(value) or \
               self._is_foreign_format(value) or \
               self._is_state_security_format(value) or \
               self._is_gov_format(value)

    @staticmethod
    def _is_old_format(value):
        from localflavor.md.choices import REGION_CHOICES
        regions = "|".join([code for code, desc in REGION_CHOICES])
        pattern = '({regions}) [A-Z]{{2}} \d{{1,3}}'.format(regions=regions)
        return re.match(pattern, value) is not None

    @staticmethod
    def _is_new_format(value):
        from localflavor.md.choices import LICENSE_PLATE_POLICE
        if not any(x in value for x, y in LICENSE_PLATE_POLICE):
            pattern = '^[A-Z]{3} \d{1,3}$'
            return re.match(pattern, value) is not None

    @staticmethod
    def _is_gov_format(value):
        from localflavor.md.choices import LICENSE_PLATE_GOVERNMENT_TYPE
        types = "|".join([code for code, desc in LICENSE_PLATE_GOVERNMENT_TYPE])
        pattern = '^RM ({types}) \d{{3}}$'.format(types=types)
        return re.match(pattern, value) is not None

    @staticmethod
    def _is_diplomatic_format(value):
        from localflavor.md.choices import LICENSE_PLATE_DIPLOMATIC
        types = "|".join([code for code, desc in LICENSE_PLATE_DIPLOMATIC])
        pattern = '^({types}) \d{{3}} A{{1,2}}$'.format(types=types)
        return re.match(pattern, value) is not None

    @staticmethod
    def _is_police_format(value):
        from localflavor.md.choices import LICENSE_PLATE_POLICE
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
