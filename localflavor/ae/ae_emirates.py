"""UAE emirates."""

from django.utils.translation import gettext_lazy as _

#: A list of UAE emirates as `(abbreviation, name)` tuples.
EMIRATE_CHOICES = (
    ('AZ', _('Abu Dhabi')),
    ('AJ', _('Ajman')),
    ('DU', _('Dubai')),
    ('FU', _('Fujairah')),
    ('RA', _('Ras Al Khaimah')),
    ('SH', _('Sharjah')),
    ('UQ', _('Umm Al Quwain')),
)

#: Dictionary that maps emirate names and abbreviations to the
#: canonical abbreviation.
EMIRATES_NORMALIZED = {}

# Abbreviations
for abbr, name in EMIRATE_CHOICES:
    EMIRATES_NORMALIZED[abbr.lower()] = abbr
    EMIRATES_NORMALIZED[abbr.upper()] = abbr

# Names
EMIRATES_NORMALIZED.update({
    'abu dhabi': 'AZ',
    'ajman': 'AJ',
    'dubai': 'DU',
    'fujairah': 'FU',
    'ras al khaimah': 'RA',
    'ras al-khaimah': 'RA',
    'sharjah': 'SH',
    'umm al quwain': 'UQ',
    'umm al-quwain': 'UQ',
    # Arabic names
    'أبو ظبي': 'AZ',
    'عجمان': 'AJ',
    'دبي': 'DU',
    'الفجيرة': 'FU',
    'رأس الخيمة': 'RA',
    'الشارقة': 'SH',
    'أم القيوين': 'UQ',
})
