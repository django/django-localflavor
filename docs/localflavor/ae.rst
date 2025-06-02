United Arab Emirates (``ae``)
=============================

The UAE localflavor provides helpers for the most common address and
registration values used in local applications.

Highlights:

* ``UAEEmiratesIDField`` accepts Emirates ID numbers in either compact
  ``784YYYYNNNNNNNN`` form or formatted ``784-YYYY-NNNNNNN-N`` form and stores
  them in normalized dashed form.
* ``UAEPostalCodeField`` reflects local practice by allowing only ``00000`` or
  an empty value.
* ``UAEPOBoxField`` accepts plain numeric values as well as ``P.O. Box``,
  ``PO Box``, and ``POB`` prefixes.
* ``UAETaxRegistrationNumberField`` validates 15-digit VAT/TRN identifiers and
  strips embedded whitespace during cleaning.

Forms
-----

.. automodule:: localflavor.ae.forms
    :members:

Models
------

.. automodule:: localflavor.ae.models
    :members:

Data
----

.. autodata:: localflavor.ae.ae_emirates.EMIRATE_CHOICES

.. autodata:: localflavor.ae.ae_emirates.EMIRATES_NORMALIZED
