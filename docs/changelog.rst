Changelog
=========

4.0   (unreleased)
------------------

New flavors:

- None

New fields for existing flavors:

- None

Modifications to existing flavors:

- Fix error code for BRPostalCodeValidator
  (`gh-448 <https://github.com/django/django-localflavor/pull/448>`_).
- Fix spelling of the India state of Chhattisgarh
  (`gh-444 <https://github.com/django/django-localflavor/pull/444>`_).
- Fix CURP regex for MX flavor
  (`gh-449 <https://github.com/django/django-localflavor/pull/449>`_).

Other changes:

- None



3.1   (2021-05-28)
------------------

Breaking data changes:

A schema and data migration are required for users of `mx.models.MXStateField` and `mx.forms.MXStateSelect`. The
following steps are required:

    - run `manage.py makemigrations` to generate a schema migration
    - migrate `DIF` to `CDMX` with a data migration

A data migration is required for users of `in_.models.INStateField` and `in_.forms.INStateSelect`. The following data
migrations are required:

    - Migrate `CG` to `CT` for Chattisgarh
    - Migrate `UA` to `UT` for Uttarakhand
    - Migrate `DD` and `DN` to `DH` for Dadra and Nagar Haveli and Daman and Diu

A warning message will be displayed when `mx.models.MXStateField`, `mx.forms.MXStateSelect`, `in_.models.INStateField`
or `in_.forms.INStateSelect` are used. See the
`localflavor online docs <https://django-localflavor.readthedocs.io/en/latest/#backwards-compatibility>`_ for
instructions on how to suppress this warning once the migration has been completed.

New flavors:

- None

New fields for existing flavors:

- None

Modifications to existing flavors:

- Fix `fr.forms.FRNationalIdentificationNumber` validation for people born overseas
  (`gh-415 <https://github.com/django/django-localflavor/issues/415>`_).
- Breaking data change: Updated Indian states and union territories names and code as per iso 3166
  (https://www.iso.org/obp/ui/#iso:code:3166:IN). The key for Chattisgarh has been changed from CG to CT, the key for
  Uttarakhand has been changed from UA to UT, and the keys DD (Dadra and Nagar Haveli) and DN (Daman and Diu) have been
  removed and combined into DH (Dadra and Nagar Haveli and Daman and Diu). Ladakh (LA) is the new addition in the Union
  Territories. There are also a few modifications in the States and Union Territories names: Orissa (OR) is now Odisha
  (OR), Pondicherry (PY) is now Puducherry (PY) Andaman and Nicobar (AN) is now Andaman and Nicobar Islands (AN).
  (`gh-427 <https://github.com/django/django-localflavor/issues/427>`_).
- Correct sorting of US_STATES to sort by full name rather than code
  (`gh-424 <https://github.com/django/django-localflavor/issues/424>`_
  `gh-428 <https://github.com/django/django-localflavor/pull/428>`_).
- Added new region for CL
  (`gh-432 <https://github.com/django/django-localflavor/issues/432>`_,
  `gh-433 <https://github.com/django/django-localflavor/pull/433>`_).
- Updated IBAN validation for changes in IBAN Registry release 89, March 2021
  (`gh-436 <https://github.com/django/django-localflavor/issues/436>`_).
- Breaking data change: `mx.mx_states.STATE_CHOICES` has been updated to change DIF/Distrito Federal to CDMX/Ciudad de
  México, the legal name for this state as of 29 January 2016
  (`gh-235 <https://github.com/django/django-localflavor/issues/235>`_,
  `gh-400 <https://github.com/django/django-localflavor/issues/400>`_,
  `gh-438 <https://github.com/django/django-localflavor/issues/438>`_).

Other changes:

- Extended validation of BICs to match official SEPA regulations
  (`gh-418 <https://github.com/django/django-localflavor/issues/418>`_).
- Removed positional arguments (`*args`) from form fields that inherit from Django's
  `forms.CharField` and `forms.Field`. Positional arguments are not supported in the
  the parent form and did not work
  `gh-421 <https://github.com/django/django-localflavor/pull/421>`_).
