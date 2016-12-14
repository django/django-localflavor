Changelog
=========

1.4   (unreleased)
------------------

New flavors:

- Added local flavor for Venezuela
  (`gh-245 <https://github.com/django/django-localflavor/pull/245>`_)
- Added local flavor for Morocco
  (`gh-270 <https://github.com/django/django-localflavor/pull/270>`_)

New fields for existing flavors:

- Added MXCLABEField model and form fields.
  (`gh-227 <https://github.com/django/django-localflavor/pull/227>`_).
- Added AUTaxFileNumberField model and form fields.
  (`gh-238 <https://github.com/django/django-localflavor/pull/238>`_)
- Added KWGovernorateSelect field to easily select Kuwait governorates.
  (`gh-231 <https://github.com/django/django-localflavor/pull/231>`_).
- Added FRRegion2016Select field to stick to current legislation
  (`gh-260 <https://github.com/django/django-localflavor/pull/260>`_)
  and (`gh-268 <https://github.com/django/django-localflavor/pull/268>`_).

Modifications to existing flavors:

- Enhancements of localflavor.br.forms.BRCNPJField
  (`gh-240 <https://github.com/django/django-localflavor/pull/240>`_
  `gh-254 <https://github.com/django/django-localflavor/pull/254>`_).
- Fixed century bug with Kuwait Civil ID verification localflavor.kw.forms
  (`gh-195 <https://github.com/django/django-localflavor/pull/195>`_).
- Allow passing field name as first positional argument of IBANField.
  (`gh-236 <https://github.com/django/django-localflavor/pull/236>`_).
- Fixed French FRNationalIdentificationNumber bug with imaginary birth month values.
  (`gh-242 <https://github.com/django/django-localflavor/pull/242>`_).
- Fixed French FRNationalIdentificationNumber bug with corsican people born after 2000.
  (`gh-242 <https://github.com/django/django-localflavor/pull/242>`_).
- Fixed the translation for US state 'Georgia' from colliding with the country 'Georgia'
  (`gh-250 <https://github.com/django/django-localflavor/pull/250>`_).
- Fixed the styling errors and enabled prospector
  (`gh-259 <https://github.com/django/django-localflavor/pull/259>`_).
- Allow AU ABN value with spaces to validate
  (`gh-266 <https://github.com/django/django-localflavor/issues/266>`_
  `gh-267 <https://github.com/django/django-localflavor/pull/267>`_).

Other changes:

- Drop support for Django 1.7
  (`gh-218 <https://github.com/django/django-localflavor/pull/218>`_).
- Ensure the migration framework generates schema migrations for model fields that change the max_length
  (`gh-257 <https://github.com/django/django-localflavor/pull/257>`_). Users will need to generate migrations for any
  model fields they use with 'makemigrations'.
- Lazily generate US_STATES, STATE_CHOICES, and USPS_CHOICES
  (`gh-203 <https://github.com/django/django-localflavor/issues/203>`_
  `gh-272 <https://github.com/django/django-localflavor/pull/272>`_).
- Deprecated Phone Number fields
  (`gh-262 <https://github.com/django/django-localflavor/pull/262>`_).
- Bumped versions of requirements for testing
  (`gh-274 <https://github.com/django/django-localflavor/pull/274>`_).


1.3   (2016-05-06)
------------------

New flavors:

- Added local flavor for Bulgaria
  (`gh-191 <https://github.com/django/django-localflavor/pull/191>`_)
- Added local flavor for Tunisia
  (`gh-141 <https://github.com/django/django-localflavor/pull/141>`_)
- Added local flavor for Hungary
  (`gh-213 <https://github.com/django/django-localflavor/pull/213>`_)

New fields for existing flavors:

- Added ARCBUField form field.
  (`gh-151 <https://github.com/django/django-localflavor/pull/151>`_).
- Added NLZipCodeField, NLProvinceField, NLSoFiNumberField, NLPhoneNumberField model fields.
  (`gh-152 <https://github.com/django/django-localflavor/pull/152>`_).
- Added AUBusinessNumberField model and form fields.
  (`gh-63 <https://github.com/django/django-localflavor/pull/63>`_)

Modifications to existing flavors:

- Moved Dutch validators from localflavor.nl.forms to localflavor.nl.validators
  (`gh-152 <https://github.com/django/django-localflavor/pull/152>`_).
- Fix check for promotional social security numbers in USSocialSecurityNumberField
  (`gh-157 <https://github.com/django/django-localflavor/pull/157>`_).
- Updated IBANField to support the latest additions to the IBAN Registry (version 64 / March 2016).
- Fix bug with MXRFCField where some incorrect values would validate correctly.
  (`gh-204 <https://github.com/django/django-localflavor/issues/204>`_).
- Fixed bug with IBANFormField validation.
  (`gh-215 <https://github.com/django/django-localflavor/pull/215>`_).
- Update regex in DEZipCodeField to prohibit invalid postal codes.
  (`gh-216 <https://github.com/django/django-localflavor/pull/216>`_).
- Added deconstructor methods to validators.
  (`gh-220 <https://github.com/django/django-localflavor/pull/220>`_).
- Fix bug in ESIdentityCardNumberField where some valid values for NIE numbers were not
  validating.
  (`gh-217 <https://github.com/django/django-localflavor/pull/217>`_)
