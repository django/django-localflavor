# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

#: An alphabetical list of Swedish counties, sorted by codes.
#: http://en.wikipedia.org/wiki/Counties_of_Sweden
COUNTY_CHOICES = (
    ('AB', _('Stockholm')),
    ('AC', _('Västerbotten')),
    ('BD', _('Norrbotten')),
    ('C', _('Uppsala')),
    ('D', _('Södermanland')),
    ('E', _('Östergötland')),
    ('F', _('Jönköping')),
    ('G', _('Kronoberg')),
    ('H', _('Kalmar')),
    ('I', _('Gotland')),
    ('K', _('Blekinge')),
    ('M', _('Skåne')),
    ('N', _('Halland')),
    ('O', _('Västra Götaland')),
    ('S', _('Värmland')),
    ('T', _('Örebro')),
    ('U', _('Västmanland')),
    ('W', _('Dalarna')),
    ('X', _('Gävleborg')),
    ('Y', _('Västernorrland')),
    ('Z', _('Jämtland')),
)

#: A dictionary of numerical county codes, with alphabetical codes
#: as keys and the more modern numerical codes as values.
#:
#: Values taken from https://sv.wikipedia.org/wiki/Sveriges_län,
#: and code system described at https://sv.wikipedia.org/wiki/Länskod
#: and http://www.scb.se/sv_/Hitta-statistik/Regional-statistik-och-kartor/Regionala-indelningar/Lan-och-kommuner/Lan-och-kommuner-i-kodnummerordning/

NUMERICAL_COUNTY_CODE_CHOICES = {
    ('AB', '01',),
    ('AC', '24',),
    ('BD', '25',),
    ('C', '03',),
    ('D', '04',),
    ('E', '05',),
    ('F', '06',),
    ('G', '07',),
    ('H', '08',),
    ('I', '09',),
    ('K', '10',),
    ('M', '12',),
    ('N', '13',),
    ('O', '14',),
    ('S', '17',),
    ('T', '18',),
    ('U', '19',),
    ('W', '20',),
    ('X', '21',),
    ('Y', '22',),
    ('Z', '23',),
}

#: A dictionary of full county names, as these are not as
#: somewhat in Swedish, e.g. "Skåne län" as opposed to
#: the more generic "Stockholms län" (ending with genitive case s)

FULL_COUNTY_NAME_CHOICES = {
    ('AB', _('Stockholm County'),),
    ('AC', _('Västerbotten County'),),
    ('BD', _('Norrbotten County'),),
    ('C', _('Uppsala County'),),
    ('D', _('Södermanland County'),),
    ('E', _('Östergötland County'),),
    ('F', _('Jönköping County'),),
    ('G', _('Kronoberg County'),),
    ('H', _('Kalmar County'),),
    ('I', _('Gotland County'),),
    ('K', _('Blekinge County'),),
    ('M', _('Skåne County'),),
    ('N', _('Halland County'),),
    ('O', _('Västra Götaland County'),),
    ('S', _('Värmland County'),),
    ('T', _('Örebro County'),),
    ('U', _('Västmanland County'),),
    ('W', _('Dalarna County'),),
    ('X', _('Gävleborg County'),),
    ('Y', _('Västernorrland County'),),
    ('Z', _('Jämtland County'),),
}