- Added error codes to all `ValidationError`s as recommended by
  `Django's form validation documentation <https://docs.djangoproject.com/en/stable/ref/forms/validation/#raising-validationerror>`_
  (`gh-440 <https://github.com/django/django-localflavor/issues/440>`_).
- Renamed zh_CN and zh_TW locales to zh_Hans and zh_Hant respectively to match
  the Django locale names.


3.0   (2020-02-19)
------------------

Breaking changes:

Dropped support for Django < 2.2.

The deprecated `generic.checksums.luhn` and `generic.checksums.ean` functions have been removed in this release. Please
use `python-stdnum <https://arthurdejong.org/python-stdnum/>`_ instead.

Some Icelandic postcodes in `IS_POSTALCODES` have had their spelling updated, and some entries have been removed
entirely. A warning message will be displayed when `is_.forms.ISPostalCodeSelect` is used. See the
`localflavor online docs <https://django-localflavor.readthedocs.io/en/latest/#backwards-compatibility>`_ for
instructions on how to suppress this warning once any incompatibilities have been dealt with.

A data migration is required for users of `it.forms.ITRegionProvinceSelect`. The `CI`, `VS`, `OG`, and `OT` keys need to
be migrated to `SU` to account for the 2016 Italian provincial changes. Users wishing to maintain compatibility with the
old provincial structure will need to create a custom version of `it.forms.ITRegionProvinceSelect`. A warning message
will be displayed when `it.forms.ITRegionProvinceSelect` is used. See the
`localflavor online docs <https://django-localflavor.readthedocs.io/en/latest/#backwards-compatibility>`_ for
instructions on how to suppress this warning once the migration has been completed.

Using positional arguments with fields that inherit from Django's `forms.RegexField` previously only worked with Django
1.11 but were ignored with Django >= 2.0. Positional arguments have now been removed from all fields that inherit from
Django's `forms.RegexField`. Any options needed on the parent `forms.RegexField`, `forms.CharField` or `forms.Field`
must now be set with keyword arguments.

New flavors:

- Egypt local flavor
- Malaysia local flavor

New fields for existing flavors:

- None

Modifications to existing flavors:

- Extended Danish `DK_POSTALCODES` with small Danish islands getting independent post code since 2017
  (`gh-380 <https://github.com/django/django-localflavor/pull/380>`_).
- Switched incorrect `ar.forms.ARCBUField` implementation to use
  `python-stdnum <https://arthurdejong.org/python-stdnum/>`_ instead
  (`gh-391 <https://github.com/django/django-localflavor/pull/391>`_).
- Use set value of `strip` in fields that inherit from `django.forms.CharField`
  (`gh-392 <https://github.com/django/django-localflavor/pull/392>`_):

  - `gb.forms.GBPostcodeField`
  - `si.forms.SIEMSOField`
  - `si.forms.SITaxNumberField`
  - `za.forms.ZAIDField`

- Updated Icelandic `IS_POSTALCODES` with missing entries, updated spelling of entries, and removed non-existing ones.
  See breaking changes notice above (`gh-394 <https://github.com/django/django-localflavor/pull/394>`_).
- Add Kalimantan Utara in  `PROVINCE_CHOICES` for Indonesia local flavor
  (`gh-385 <https://github.com/django/django-localflavor/pull/385>`_).
- Add validation for women National identity number for Indonesia localflavor
  (`gh-386 <https://github.com/django/django-localflavor/pull/386>`_).
- Updated `ITRegionProvinceSelect` for 2016 Italian provincial changes. See breaking changes notice above
  (`gh-378 <https://github.com/django/django-localflavor/pull/378>`_,
  `gh-402 <https://github.com/django/django-localflavor/pull/402>`_).
