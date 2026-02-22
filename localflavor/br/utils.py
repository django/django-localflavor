from .br_states import STATE_CHOICES

# Mapping UF -> full state name
STATE_CHOICES_DICT = dict(STATE_CHOICES)

def get_state_name_from_state_abbreviation(abbreviation=None):
    """
    Given a Brazilian state abbreviation (UF), return the full state name.

    Returns:
        str | None:
            - The full state name if the abbreviation exists
            - None if the abbreviation is invalid

    Example:
        get_state_name_from_state_abbreviation("RJ") -> "Rio de Janeiro"
        get_state_name_from_state_abbreviation("sp") -> "São Paulo"
        get_state_name_from_state_abbreviation("XX") -> None
        get_state_name_from_state_abbreviation() -> None
    """
    if not isinstance(abbreviation, str):
        return None

    return STATE_CHOICES_DICT.get(abbreviation.upper())
