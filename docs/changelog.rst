Changelog
=========

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
- Updated Argentina's CUIT numer validation to support legal types 24 and 33 (gh-121)
- Added 'R', 'V' and 'W' to the Spanish identity card number validation (gh-132)

Other changes:

- Added checksums module (from Django) providing a Luhn validator (gh-122)

1.0 (2013-07-29)
----------------

Initial release