- Use the value returned by clean() in the following fields
  (`gh-401 <https://github.com/django/django-localflavor/pull/401>`_,
  `gh-403 <https://github.com/django/django-localflavor/pull/403>`_):

  - `ca.forms.CAProvinceField`
  - `ca.forms.CASocialInsuranceNumberField`
  - `ch.forms.CHIdentityCardNumberField`
  - `cl.forms.CLRutField`
  - `cn.forms.CNIDCardField`
  - `cu.forms.CURegionField`
  - `cu.forms.CUProvinceField`
  - `cz.forms.CZBirthNumberField`
  - `cz.forms.CZICNumberField`
  - `de.forms.DEIdentityCardNumberField`
  - `ee.forms.EEPersonalIdentificationCode`
  - `eg.forms.EGNationalIDNumberField`
  - `es.forms.ESIdentityCardNumberField`
  - `es.forms.ESCCCField`
  - `fi.forms.FISocialSecurityNumber`
  - `fr.forms.FRNationalIdentificationNumber`
  - `fr.forms.FRSIRENField`
  - `fr.forms.FRSIRETField`
  - `gr.forms.GRTaxNumberCodeField`
  - `gr.forms.GRSocialSecurityNumberCodeField`
  - `hr.forms.HRJMBGField`
  - `hr.forms.HROIBField`
  - `hr.forms.HRLicensePlateField`
  - `hr.forms.HRPostalCodeField`
  - `hr.forms.HRJMBAGField`
  - `id.forms.IDPostCodeField`
  - `id.forms.IDLicensePlateField`
  - `id.forms.IDNationalIdentityNumberField`
  - `kw.forms.KWCivilIDNumberField`
  - `lt.forms.LTIDCodeField`
  - `lv.forms.LVPersonalCodeField`
  - `no.forms.NOSocialSecurityNumber`
  - `nz.forms.NZBankAccountNumberField`
  - `pl.forms.PLPESELField`
  - `pl.forms.PLNationalIDCardNumberField`
  - `pl.forms.PLNIPField`
  - `pl.forms.PLREGONField`
  - `pt.forms.PTCitizenCardNumberField`
  - `pt.forms.PTSocialSecurityNumberField`
  - `ro.forms.ROCountyField`
  - `sg.forms.SGNRICFINField`
  - `si.forms.SIEMSOField`
  - `si.forms.SITaxNumberField`
  - `tr.forms.TRIdentificationNumberField`
  - `us.forms.USSocialSecurityNumberField`
  - `us.forms.USStateField`
  - `za.forms.ZAIDField`

- Removed unused positional arguments from fields that inherit from `forms.RegexField`
  (`gh-405 <https://github.com/django/django-localflavor/pull/405>`_).

Other changes:

- Removed deprecated `generic.checksums.luhn` and `generic.checksums.ean` functions
  (`gh-379 <https://github.com/django/django-localflavor/pull/379>`_).


2.2   (2019-05-07)
------------------

All deprecated code will be removed in the next release (3.0). Please run you project's tests using `python -Wd` so that
deprecation warnings appear and can be addressed.

New flavors:

- Added local flavor for Iran
  (`gh-359 <https://github.com/django/django-localflavor/pull/359>`_).

New fields for existing flavors:

- Added `BRPostalCodeField`, `BRCPFField` and `BRCNPJField` models fields
  (`gh-365 <https://github.com/django/django-localflavor/pull/365>`_).
- Added `EircodeField` in IE flavor
  (`gh-360 <https://github.com/django/django-localflavor/pull/360>`_)
  (`gh-366 <https://github.com/django/django-localflavor/pull/366>`_).
- Added Models for Spain (`ESPostalCodeField` and `ESIdentityCardNumberField`)
  (`gh-357 <https://github.com/django/django-localflavor/pull/357>`_)
  (`gh-372 <https://github.com/django/django-localflavor/pull/372>`_).

