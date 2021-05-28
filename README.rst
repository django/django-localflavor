==================
django-localflavor
==================

.. image:: https://img.shields.io/pypi/v/django-localflavor.svg
   :target: https://pypi.python.org/pypi/django-localflavor

.. image:: https://img.shields.io/travis/django/django-localflavor.svg
    :target: http://travis-ci.org/django/django-localflavor

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

For a full list of available localflavors, see
https://django-localflavor.readthedocs.io/

django-localflavor can also be found on and installed from the Python
Package Index: https://pypi.python.org/pypi/django-localflavor

**Release Overview**

You're encouraged to use the latest version of this package unless you need
support for an unsupported version of Django.

**2021-05-28 - 3.1**: Django 2.2, 3.0, 3.1 & 3.2

This release contains breaking data changes for the MX and IN flavors.
Please see the changelog for details:
https://github.com/django/django-localflavor/blob/3.1/docs/changelog.rst

**2020-02-19 - 3.0**: Django 2.2 & 3.0

All deprecated code has been removed in this release. This release also includes a number of other breaking changes.
Please see the changelog for details:
https://github.com/django/django-localflavor/blob/3.0/docs/changelog.rst

**2019-05-07 - 2.2**: Django 1.11 - 2.2

All deprecated code will be removed in the 3.0 release. Please run you project's tests using `python -Wd` so that
deprecation warnings appear and can be addressed. See changelog for details.

**2018-08-24 - 2.1**: Django 1.11 - 2.1

**2017-12-30 - 2.0**: Django 1.11 - 2.0

All deprecated code has been removed in this release. See changelog for details.

**2017-11-22 - 1.6**: Django 1.8 - 1.11

All deprecated code will be removed in the next release. Please run you project's tests using `python -Wd` so that
deprecation warnings appear and can be addressed.

**2017-05-26 - 1.5**: Django 1.8 - 1.11

**2017-01-03 - 1.4**: Django 1.8 - 1.10

**2016-05-06 - 1.3**: Django 1.7 - 1.9

**2015-11-27 - 1.2**: Django 1.5 - 1.9

**2014-12-10 - 1.1**: Django 1.5 - 1.7

**2013-07-29 - 1.0**: Django 1.5 - 1.6

