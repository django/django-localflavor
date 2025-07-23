from .br_states import STATE_CHOICES


def get_states_of_brazil(federative_unit=None, capital_letter=False):
    """
    Return a state of Brazil or available options

    Parametes:
    federative_unit (Any, optional): The Federative Unit. If not provided, defaults to None.
    capital_letter (bool, optional): A boolean flag to return the state with capital letter. Defaults to False

    returns:
    Union[str, dict]:
        - If federative_unit not is None and his value is valid, returns a string
        - If federative_unit is None, returns a dictionary
        - If capital_letter is True, returns all values with capital letters
    """

    state_choices_available = {
        acronym: state.upper() if capital_letter else state for acronym, state in STATE_CHOICES
    }

    if federative_unit is None:
        return state_choices_available

    federative_unit = federative_unit.upper() if isinstance(federative_unit, str) else ""

    if federative_unit in state_choices_available:
        return state_choices_available[federative_unit]

    return state_choices_available
