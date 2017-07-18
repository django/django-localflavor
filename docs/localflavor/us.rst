United States of America (``us``)
=================================

Forms
-----

.. automodule:: localflavor.us.forms
    :members:

Models
------

.. automodule:: localflavor.us.models
    :members:

Data
----

.. autodata:: localflavor.us.us_states.CONTIGUOUS_STATES

.. autodata:: localflavor.us.us_states.NON_CONTIGUOUS_STATES

.. autodata:: localflavor.us.us_states.US_TERRITORIES

.. autodata:: localflavor.us.us_states.ARMED_FORCES_STATES

.. autodata:: localflavor.us.us_states.COFA_STATES

.. autodata:: localflavor.us.us_states.OBSOLETE_STATES

.. data:: localflavor.us.us_states.US_STATES
    :annotation: = CONTIGUOUS_STATES + NON_CONTIGUOUS_STATES

    All US states.

    This tuple is lazily generated and may not work as expected in all cases due
    to tuple optimizations in the Python interpreter which do not account for
    lazily generated tuples.  For example::

      US_STATES + ('XX', _('Select a State'))

    should work as expected, but::

      ('XX', _('Select a State')) + US_STATES

    may throw:

    ``TypeError: can only concatenate tuple (not "proxy") to tuple``

    due to a Python optimization that causes the concatenation to occur before
    US_STATES has been lazily generated.  To work around these issues, you
    can use a slice index (``[:]``) to force the generation of US_STATES
    before any other operations are processed by the Python interpreter::

      ('XX', _('Select a State')) + US_STATES[:]

.. data:: localflavor.us.us_states.STATE_CHOICES
    :annotation: = CONTIGUOUS_STATES + NON_CONTIGUOUS_STATES + US_TERRITORIES + ARMED_FORCES_STATES

    All US states and territories plus DC and military mail.

    This tuple is lazily generated and may not work as expected in all cases due
    to tuple optimizations in the Python interpreter which do not account for
    lazily generated tuples.  For example::

      STATE_CHOICES + ('XX', _('Select a State'))

    should work as expected, but::

      ('XX', _('Select a State')) + STATE_CHOICES

    may throw:

    ``TypeError: can only concatenate tuple (not "proxy") to tuple``

    due to a Python optimization that causes the concatenation to occur before
    STATE_CHOICES has been lazily generated.  To work around these issues, you
    can use a slice index (``[:]``) to force the generation of STATE_CHOICES
    before any other operations are processed by the Python interpreter::

      ('XX', _('Select a State')) + STATE_CHOICES[:]

.. data:: localflavor.us.us_states.USPS_CHOICES
    :annotation: = CONTIGUOUS_STATES + NON_CONTIGUOUS_STATES + US_TERRITORIES + ARMED_FORCES_STATES + COFA_STATES

    All US Postal Service locations.

    This tuple is lazily generated and may not work as expected in all cases due
    to tuple optimizations in the Python interpreter which do not account for
    lazily generated tuples.  For example::

      USPS_CHOICES + ('XX', _('Select a State'))

    should work as expected, but::

      ('XX', _('Select a State')) + USPS_CHOICES

    may throw:

      ``TypeError: can only concatenate tuple (not "proxy") to tuple``

    due to a Python optimization that causes the concatenation to occur before
    USPS_CHOICES has been lazily generated.  To work around these issues, you
    can use a slice index (``[:]``) to force the generation of USPS_CHOICES
    before any other operations are processed by the Python interpreter::

      ('XX', _('Select a State')) + USPS_CHOICES[:]

.. autodata:: localflavor.us.us_states.STATES_NORMALIZED
