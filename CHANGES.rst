CHANGES
=======

tip   (unreleased)
------------------

New flavors:

- Add local flavor for Pakistan (gh-41)
- Add local flavor for Denmark (gh-83)
- Add local flavor for Latvia (gh-68)
- Add local flavor for Estonia (gh-70)
- Add local flavor for Malta (gh-88)

New fields for existing flavors:

- Add model field for states of Brazil (gh-22)
- Add form field for Indian Aadhaar numbers (gh-23)
- Add model field for states of India (gh-23)
- Add form field for Lithuanian phone numbers
- Add model field for Dutch bank accounts (gh-42)
- Add form field for Italian phone numbers (gh-74)
- Add form field for French National Identification Number (gh-75)
- Add IBAN model and form fields (gh-86)
- Add SSN model field for US (gh-96)

Other modifications to existing flavors:

- Add Ceuta and Mellila to regions of Spain (gh-8)
- Support 14x phone numbers for China (gh-17)
- Support entities in Italian SSN form field (gh-20)
- Add Japanese prefecture codes and fix prefecture order (gh-27)
- Allow spaces in CPF numbers for Brazil (gh-32)
- US SSN starting with 9 is rejected (gh-35)
- Fix REGON number validation for Poland (gh-62)
- Add normalization for Lithuanian postal code field (gh-69)
- Strip whitespace from US ZIP code field (gh-77)
- Fix CIF validation for Spain (gh-78)
- Fixed armed forces "states" for US (gh-8)
- Allow customizing French form field labels (gh-102)
- Invalidate Brazilian CPF number when all numbers all numbers are equal (gh-103)
- Add mapping between provinces and regions for Italy (gh-105)
- Add Telengana to states of India (gh-107)


1.0.0 (2013-07-29)
------------------

Initial release