Modifications to existing flavors:

- Deprecated `generic.checksums.luhn` and `generic.checksums.ean`. Please use the python-stdnum library instead.
  (`gh-370 <https://github.com/django/django-localflavor/pull/370>`_).

Other changes:

- Added dependency on python-stdnum which is currently used for Luhn and EAN validation in several local-flavors
  (`gh-370 <https://github.com/django/django-localflavor/pull/370>`_).
- Added support for Vatican IBAN
  (`gh-355 <https://github.com/django/django-localflavor/pull/355>`_).
- Extended validation of BICs to check for the correct character set
  (`gh-364 <https://github.com/django/django-localflavor/pull/364>`_).
- Run tests for Django 2.2 and Python 3.5, 3.6 and 3.7
  (`gh-368 <https://github.com/django/django-localflavor/pull/368>`_).
- Run tests for Django 2.0 and Python 3.7
  (`gh-368 <https://github.com/django/django-localflavor/pull/368>`_).


2.1   (2018-08-24)
------------------

New flavors:

- Added local flavor for Moldova
  (`gh-309 <https://github.com/django/django-localflavor/pull/309>`_).

New fields for existing flavors:

- `NLLicensePlateField` in NL flavor
  (`gh-327 <https://github.com/django/django-localflavor/pull/327>`_).
- `GRSocialSecurityNumberField` (AMKA) in GR flavor
  (`gh-337 <https://github.com/django/django-localflavor/pull/337>`_).

Modifications to existing flavors:

- Allowed invalid message to be overridden in ESIdentityCardNumberField
  (`gh-339 <https://github.com/django/django-localflavor/issues/339>`_).
- Fix COFA validation for USStateField
  (`gh-303 <https://github.com/django/django-localflavor/pull/303>`_)

Other changes:

- Added VAT identification number validator for all EU locales
  (`gh-324 <https://github.com/django/django-localflavor/pull/324>`_).
- Fix EAN validation when intermediate checksum is 10
  (`gh-331 <https://github.com/django/django-localflavor/issues/331>`_).
- Confirmed support for Django 2.1.
- Added 34 as a valid CUIT prefix value for `ARCUITField`
  (`gh-342 <https://github.com/django/django-localflavor/pull/342>`_).


2.0   (2017-12-30)
------------------

All deprecated code has been removed in this release. Specifically, all of the phone number fields have been removed
and we recommend that you use `django-phonenumber-field <https://github.com/stefanfoulis/django-phonenumber-field>`_
instead. If you need to use django-phonenumber-field with Django 2.0, you will need to use the version from the
`Django 2.0 support pull request <https://github.com/stefanfoulis/django-phonenumber-field/pull/196>`_ until this pull
request is merged.

A full list of the removed classes and functions is the "Other changes" section below.

New flavors:

- None

New fields for existing flavors:

- None

Modifications to existing flavors:

- Changed RUT to NIT in CONITField form field error message.
- Fixed validation of Czech birth numbers for birth dates after 1st January 1954
  (`gh-315 <https://github.com/django/django-localflavor/issues/315>`_).

Other changes:

- Added support for Django 2.0 and dropped support for Django < 1.11
  (`gh-310 <https://github.com/django/django-localflavor/pull/310>`_).
