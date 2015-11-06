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
    py26-1.5
    py26-1.6
    py27-1.5
    py27-1.6
    py32-1.5
    py32-1.6
    py33-1.5
    py33-1.6

You can run each environment with the ``-e`` option::

    $ tox -e py27-1.6  # runs the tests only on Pyton 2.7 and Django 1.6.x

Optionally you can also specify a country whose tests you want to run::

    $ COUNTRY=us tox

And combine both options::

    $ COUNTRY=us tox -e py27-1.6

__ https://github.com/django/django-localflavor/issues
__ http://tox.readthedocs.org/en/latest/install.html
