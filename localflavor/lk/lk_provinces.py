"""
List of Provinces of Sri Lanka.

Source: https://en.wikipedia.org/wiki/Provinces_of_Sri_Lanka

Sri Lanka province list choices are in this format:

    ('name_of_province',_('Name of province')),

eg.
    ('central', _('Central')),
"""

from django.utils.translation import gettext_lazy as _

PROVINCES = [
    ('central', _('Central')),
    ('north_central', _('North Central')),
    ('northern', _('Northern')),
    ('eastern', _('Eastern')),
    ('north_western', _('North Western')),
    ('southern', _('Southern')),
    ('uva', _('Uva')),
    ('sabaragamuwa', _('Sabaragamuwa')),
    ('western', _('Western')),
]