- Fixed README and changelog documentation about dropping Python 2 and Django 1.11.
- Removed all deprecated classes, functions and associated data / regular expressions.
  These are the classes and functions that have been removed
  (`gh-321 <https://github.com/django/django-localflavor/pull/321>`_):

  - `au.forms.AUPhoneNumberField`
  - `au.models.AUPhoneNumberField`
  - `be.forms.BEPhoneNumberField`
  - `br.forms.BRPhoneNumberField`
  - `br.forms.DV_maker`
  - `ca.forms.CAPhoneNumberField`
  - `ch.forms.CHPhoneNumberField`
  - `cn.forms.CNPhoneNumberField`
  - `cn.forms.CNCellNumberField`
  - `dk.forms.DKPhoneNumberField`
  - `es.forms.ESPhoneNumberField`
  - `fr.forms.FRPhoneNumberField`
  - `gr.forms.GRPhoneNumberField`
  - `gr.forms.GRMobilePhoneNumberField`
  - `hk.forms.HKPhoneNumberField` (`localflavor.hk` has been removed because it only contained this field)
  - `hr.forms.HRPhoneNumberField`
  - `hr.forms.HRPhoneNumberPrefixSelect`
  - `id_.forms.IDPhoneNumberField`
  - `il.forms.ILMobilePhoneNumberField`
  - `in.forms.INPhoneNumberField`
  - `is_.forms.ISPhoneNumberField`
  - `it.forms.ITPhoneNumberField`
  - `lt.forms.LTPhoneField`
  - `nl.forms.NLPhoneNumberField`
  - `nl.forms.NLSoFiNumberField`
  - `nl.models.NLBankAccountNumberField`
  - `nl.models.NLPhoneNumberField`
  - `nl.models.NLSoFiNumberField`
  - `nl.validators.NLBankAccountNumberFieldValidator`
  - `nl.validators.NLPhoneNumberFieldValidator`
  - `nl.validators.NLSoFiNumberFieldValidator`
  - `no.forms.NOPhoneNumberField`
  - `nz.forms.NZPhoneNumberField`
  - `pk.forms.PKPhoneNumberField`
  - `pk.models.PKPhoneNumberField`
  - `pt.forms.PTPhoneNumberField`
  - `ro.forms.ROIBANField`
  - `ro.forms.ROPhoneNumberField`
  - `sg.forms.SGPhoneNumberField`
  - `sg.forms.SGNRIC_FINField`
  - `si.forms.SIPhoneNumberField`
  - `tr.forms.TRPhoneNumberField`
  - `us.forms.USPhoneNumberField`
  - `us.models.PhoneNumberField`

1.6   (2017-11-22)
------------------

All deprecated code will be removed in the next release. Please run you project's tests using `python -Wd` so that
deprecation warnings appear and can be addressed.

New flavors:

- Added local flavor for Cuba
  (`gh-292 <https://github.com/django/django-localflavor/pull/292>`_).

New fields for existing flavors:

- Added KWAreaSelect form field
  (`gh-296 <https://github.com/django/django-localflavor/pull/296>`_).
- Added CONITField form field
  (`gh-145 <https://github.com/django/django-localflavor/pull/145>`_).
- Added `nl.models.NLBSNField`, `nl.forms.NLBSNFormField` and `nl.validators.NLBSNFieldValidator`
  (`gh-314 <https://github.com/django/django-localflavor/pull/314>`_).

Modifications to existing flavors:

- Fixed crash with USZipCodeField form validation when null=True is allowed
  (`gh-295 <https://github.com/django/django-localflavor/pull/295>`_).
- Deprecated br.forms.DV_maker, sg.forms.SGNRIC_FINField, lt.forms.LTPhoneField
  and ro.forms.ROIBANField
  (`gh-305 <https://github.com/django/django-localflavor/pull/305>`_).
- Added support for Swedish interim personal identity numbers
  (`gh-308 <https://github.com/django/django-localflavor/pull/308>`_).
- Deprecated `nl.models.NLBankAccountNumberField`
  (`gh-307 <https://github.com/django/django-localflavor/pull/307>`_).
- Updated IBANField to support the latest additions to the IBAN Registry (version 78 / August 2017).
- Deprecated `nl.models.NLSoFiNumberField`, `nl.forms.NLSoFiNumberField` and `nl.validators.NLSoFiNumberFieldValidator`
  (`gh-314 <https://github.com/django/django-localflavor/pull/314>`_).
