# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import string

from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _

from . import checksums
from .countries.iso_3166 import ISO_3166_1_ALPHA2_COUNTRY_CODES

# Dictionary of ISO country code to IBAN length.
#
# The official IBAN Registry document is the best source for up-to-date information about IBAN formats and which
# countries are in IBAN.
#
# https://www.swift.com/standards/data-standards/iban
#
# The IBAN_COUNTRY_CODE_LENGTH dictionary has been updated version 64 of the IBAN Registry document which was published
# in March 2016.
#
# Other Resources:
#
# https://en.wikipedia.org/wiki/International_Bank_Account_Number#IBAN_formats_by_country
# http://www.ecbs.org/iban/france-bank-account-number.html
# https://www.nordea.com/V%C3%A5ra+tj%C3%A4nster/Internationella+produkter+och+tj%C3%A4nster/Cash+Management/IBAN+countries/908472.html


IBAN_COUNTRY_CODE_LENGTH = {'AL': 28,  # Albania
                            'AD': 24,  # Andorra
                            'AE': 23,  # United Arab Emirates
                            'AT': 20,  # Austria
                            'AZ': 28,  # Azerbaijan
                            'BA': 20,  # Bosnia and Herzegovina
                            'BE': 16,  # Belgium
                            'BG': 22,  # Bulgaria
                            'BH': 22,  # Bahrain
                            'BR': 29,  # Brazil
                            'CH': 21,  # Switzerland
                            'CR': 21,  # Costa Rica
                            'CY': 28,  # Cyprus
                            'CZ': 24,  # Czech Republic
                            'DE': 22,  # Germany
                            'DK': 18,  # Denmark
                            'DO': 28,  # Dominican Republic
                            'EE': 20,  # Estonia
                            'ES': 24,  # Spain
                            'FI': 18,  # Finland
                            'FO': 18,  # Faroe Islands
                            'FR': 27,  # France + Central African Republic, French Guiana, French Polynesia, Guadeloupe,
                                       #          Martinique, Réunion, Saint-Pierre and Miquelon, New Caledonia,
                                       #          Wallis and Futuna
                            'GB': 22,  # United Kingdom + Guernsey, Isle of Man, Jersey
                            'GE': 22,  # Georgia
                            'GI': 23,  # Gibraltar
                            'GL': 18,  # Greenland
                            'GR': 27,  # Greece
                            'GT': 28,  # Guatemala
                            'HR': 21,  # Croatia
                            'HU': 28,  # Hungary
                            'IE': 22,  # Ireland
                            'IL': 23,  # Israel
                            'IS': 26,  # Iceland
                            'IT': 27,  # Italy
                            'JO': 30,  # Jordan
                            'KZ': 20,  # Kazakhstan
                            'KW': 30,  # Kuwait
                            'LB': 28,  # Lebanon
                            'LC': 32,  # Saint Lucia
                            'LI': 21,  # Liechtenstein
                            'LT': 20,  # Lithuania
                            'LU': 20,  # Luxembourg
                            'LV': 21,  # Latvia
                            'MC': 27,  # Monaco
                            'MD': 24,  # Moldova
                            'ME': 22,  # Montenegro
                            'MK': 19,  # Macedonia
                            'MT': 31,  # Malta
                            'MR': 27,  # Mauritania
                            'MU': 30,  # Mauritius
                            'NL': 18,  # Netherlands
                            'NO': 15,  # Norway
                            'PS': 29,  # Palestine
                            'PK': 24,  # Pakistan
                            'PL': 28,  # Poland
                            'PT': 25,  # Portugal + Sao Tome and Principe
                            'QA': 29,  # Qatar
                            'RO': 24,  # Romania
                            'RS': 22,  # Serbia
                            'SA': 24,  # Saudi Arabia
                            'SC': 31,  # Seychelles
                            'SE': 24,  # Sweden
                            'SI': 19,  # Slovenia
                            'SK': 24,  # Slovakia
                            'SM': 27,  # San Marino
                            'ST': 25,  # Sao Tome And Principe
                            'TL': 23,  # Timor-Leste
                            'TN': 24,  # Tunisia
                            'TR': 26,  # Turkey
                            'UA': 29,  # Ukraine
                            'VG': 24,  # British Virgin Islands
                            'XK': 20}  # Republic of Kosovo (user-assigned country code)


# Nordea has catalogued IBANs for some additional countries but they are not part of the office IBAN network yet.
#
# Reference:
# https://www.nordea.com/V%C3%A5ra+tj%C3%A4nster/Internationella+produkter+och+tj%C3%A4nster/Cash+Management/IBAN+countries/908472.html

