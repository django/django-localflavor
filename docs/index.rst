======================
The "local flavor" app
======================

.. module:: localflavor
    :synopsis: A collection of various Django snippets that are useful only for
               a particular country or culture.

django-localflavor is a collection of assorted pieces of code that are
useful for particular countries or cultures. These are called the
"local flavor" add-ons and live in the :mod:`localflavor` package.

Inside that package, country- or culture-specific code is organized into
subpackages, named using `ISO 3166 country codes`_.

Most of the ``localflavor`` add-ons are localized form components deriving
from the forms framework -- for example,
a :class:`~localflavor.us.forms.USStateField` that knows how to validate
U.S. state abbreviations, and a
:class:`~localflavor.fi.forms.FISocialSecurityNumber` that knows how to
validate Finnish social security numbers.

To use one of these localized components, just import the relevant subpackage.
For example, here's how you can create a form with a field representing a
French telephone number::

    from django import forms
    from localflavor.fr.forms import FRPhoneNumberField

    class MyForm(forms.Form):
        my_french_phone_no = FRPhoneNumberField()

.. toctree::
   :maxdepth: 1
   :glob:

   localflavor/*
   generic

The ``localflavor`` package also includes a :doc:`generic </generic>` subpackage,
containing useful code that is not specific to one particular country or culture.
Currently, it defines date, datetime and split datetime input fields based on
those from the forms, but with non-US default formats. Here's an example of
how to use them::

    from django import forms
    from localflavor import generic

    class MyForm(forms.Form):
        my_date_field = generic.forms.DateField()

Installation
============

To install django-localflavor use your favorite packaging tool, e.g.pip::

    pip install django-localflavor

Or download the source distribution from PyPI_ at
https://pypi.python.org/pypi/django-localflavor, decompress the file and
run ``python setup.py install`` in the unpacked directory.

Then add ``'localflavor'`` to your :setting:`INSTALLED_APPS` setting.

.. _PyPI: https://pypi.python.org/

Internationalization
====================

Localflavor has its own catalog of translations, in the directory
``localflavor/locale``, and it's not loaded automatically like Django's
general catalog in ``django/conf/locale``. If you want localflavor's
texts to be translated, like form fields error messages, you must include
:mod:`localflavor` in the :setting:`INSTALLED_APPS` setting, so
the internationalization system can find the catalog, as explained in
:ref:`django:how-django-discovers-translations`.

Adding flavors
==============

We'd love to add more of these, so please `create a ticket`_ with
any code you'd like to contribute. One thing we ask is that you please use
Unicode objects (``u'mystring'``) for strings, rather than setting the encoding
in the file. See any of the existing flavors for examples.

.. _create a ticket: https://github.com/django/django-localflavor/issues

Backwards compatibility
=======================

We will always attempt to make :mod:`localflavor` reflect the officially
gazetted policies of the appropriate local government authority. For example,
if a government body makes a change to add, alter, or remove a province
(or state, or county), that change will be reflected in localflavor in the
next release.

When a backwards-incompatible change is made (for example, the removal
or renaming of a province) the localflavor in question will raise a
warning when that localflavor is imported. This provides a runtime
indication that something may require attention.

However, once you have addressed the backwards compatibility (for
example, auditing your code to see if any data migration is required),
the warning serves no purpose. The warning can then be supressed.
For example, to suppress the warnings raised by the Indonesian
localflavor you would use the following code::

    import warnings
    warnings.filterwarnings('ignore',
                            category=RuntimeWarning,
                            module='localflavor.id')
    from localflavor.id import forms as id_forms

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _ISO 3166 country codes: http://www.iso.org/iso/country_codes.htm
