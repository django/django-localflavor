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

.. hlist::
   :columns: 4

   * :doc:`localflavor/ar`
   * :doc:`localflavor/at`
   * :doc:`localflavor/au`
   * :doc:`localflavor/be`
   * :doc:`localflavor/br`
   * :doc:`localflavor/ca`
   * :doc:`localflavor/ch`
   * :doc:`localflavor/cl`
   * :doc:`localflavor/cn`
   * :doc:`localflavor/co`
   * :doc:`localflavor/cz`
   * :doc:`localflavor/de`
   * :doc:`localflavor/dk`
   * :doc:`localflavor/ec`
   * :doc:`localflavor/ee`
   * :doc:`localflavor/es`
   * :doc:`localflavor/fi`
   * :doc:`localflavor/fr`
   * :doc:`localflavor/gb`
   * :doc:`localflavor/gr`
   * :doc:`localflavor/hk`
   * :doc:`localflavor/hr`
   * :doc:`localflavor/id_`
   * :doc:`localflavor/ie_`
   * :doc:`localflavor/il`
   * :doc:`localflavor/in_`
   * :doc:`localflavor/is_`
   * :doc:`localflavor/it`
   * :doc:`localflavor/jp`
   * :doc:`localflavor/kw`
   * :doc:`localflavor/lt`
   * :doc:`localflavor/lv`
   * :doc:`localflavor/mk`
   * :doc:`localflavor/mt`
   * :doc:`localflavor/mx`
   * :doc:`localflavor/nl`
   * :doc:`localflavor/no`
   * :doc:`localflavor/nz`
   * :doc:`localflavor/pe`
   * :doc:`localflavor/pk`
   * :doc:`localflavor/pl`
   * :doc:`localflavor/pt`
   * :doc:`localflavor/py_`
   * :doc:`localflavor/ro`
   * :doc:`localflavor/ru`
   * :doc:`localflavor/se`
   * :doc:`localflavor/si`
   * :doc:`localflavor/sk`
   * :doc:`localflavor/tr`
   * :doc:`localflavor/us`
   * :doc:`localflavor/uy`
   * :doc:`localflavor/za`

To use one of these localized components, just import the relevant subpackage.
For example, here's how you can create a form with a field representing a
French telephone number::

    from django import forms
    from localflavor.fr.forms import FRPhoneNumberField

    class MyForm(forms.Form):
        my_french_phone_no = FRPhoneNumberField()

The ``localflavor`` package also includes a :doc:`generic </generic>` subpackage,
containing useful code that is not specific to one particular country or culture.
This package defines date, datetime and split datetime input fields based on
those from the forms, but with non-US default formats. Here's an example of
how to use them::

    from django import forms
    from localflavor import generic

    class MyForm(forms.Form):
        my_date_field = generic.forms.DateField()

The ``localflavor`` generic package also has IBAN and BIC model and form fields.
Here's an example of how to use the IBAN and BIC form fields::

    from django import forms
    from localflavor.generic.forms import BICFormField, IBANFormField

    class MyForm(forms.Form):
        iban = IBANFormField()
        bic = BICFormField()

.. _ISO 3166 country codes: http://www.iso.org/iso/country_codes.htm

Installation
============

To install django-localflavor use your favorite packaging tool, e.g.pip::

    pip install django-localflavor

Or download the source distribution from PyPI_ at
https://pypi.python.org/pypi/django-localflavor, decompress the file and
run ``python setup.py install`` in the unpacked directory.

Then add ``'localflavor'`` to your :setting:`INSTALLED_APPS` setting::

    INSTALLED_APPS = (
        # ...
        'localflavor',
    )

.. note::

  Adding ``'localflavor'`` to your ``INSTALLED_APPS`` setting is required
  for South_ and translations to work. Using django-localflavor without
  adding it to your ``INSTALLED_APPS`` setting is not recommended.

.. _PyPI: https://pypi.python.org/
.. _South: http://south.aeracode.org/

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

See the `contributing documentation`_ for how to run the tests while working on a
local flavor.

If you consider adding a new localflavor for country here are some examples
that you might consider implementing:

- form fields and form widgets

  - ID verification
  - tax or social security number validator
  - car registration
  - zip code validation
  - phone number validation
  - country area selects, e.g. cities, counties, states, provinces

- model fields, e.g. for storing any of the above form fields' values

- local translations of English area names. Join your language team at
  Transifex: https://www.transifex.com/projects/p/django-localflavor/

.. _create a ticket: https://github.com/django/django-localflavor/issues
.. _contributing documentation: https://github.com/django/django-localflavor/blob/master/CONTRIBUTING.rst

Releases
========

Due to django-localflavor' history as a former contrib app, the app is
required to be working with the actively maintained Django versions. See
the documentation about `Django's release process`_ for more information.

django-localflavor releases are not tied to the release cycle of Django.
Version numbers follow the appropriate Python standards, e.g. PEPs 386_ and 440_.

.. _386: http://www.python.org/dev/peps/pep-0386/
.. _440: http://www.python.org/dev/peps/pep-0440/
.. _`Django's release process`: https://docs.djangoproject.com/en/dev/internals/release-process/

How to migrate
==============

If you've used the old ``django.contrib.localflavor`` package or one of the
temporary ``django-localflavor-*`` releases, follow these two easy steps to
update your code:

1. Install the third-party ``django-localflavor`` package.

2. Change your app's import statements to reference the new packages.

   For example, change this::

       from django.contrib.localflavor.fr.forms import FRPhoneNumberField

   ...to this::

       from localflavor.fr.forms import FRPhoneNumberField

   Or if you used one of the shortlived ``django-localflavor-*`` packages
   change::

       from django_localflavor_fr.forms import FRPhoneNumberField

   ...to this::

       from localflavor.fr.forms import FRPhoneNumberField

The code in the new package is the same (it was copied directly from Django),
so you don't have to worry about backwards compatibility in terms of
functionality. Only the imports have changed.

Backwards compatibility
=======================

We will always attempt to make :mod:`localflavor` reflect the officially
gazetted policies of the appropriate local government authority. For example,
if a government body makes a change to add, alter, or remove a province
(or state, or county), that change will be reflected in localflavor in the
next release.

When a backwards-incompatible change is made (for example, the removal
or renaming of a province) the localflavor in question will raise a
warning when that localflavor is imported. This provides a run-time
indication that something may require attention.

However, once you have addressed the backwards compatibility (for
example, auditing your code to see if any data migration is required),
the warning serves no purpose. The warning can then be suppressed.
For example, to suppress the warnings raised by the Indonesian
localflavor you would use the following code::

    import warnings
    warnings.filterwarnings('ignore',
                            category=RuntimeWarning,
                            module='localflavor.id')
    from localflavor.id import forms as id_forms

Indices and tables
==================

.. toctree::

    authors
    changelog

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :glob:
   :hidden:

   localflavor/*
   generic