NORDEA_COUNTRY_CODE_LENGTH = {'AO': 25,  # Angola
                              'BJ': 28,  # Benin
                              'BF': 27,  # Burkina Faso
                              'BI': 16,  # Burundi
                              'CI': 28,  # Ivory Coast
                              'CG': 27,  # Congo
                              'CM': 27,  # Cameroon
                              'CV': 25,  # Cape Verde
                              'DZ': 24,  # Algeria
                              'EG': 27,  # Egypt
                              'GA': 27,  # Gabon
                              'IR': 26,  # Iran
                              'MG': 27,  # Madagascar
                              'ML': 28,  # Mali
                              'MZ': 25,  # Mozambique
                              'SN': 28}  # Senegal


@deconstructible
class IBANValidator(object):
    """A validator for International Bank Account Numbers (IBAN - ISO 13616-1:2007)."""

    def __init__(self, use_nordea_extensions=False, include_countries=None):
        self.use_nordea_extensions = use_nordea_extensions
        self.include_countries = include_countries

        self.validation_countries = IBAN_COUNTRY_CODE_LENGTH.copy()
        if self.use_nordea_extensions:
            self.validation_countries.update(NORDEA_COUNTRY_CODE_LENGTH)

        if self.include_countries:
            for country_code in self.include_countries:
                if country_code not in self.validation_countries:
                    msg = 'Explicitly requested country code %s is not ' \
                          'part of the configured IBAN validation set.' % country_code
                    raise ImproperlyConfigured(msg)

    def __eq__(self, other):
        return (self.use_nordea_extensions == other.use_nordea_extensions and
                self.include_countries == other.include_countries)

    @staticmethod
    def iban_checksum(value):
        """
        Returns check digits for an input IBAN number.

        Original checksum in input value is ignored.
        """
        # 1. Move the two initial characters to the end of the string, replacing checksum for '00'
        value = value[4:] + value[:2] + '00'

        # 2. Replace each letter in the string with two digits, thereby expanding the string, where
        #    A = 10, B = 11, ..., Z = 35.
        value_digits = ''
        for x in value:
            if '0' <= x <= '9':
                value_digits += x
            elif 'A' <= x <= 'Z':
                value_digits += str(ord(x) - 55)
            else:
                raise ValidationError(_('%s is not a valid character for IBAN.') % x)

        # 3. The remainder of the number above when divided by 97 is then subtracted from 98.
        return '%02d' % (98 - int(value_digits) % 97)

    def __call__(self, value):
        """
        Validates the IBAN value using the official IBAN validation algorithm.

        https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN
        """
        if value is None:
            return value

        value = value.upper().replace(' ', '').replace('-', '')

        # Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid.
        country_code = value[:2]
        if country_code in self.validation_countries:

            if self.validation_countries[country_code] != len(value):
                msg_params = {'country_code': country_code, 'number': self.validation_countries[country_code]}
                raise ValidationError(_('%(country_code)s IBANs must contain %(number)s characters.') % msg_params)

        else:
            raise ValidationError(_('%s is not a valid country code for IBAN.') % country_code)
        if self.include_countries and country_code not in self.include_countries:
            raise ValidationError(_('%s IBANs are not allowed in this field.') % country_code)

        if self.iban_checksum(value) != value[2:4]:
            raise ValidationError(_('Not a valid IBAN.'))


@deconstructible
class BICValidator(object):
    """
    A validator for SWIFT Business Identifier Codes (ISO 9362:2009).

    Validation is based on the BIC structure found on wikipedia.

    https://en.wikipedia.org/wiki/ISO_9362#Structure
    """

    def __eq__(self, other):
        # The is no outside modification of properties so this should always be true by default.
        return True

    def __call__(self, value):
        if value is None:
            return value

        value = value.upper()

        # Length is 8 or 11.
        bic_length = len(value)
        if bic_length != 8 and bic_length != 11:
            raise ValidationError(_('BIC codes have either 8 or 11 characters.'))

        # First 4 letters are A - Z.
        institution_code = value[:4]
        for x in institution_code:
            if x not in string.ascii_uppercase:
                raise ValidationError(_('%s is not a valid institution code.') % institution_code)

        # Letters 5 and 6 consist of an ISO 3166-1 alpha-2 country code.
        country_code = value[4:6]
        if country_code not in ISO_3166_1_ALPHA2_COUNTRY_CODES:
            raise ValidationError(_('%s is not a valid country code.') % country_code)


@deconstructible
class EANValidator(object):
    """
    A generic validator for EAN like codes with the last digit being the checksum.

    http://en.wikipedia.org/wiki/International_Article_Number_(EAN)
    """

    message = _('Not a valid EAN code.')

    def __init__(self, strip_nondigits=False, message=None):
        if message is not None:
            self.message = message
        self.strip_nondigits = strip_nondigits

    def __eq__(self, other):
        return ((not hasattr(self, 'message') or self.message == other.message) and
                self.strip_nondigits == other.strip_nondigits)

    def __call__(self, value):
        if value is None:
            return value
        if self.strip_nondigits:
            value = re.compile(r'[^\d]+').sub('', value)
        if not checksums.ean(value):
            raise ValidationError(self.message, code='invalid')
