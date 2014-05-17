# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

# Dictionary of ISO country code to IBAN length.
#
# References:
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
                            'SE': 24,  # Sweden
                            'SI': 19,  # Slovenia
                            'SK': 24,  # Slovakia
                            'SM': 27,  # San Marino
                            'TN': 24,  # Tunisia
                            'TR': 26,  # Turkey
                            'VG': 24}  # British Virgin Islands


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
                              'UA': 29,  # Ukraine
                              'SN': 28}  # Senegal


class IBANValidator(object):
    """ A validator for International Bank Account Numbers (IBAN - ISO 13616-1:2007). """

    def __init__(self, use_nordea_extensions=False, include_countries=None):
        self.validation_countries = IBAN_COUNTRY_CODE_LENGTH.copy()
        if use_nordea_extensions:
            self.validation_countries.update(NORDEA_COUNTRY_CODE_LENGTH)

        self.include_countries = include_countries
        if self.include_countries:
            for country_code in include_countries:
                if country_code not in self.validation_countries:
                    raise ImproperlyConfigured(_('Explicitly requested country code {0} is not part of the configured IBAN validation set.'
                                                 ''.format(country_code)))

    def __call__(self, value):
        """
        Validates the IBAN value using the official IBAN validation algorithm.

        https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN
        """
        if value is None:
            return value

        value = value.replace(' ', '').replace('-', '')

        # 1. Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid.
        country_code = value[:2]
        if country_code in self.validation_countries:
            if self.validation_countries[country_code] != len(value):
                raise ValidationError(_('{0} IBANs must contain {1} characters.'
                                        ''.format(country_code, self.validation_countries[country_code])))

        else:
            raise ValidationError(_('{0} is not a valid country code for IBAN.'.format(country_code)))

        if self.include_countries and country_code not in self.include_countries:
            raise ValidationError(_('{0} IBANs are not allowed in this field.'.format(country_code)))

        # 2. Move the four initial characters to the end of the string.
        value = value[4:] + value[:4]

        # 3. Replace each letter in the string with two digits, thereby expanding the string, where
        #    A = 10, B = 11, ..., Z = 35.
        value_digits = ''
        for x in value:
            ord_value = ord(x)
            if 48 <= ord_value <= 57:  # 0 - 9
                value_digits += x
            elif 65 <= ord_value <= 90:  # A - Z
                value_digits += str(ord_value - 55)
            else:
                raise ValidationError(_('{0} is not a valid character for IBAN.'.format(x)))

        # 4. Interpret the string as a decimal integer and compute the remainder of that number on division by 97.
        if int(value_digits) % 97 != 1:
            raise ValidationError(_('Not a valid IBAN.'))
