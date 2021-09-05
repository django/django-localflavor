"""
List of Zones in Nepal.

Source: https://en.wikipedia.org/wiki/List_of_zones_of_Nepal

Nepali zones list choices are in format:

    ('Name of zone',_('Name of zone')),

eg.
    ('Bagmati', _('Bagmati')),

"""

from django.utils.translation import gettext_lazy as _

# list of zones in nepal
ZONES = [
    (('bagmati'), _('Bagmati')),
    (('bheri'), _('Bheri')),
    (('dhawalagiri'), _('Dhawalagiri')),
    (('dandaki'), _('Gandaki')),
    (('janakpur'), _('Janakpur')),
    (('karnali'), _('Karnali')),
    (('koshi'), _('Koshi')),
    (('lumbini'), _('Lumbini')),
    (('mahakali'), _('Mahakali')),
    (('mechi'), _('Mechi')),
    (('narayani'), _('Narayani')),
    (('rapti'), _('Rapti')),
    (('sagarmatha'), _('Sagarmatha')),
    (('seti'), _('Seti')),
]
