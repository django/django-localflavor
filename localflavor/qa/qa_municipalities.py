import unicodedata
from django.utils.translation import gettext_lazy as _

# A list of Qatar municipalities (baladiyat) as (abbreviation, name) tuples.
# As per https://www.data.gov.qa/explore/dataset/municipalities-in-qatar-2025/
# Abbreviations are ISO 3166-2:QA subdivision codes.
MUNICIPALITY_CHOICES = (
    ("DA", _("Doha")),
    ("KH", _("Al Khor and Al Dakhira")),
    ("RA", _("Al Rayyan")),
    ("MS", _("Al Shamal")),
    ("SH", _("Al Sheehaniya")),
    ("WA", _("Al Wakrah")),
    ("ZA", _("Al Daayen")),
    ("US", _("Umm Slal")),
)

# Canonical aliases for municipalities
MUNICIPALITY_ALIASES: dict[str, list[str]] = {
    "DA": ["doha", "al doha", "ad dawhah", "الدوحة"],
    "KH": ["al khor and al dakhira", "al khor", "khor", "الخور والذخيرة"],
    "RA": ["al rayyan", "rayyan", "al rayan", "rayan", "الريان"],
    "MS": ["al shamal", "shamal", "north", "الشمال"],
    "SH": ["al shahaniya", "shahaniya", "الشحانية"],
    "WA": ["al wakrah", "wakrah", "الوكرة"],
    "ZA": ["al daayen", "daayen", "الضعاين"],
    "US": ["umm salal", "أم صلال", "ام صلال"],
}


def _normalize(value):
    """Lowercase, strip surrounding whitespace, collapse internal runs,
    and remove Unicode combining characters (e.g. diacritics)."""
    value = " ".join(value.strip().lower().split())
    return unicodedata.normalize("NFKD", value)


def _build_lookup():
    """Build a mapping from every known name / alias / code to its ISO code."""
    lookup = {}

    for abbr, _label in MUNICIPALITY_CHOICES: 
        lookup[_normalize(abbr)] = abbr
        lookup[_normalize(_label)] = abbr

    for abbr, aliases in MUNICIPALITY_ALIASES.items():
        for alias in aliases:
            lookup[_normalize(alias)] = abbr

    return lookup


# Dictionary mapping municipality names / aliases to canonical ISO code.
# Built once at import time
QA_MUNICIPALITIES_NORMALIZED = _build_lookup()

def resolve_municipality(value):
    """Return the ISO 3166-2:QA code for *value*, or ``None`` if unrecognised.

    Accepts codes, English names, Arabic names, and registered aliases,
    all case- and whitespace-insensitive.
    """
    return QA_MUNICIPALITIES_NORMALIZED.get(_normalize(value))
