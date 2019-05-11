from django.utils.translation import gettext_lazy as _

# List of governorates as defined by ISO_3166-2
# For reference; see https://en.wikipedia.org/wiki/ISO_3166-2:EG
# Note that these are governorates and not subdivisions

GOVERNORATE_CHOICES = (
    ('DK', _('Ad Daqahliyah')),
    ('BA', _('Al Bahr al Ahmar')),
    ('BH', _('Al Buhayrah')),
    ('FYM', _('Al Fayyum')),
    ('GH', _('Al Gharbiyah')),
    ('ALX', _('Al Iskandariyah')),
    ('IS', _("Al Isma'iliyah")),
    ('GZ', _('Al Jizah')),
    ('MNF', _('Al Minufiyah')),
    ('MN', _('Al Minya')),
    ('C', _('Al Qahirah')),
    ('KB', _('Al Qalyubiyah')),
    ('LX', _('Al Uqsur')),
    ('WAD', _('Al Wadi al Jadid')),
    ('SUZ', _('As Suways')),
    ('SHR', _('Ash Sharqiyah')),
    ('ASN', _('Aswan')),
    ('AST', _('Asyut')),
    ('BNS', _('Bani Suwayf')),
    ('PTS', _("Bur Sa'id")),
    ('DT', _('Dumyat')),
    ('JS', _("Janub Sina'")),
    ('KFS', _('Kafr ash Shaykh')),
    ('MT', _('Matruh')),
    ('KN', _('Qina')),
    ('SIN', _("Shamal Sina'")),
    ('SHG', _('Suhaj')),
)