- Add deconstruct method to all model fields
  (`gh-162 <https://github.com/django/django-localflavor/pull/162>`_
  `gh-224 <https://github.com/django/django-localflavor/pull/224>`_).

Other changes:

- Drop support for Django 1.5, Django 1.6 and Python 2.6
  (`gh-170 <https://github.com/django/django-localflavor/pull/170>`_).

1.2   (2015-11-27)
------------------

New flavors:

- None

New fields for existing flavors:

- Added form field for Estonian business registration codes
  (`gh-135 <https://github.com/django/django-localflavor/pull/135>`_).
- Added model field for Ecuadorian provinces
  (`gh-138 <https://github.com/django/django-localflavor/pull/138>`_).
- Added form field for Swiss Social Security numbers (
  (`gh-155 <https://github.com/django/django-localflavor/pull/155>`_).
- Added form field for Brazilian Legal Process numbers (Processo)
  (`gh-163 <https://github.com/django/django-localflavor/pull/163>`_).

Modifications to existing flavors:

- Fixed misspelled Polish administrative unit names
  (`gh-136 <https://github.com/django/django-localflavor/pull/136>`_).
- Added Kosovo and Timor-Leste to list of IBAN countries
  (`gh-139 <https://github.com/django/django-localflavor/pull/139>`_).
- Fixed error in Romanian fiscal identity code (CIF) field when value has a trailing slash
  (`gh-146 <https://github.com/django/django-localflavor/pull/146>`_).
- Updated validation in Swiss postal code field to only accept values in the range 1000 - 9000
  (`gh-154 <https://github.com/django/django-localflavor/pull/154>`_).
- Added validator for International Article Number (EAN) to the generic module
  (`gh-156 <https://github.com/django/django-localflavor/pull/156>`_).
- Updated Italian social security number field to use 'tax code' in error message
  (`gh-167 <https://github.com/django/django-localflavor/pull/167>`_).
- Fixed error in Greek tax number code field when value has only alpha characters
  (`gh-171 <https://github.com/django/django-localflavor/pull/171>`_).
- Added stricter validation in the Brazilian Cadastro de Pessoas Físicas (CPF) field
  (`gh-172 <https://github.com/django/django-localflavor/pull/172>`_).
- Corrected Romanian counties choice names to use ș and ț (comma below)
  (`gh-175 <https://github.com/django/django-localflavor/pull/175>`_).
- Updated Brazilian postal code field to also accept values with XX.XXX-XXX and XXXXXXXX formats
  (`gh-177 <https://github.com/django/django-localflavor/pull/177>`_).
- Marked US state names for translation
  (`gh-178 <https://github.com/django/django-localflavor/pull/178>`_).
- Fixed French national identification number validation for people born before 1976 in Corsica
  (`gh-186 <https://github.com/django/django-localflavor/pull/186>`_).

1.1   (2014-12-10)
------------------

New flavors:

- Added local flavor for Denmark (gh-83)
- Added local flavor for Estonia (gh-70)
- Added local flavor for Latvia (gh-68)
- Added local flavor for Malta (gh-88)
- Added local flavor for Pakistan (gh-41)
- Added local flavor for Singapore (gh-119)

New fields for existing flavors:

- Added model and form fields for French SIREN/SIRET numbers (gh-123)
- Added model field for states of Brazil (gh-22)
- Added form field for Indian Aadhaar numbers (gh-23)
- Added model field for states of India (gh-23)
- Added form field for Lithuanian phone numbers
- Added model field for Dutch bank accounts (gh-42)
- Added form field for Italian phone numbers (gh-74)
- Added form field for French National Identification Number (gh-75)
- Added IBAN model and form fields (gh-86)
- Added BIC model and form fields (gh-125)
- Added SSN model field for US (gh-96)
- Added ZIP code model field for US (gh-55)

Other modifications to existing flavors:

- *backward incompatible* Updated the region lists of Great Britain (gh-43, gh-126)
- Added Ceuta and Mellila to regions of Spain (gh-8)
- Added support entities in Italian SSN form field (gh-20)
- Added Japanese prefecture codes and fix prefecture order (gh-27)
- Added normalization for Lithuanian postal code field (gh-69)
- Added whitespace stripping whitespace from US ZIP code field (gh-77)
- Added an option for customizing French form field labels (gh-102)
- Added mapping between provinces and regions for Italy (gh-105)
- Added Telengana to states of India (gh-107)
- Added support for 14X and 17X Chinese cell numbers (gh-17, gh-120)
- Allowed spaces in CPF numbers for Brazil (gh-32)
- Fixed CIF validation for Spain (gh-78)
- Fixed armed forces "states" for US (gh-8)
- Fixed REGON number validation for Poland (gh-62)
- Rejected US SSN starting with 9 (gh-35)
- Rejected Brazilian CPF number when all numbers all numbers are equal (gh-103)
- Added 'Y' to the NIE number validation for Spain (gh-127)
- Updated Argentina's CUIT number validation to support legal types 24 and 33 (gh-121)
- Added 'R', 'V' and 'W' to the Spanish identity card number validation (gh-132)

Other changes:

- Added checksums module (from Django) providing a Luhn validator (gh-122)

1.0 (2013-07-29)
----------------

Initial release
