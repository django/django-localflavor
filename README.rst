==================
django-localflavor
==================

.. image:: https://img.shields.io/pypi/v/django-localflavor.svg
   :target: https://pypi.org/project/django-localflavor/

.. image:: https://github.com/django/django-localflavor/actions/workflows/test.yml/badge.svg
    :target: https://github.com/django/django-localflavor/actions/workflows/test.yml

.. image:: https://img.shields.io/codecov/c/github/django/django-localflavor/master.svg
   :target: http://codecov.io/github/django/django-localflavor?branch=master

.. image:: https://readthedocs.org/projects/django-localflavor/badge/?version=latest&style=plastic
   :target: https://django-localflavor.readthedocs.io/en/latest/

Django's "localflavor" packages offer additional functionality for particular
countries or cultures. For example, these might include form fields for your
country's postal codes or government ID numbers.

This code used to live in Django proper -- in ``django.contrib.localflavor``
-- but was separated into a standalone package in Django 1.5 to keep the
framework's core clean.

django-localflavor no longer includes country specific phone number fields. The django-phonenumber-field package has
excellent support for validating phone numbers in many countries and we recommend this package.
https://pypi.org/project/django-phonenumber-field/


For a full list of available localflavors, see
https://django-localflavor.readthedocs.io/

django-localflavor can also be found on and installed from the Python
Package Index: https://pypi.org/project/django-localflavor/

**Release Overview**

You're encouraged to use the latest version of this package unless you need
support for an unsupported version of Django.

**2025-05-21 - 5.0**: Django 4.2, 5.0, 5.1 & 5.2

This release contains breaking data changes for the LV, NP and NO flavors.
Please see the changelog for details:
https://github.com/django/django-localflavor/blob/5.0/docs/changelog.rst

**2023-04-22 - 4.0**: Django 3.2, 4.0, 4.1 & 4.2

**2021-05-28 - 3.1**: Django 2.2, 3.0, 3.1 & 3.2

This release contains breaking data changes for the MX and IN flavors.
Please see the changelog for details:
https://github.com/django/django-localflavor/blob/3.1/docs/changelog.rst

**2020-02-19 - 3.0**: Django 2.2 & 3.0

All deprecated code has been removed in this release. This release also includes a number of other breaking changes.
Please see the changelog for details:
https://github.com/django/django-localflavor/blob/3.0/docs/changelog.rst

**2019-05-07 - 2.2**: Django 1.11 - 2.2

All deprecated code will be removed in the 3.0 release. Please run your project's tests using `python -Wd` so that
deprecation warnings appear and can be addressed. See changelog for details.

**2018-08-24 - 2.1**: Django 1.11 - 2.1

**2017-12-30 - 2.0**: Django 1.11 - 2.0