- Fixes issue with `no.forms.NOBankAccountNumber` unclean data
  (`gh-311 <https://github.com/django/django-localflavor/pull/311>`_).

Other changes:

- Added support for empty_value kwarg in Django >= 1.11
  (`gh-298 <https://github.com/django/django-localflavor/pull/298>`_).
- Dropped support for Python 3.2.

1.5   (2017-05-26)
------------------

New flavors:

- Added local flavor for Ukraine
  (`gh-273 <https://github.com/django/django-localflavor/pull/273>`_).

New fields for existing flavors:

- Added NOBankAccountNumber form field
  (`gh-275 <https://github.com/django/django-localflavor/pull/275>`_).
- Added AUCompanyNumberField model and form field
  (`gh-278 <https://github.com/django/django-localflavor/pull/278>`_).

Modifications to existing flavors:

- Added normalized versions of COFA state names for US
  (`gh-277 <https://github.com/django/django-localflavor/pull/277>`_).
- Fixed Dutch NLZipCodeField field not to store empty value as a single space
  (`gh-280 <https://github.com/django/django-localflavor/pull/280>`_).
- Fixed validation for old Australian tax file numbers
  (`gh-284 <https://github.com/django/django-localflavor/pull/284>`_).

Other changes:

- None

1.4   (2017-01-03)
------------------

New flavors:

- Added local flavor for Venezuela
  (`gh-245 <https://github.com/django/django-localflavor/pull/245>`_).
- Added local flavor for Morocco
  (`gh-270 <https://github.com/django/django-localflavor/pull/270>`_).

New fields for existing flavors:

- Added MXCLABEField model and form fields
  (`gh-227 <https://github.com/django/django-localflavor/pull/227>`_).
- Added AUTaxFileNumberField model and form fields
  (`gh-238 <https://github.com/django/django-localflavor/pull/238>`_).
- Added KWGovernorateSelect field to easily select Kuwait governorates.
  (`gh-231 <https://github.com/django/django-localflavor/pull/231>`_).
- Added FRRegion2016Select field to stick to current legislation
  (`gh-260 <https://github.com/django/django-localflavor/pull/260>`_).
  and (`gh-268 <https://github.com/django/django-localflavor/pull/268>`_).

Modifications to existing flavors:

- Enhancements of localflavor.br.forms.BRCNPJField
  (`gh-240 <https://github.com/django/django-localflavor/pull/240>`_
  `gh-254 <https://github.com/django/django-localflavor/pull/254>`_).
- Fixed century bug with Kuwait Civil ID verification localflavor.kw.forms
  (`gh-195 <https://github.com/django/django-localflavor/pull/195>`_).
- Allow passing field name as first positional argument of IBANField
  (`gh-236 <https://github.com/django/django-localflavor/pull/236>`_).
- Fixed French FRNationalIdentificationNumber bug with imaginary birth month values
  (`gh-242 <https://github.com/django/django-localflavor/pull/242>`_).
- Fixed French FRNationalIdentificationNumber bug with corsican people born after 2000
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
  (`gh-191 <https://github.com/django/django-localflavor/pull/191>`_).
- Added local flavor for Tunisia
  (`gh-141 <https://github.com/django/django-localflavor/pull/141>`_).
- Added local flavor for Hungary
  (`gh-213 <https://github.com/django/django-localflavor/pull/213>`_).

New fields for existing flavors:

- Added ARCBUField form field.
  (`gh-151 <https://github.com/django/django-localflavor/pull/151>`_).
- Added NLZipCodeField, NLProvinceField, NLSoFiNumberField, NLPhoneNumberField model fields
  (`gh-152 <https://github.com/django/django-localflavor/pull/152>`_).
- Added AUBusinessNumberField model and form fields
  (`gh-63 <https://github.com/django/django-localflavor/pull/63>`_).

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
  validating
  (`gh-217 <https://github.com/django/django-localflavor/pull/217>`_).
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
