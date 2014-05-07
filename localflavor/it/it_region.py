# -*- coding: utf-8 -*
from __future__ import unicode_literals

#: An alphabetical list of regions
REGION_CHOICES = (
    ('ABR', 'Abruzzo'),
    ('BAS', 'Basilicata'),
    ('CAL', 'Calabria'),
    ('CAM', 'Campania'),
    ('EMR', 'Emilia-Romagna'),
    ('FVG', 'Friuli-Venezia Giulia'),
    ('LAZ', 'Lazio'),
    ('LIG', 'Liguria'),
    ('LOM', 'Lombardia'),
    ('MAR', 'Marche'),
    ('MOL', 'Molise'),
    ('PMN', 'Piemonte'),
    ('PUG', 'Puglia'),
    ('SAR', 'Sardegna'),
    ('SIC', 'Sicilia'),
    ('TOS', 'Toscana'),
    ('TAA', 'Trentino-Alto Adige'),
    ('UMB', 'Umbria'),
    ('VAO', 'Valle d’Aosta'),
    ('VEN', 'Veneto'),
)

REGION_PROVINCE = {
    'ABR': ['AQ', 'CH', 'PE', 'TE'],
    'BAS': ['MT', 'PZ'],
    'CAL': ['CS', 'CZ', 'KR', 'RC', 'VV'],
    'CAM': ['AV', 'BN', 'CE', 'NA', 'SA'],
    'EMR': ['BO', 'FC', 'FE', 'MO', 'PC', 'PR', 'RA', 'RE', 'RN'],
    'FVG': ['GO', 'PN', 'TS', 'UD'],
    'LAZ': ['FR', 'LT', 'RI', 'RM', 'VT'],
    'LIG': ['GE', 'IM', 'SP', 'SV'],
    'LOM': ['BG', 'BS', 'CO', 'CR', 'LC', 'LO', 'MB', 'MI', 'MN', 'PV', 'SO', 'VA'],
    'MAR': ['AN', 'AP', 'FM', 'MC', 'PU'],
    'MOL': ['CB', 'IS'],
    'PMN': ['AL', 'AT', 'BI', 'CN', 'NO', 'TO', 'VB', 'VC'],
    'PUG': ['BA', 'BR', 'BT', 'FG', 'LE', 'TA'],
    'SAR': ['CA', 'CI', 'NU', 'OG', 'OR', 'OT', 'SS', 'VS'],
    'SIC': ['AG', 'CL', 'CT', 'EN', 'ME', 'PA', 'RG', 'SR', 'TP'],
    'TAA': ['BZ', 'TN'],
    'TOS': ['AR', 'FI', 'GR', 'LI', 'LU', 'MS', 'PI', 'PO', 'PT', 'SI'],
    'UMB': ['PG', 'TR'],
    'VAO': ['AO'],
    'VEN': ['BL', 'PD', 'RO', 'TV', 'VE', 'VI', 'VR'],
}
