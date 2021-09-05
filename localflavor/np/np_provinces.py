"""
List of Provinces in Nepal.

Source: https://en.wikipedia.org/wiki/Provinces_of_Nepal

Nepali province list choices are in format:

    ('Name of province',_('Name of province')),

eg.
    (('Bagmati'), _('Bagmati')),
"""

from django.utils.translation import gettext_lazy as _

PROVINCES = [
    (('bagmati'), _('Bagmati')),
    (('gandaki'), _('Gandaki')),
    (('karnali'), _('Karnali')),
    (('lumbini'), _('Lumbini')),
    (('province1'), _('Province 1')),
    (('province2'), _('Province 2')),
    (('sudurpaschim'), _('Sudurpaschim')),
]