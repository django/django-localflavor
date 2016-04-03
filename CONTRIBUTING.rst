==================================
Contributing to django-localflavor
==================================

As an open source project, django-localflavor welcomes contributions of many
forms, similar to its origin in the Django framework.

Examples of contributions include:

* Code patches
* Documentation improvements
* Bug reports and patch reviews

Extensive contribution guidelines are available online at:

    https://docs.djangoproject.com/en/dev/internals/contributing/

`File a ticket`__ to suggest changes or send pull requests.

django-localflavor uses Github's issue system to keep track of bugs, feature
requests, and pull requests for patches.

Running tests is as simple as `installing Tox`__ and running it in the root
Git clone directory::

    $ git clone https://github.com/django/django-localflavor
    [..]
    $ cd django-localflavor
    $ tox
    [..]
      congratulations :)

The previous command will run the tests in different combinations of Python
(if available) and Django versions. To see the full list of combinations use
the ``-l`` option::

    $ tox -l
    docs
    py27-1.7
    py27-1.8
    py32-1.7
    py32-1.8
    py33-1.7
    py33-1.8
    py34-1.7
    py34-1.8
    py27-master
    py34-master

You can run each environment with the ``-e`` option::

    $ tox -e py27-1.7  # runs the tests only on Pyton 2.7 and Django 1.7.x

Optionally you can also specify a country whose tests you want to run::

    $ COUNTRY=us tox

And combine both options::

    $ COUNTRY=us tox -e py27-1.7

Pull Request Review Checklist
=============================

- [ ] Prefix the country code to all fields.
- [ ] Field names should be easily understood by developers from the
      target localflavor country. This means that English translations
      are usually not the best name unless it's for something standard
      like postal code, phone number, tax / VAT ID etc.
- [ ] Prefer '<country code>PostalCodeField' for postal codes as it's
      international English; ZipCode is a term specific to the United
      States postal system.
- [ ] There must be meaningful tests. 100% test coverage is not required
      but all validation edge cases should be covered.
- [ ] Add `.. versionadded:: <next-version>` comment markers to new
      localflavors.
- [ ] Add documentation for any new fields you add.
- [ ] Add an entry to the docs/changelog.rst describing the change.
- [ ] Add an entry for your name in the the docs/authors.rst file.

__ https://github.com/django/django-localflavor/issues
__ http://tox.readthedocs.org/en/latest/install.html
