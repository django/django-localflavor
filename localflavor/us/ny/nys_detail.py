"""
File for mapping of New York State counties, and cities.
"""

# County codes for each county
NYS_COUNTIES = (
    ('001', 'Albany'),
    ('003', 'Allegany'),
    ('005', 'Bronx'),
    ('007', 'Broome'),
    ('009', 'Cattaraugus'),
    ('011', 'Cayuga'),
    ('013', 'Chautauqua'),
    ('015', 'Chemung'),
    ('017', 'Chenango'),
    ('019', 'Clinton'),
    ('021', 'Columbia'),
    ('023', 'Cortland'),
    ('025', 'Delaware'),
    ('027', 'Dutchess'),
    ('029', 'Erie'),
    ('031', 'Essex'),
    ('033', 'Franklin'),
    ('035', 'Fulton'),
    ('037', 'Genesee'),
    ('039', 'Greene'),
    ('041', 'Hamilton'),
    ('043', 'Herkimer'),
    ('045', 'Jefferson'),
    ('047', 'Kings'),
    ('049', 'Lewis'),
    ('051', 'Livingston'),
    ('053', 'Madison'),
    ('055', 'Monroe'),
    ('057', 'Montgomery'),
    ('059', 'Nassau'),
    ('061', 'New York'),
    ('063', 'Niagara'),
    ('065', 'Oneida'),
    ('067', 'Onondaga'),
    ('069', 'Ontario'),
    ('071', 'Orange'),
    ('073', 'Orleans'),
    ('075', 'Oswego'),
    ('077', 'Otsego'),
    ('079', 'Putnam'),
    ('081', 'Queens'),
    ('083', 'Rensselaer'),
    ('085', 'Richmond'),
    ('087', 'Rockland'),
    ('091', 'Saratoga'),
    ('093', 'Schenectady'),
    ('095', 'Schoharie'),
    ('097', 'Schuyler'),
    ('099', 'Seneca'),
    ('089', 'St. Lawrence'),
    ('101', 'Steuben'),
    ('103', 'Suffolk'),
    ('105', 'Sullivan'),
    ('107', 'Tioga'),
    ('109', 'Tompkins'),
    ('111', 'Ulster'),
    ('113', 'Warren'),
    ('115', 'Washington'),
    ('117', 'Wayne'),
    ('119', 'Westchester'),
    ('121', 'Wyoming'),
    ('123', 'Yates'),
)

#: All NY State Counties
NYS_COUNTY_CHOICES = tuple(sorted(NYS_COUNTIES, key=lambda obj: obj[1]))
