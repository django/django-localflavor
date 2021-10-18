"""
List of Provinces of Nepal.

Source: https://en.wikipedia.org/wiki/Provinces_of_Nepal

Nepali province list choices are in this format:

    ('name_of_province',_('Name of province')),

eg.
    ('bagmati', _('Bagmati')),
"""

from django.utils.translation import gettext_lazy as _

PROVINCES = [
    ('bagmati', _('Bagmati')),
    ('gandaki', _('Gandaki')),
    ('karnali', _('Karnali')),
    ('lumbini', _('Lumbini')),
    ('province1', _('Province 1')),
    ('province2', _('Province 2')),
    ('sudurpaschim', _('Sudurpaschim')),
]
