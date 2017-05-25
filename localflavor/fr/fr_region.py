# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#: See the "Code officiel géographique" on the INSEE website <www.insee.fr>.
REGION_CHOICES = (
    # Overseas regions
    ('01', 'Guadeloupe'),
    ('02', 'Martinique'),
    ('03', 'Guyane'),
    ('04', 'La Réunion'),
    ('06', 'Mayotte'),
    # Metropolitan regions
    ('11', 'Île-de-France'),
    ('24', 'Centre-Val de Loire'),
    ('27', 'Bourgogne-Franche-Comté'),
    ('28', 'Normandie'),
    ('32', 'Nord-Pas-de-Calais-Picardie'),
    ('44', 'Alsace-Champagne-Ardenne-Lorraine'),
    ('52', 'Pays de la Loire'),
    ('53', 'Bretagne'),
    ('75', 'Aquitaine-Limousin-Poitou-Charentes'),
    ('76', 'Languedoc-Roussillon-Midi-Pyrénées'),
    ('84', 'Auvergne-Rhône-Alpes'),
    ('93', 'Provence-Alpes-Côte d\'Azur'),
    ('94', 'Corse')
)

#: France changed its regions in 2016, see:
# http://www.interieur.gouv.fr/Actualites/L-actu-du-Ministere/Les-noms-des-nouvelles-regions-sont-actes
REGION_2016_CHOICES = (
    # Overseas regions
    ('01', "Guadeloupe"),
    ('02', "Martinique"),
    ('03', "Guyane"),
    ('04', "La Réunion"),
    ('06', "Mayotte"),
    # Metropolitan regions
    ('11', "Île-de-France"),
    ('24', "Centre-Val de Loire"),
    ('27', "Bourgogne-Franche-Comté"),
    ('28', "Normandie"),
    ('32', "Hauts-de-France"),
    ('44', "Grand Est"),
    ('52', "Pays de la Loire"),
    ('53', "Bretagne"),
    ('75', "Nouvelle-Aquitaine"),
    ('76', "Occitanie"),
    ('84', "Auvergne-Rhône-Alpes"),
    ('93', "Provence-Alpes-Côte d'Azur"),
    ('94', "Corse"),
)
