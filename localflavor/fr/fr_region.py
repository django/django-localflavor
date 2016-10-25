# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#: See the "Code officiel géographique" on the INSEE website <www.insee.fr>.
# http://www.insee.fr/fr/methodes/default.asp?page=nomenclatures/cog/codes_regions_2016.htm
REGION_CHOICES = (
    # Overseas regions
    ('01', 'Guadeloupe'),
    ('02', 'Martinique'),
    ('03', 'Guyane'),
    ('04', 'La Réunion'),
    ('06', 'Mayotte'),
    # Metropolitan regions
    ('11', 'Île-de-France'),
    ('21', 'Champagne-Ardenne'),
    ('22', 'Picardie'),
    ('23', 'Haute-Normandie'),
    ('24', 'Centre'),
    ('25', 'Basse-Normandie'),
    ('26', 'Bourgogne'),
    ('31', 'Nord-Pas-de-Calais'),
    ('41', 'Lorraine'),
    ('42', 'Alsace'),
    ('43', 'Franche-Comté'),
    ('52', 'Pays de la Loire'),
    ('53', 'Bretagne'),
    ('54', 'Poitou-Charentes'),
    ('72', 'Aquitaine'),
    ('73', 'Midi-Pyrénées'),
    ('74', 'Limousin'),
    ('82', 'Rhône-Alpes'),
    ('83', 'Auvergne'),
    ('91', 'Languedoc-Roussillon'),
    ('93', 'Provence-Alpes-Côte d\'Azur'),
    ('94', 'Corse')
)

NEW_REGION_CHOICES = (
    # Overseas regions
    ('01', 'Guadeloupe',                         ['01']),
    ('02', 'Martinique',                         ['02']),
    ('03', 'Guyane',                             ['03']),
    ('04', 'La Réunion',                         ['04']),
    ('06', 'Mayotte',                            ['06']),
    # Metropolitan regions
    ('11', 'Île-de-France',                      ['11']),
    ('24', 'Centre-Val de Loire',                ['24']),
    ('27', 'Picardie',                           ['26','43']),
    ('28', 'Normandie',                          ['23','25']),
    ('32', 'Nord-Pas-de-Calais-Picardie',        ['31','22']),
    ('44', 'Alsace-Champagne-Ardenne-Lorraine',  ['41','42','21']),
    ('52', 'Pays de la Loire',                   ['52']),
    ('53', 'Bretagne',                           ['53']),
    ('75', 'Aquitaine-Limousin-Poitou-Charentes',['72','54','74']),
    ('76', 'Languedoc-Roussillon-Midi-Pyrénées', ['73','91']),
    ('84', 'Auvergne-Rhône-Alpes',               ['82','83']),
    ('93', 'Provence-Alpes-Côte d\'Azur',        ['93']),
    ('94', 'Corse',                              ['94'])
)


def transform(old_region):
    res =  None
    it = iter(NEW_REGION_CHOICES)
    next_reg = True
    while res == None and next_reg :
        next_reg = it.next()
        if old_region[0] in next_reg[2]:
            res = next_reg[0]

    return (old_region[0], res)

OLD_TO_NEW_REGION_CODE = dict(map(transform, REGION_CHOICES))

