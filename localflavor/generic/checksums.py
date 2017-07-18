"""Common checksum routines."""
from django.utils import six

__all__ = ['luhn', 'ean']

LUHN_ODD_LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)  # sum_of_digits(index * 2)
EAN_LOOKUP = (3, 1)


def luhn(candidate):
    """
    Checks a candidate number for validity according to the Luhn algorithm.

    Luhn algorithm is used in validation of, for example, credit cards.
    Both numeric and string candidates are accepted.
    """
    if not isinstance(candidate, six.string_types):
        candidate = str(candidate)
    try:
        evens = sum(int(c) for c in candidate[-1::-2])
        odds = sum(LUHN_ODD_LOOKUP[int(c)] for c in candidate[-2::-2])
        return ((evens + odds) % 10 == 0)
    except ValueError:  # Raised if an int conversion fails
        return False


def ean(candidate):
    """
    Checks a candidate number for validity according to the EAN checksum calculation.

    Note that this validator does not enforce any length checks (usually 13 or 8).

    http://en.wikipedia.org/wiki/International_Article_Number_(EAN)
    """
    if not isinstance(candidate, six.string_types):
        candidate = str(candidate)
    if len(candidate) <= 1:
        return False
    given_number, given_checksum = candidate[:-1], candidate[-1]
    try:
        calculated_checksum = sum(
            int(digit) * EAN_LOOKUP[i % 2] for i, digit in enumerate(reversed(given_number)))
        calculated_checksum = 10 - (calculated_checksum % 10)
        return str(calculated_checksum) == given_checksum
    except ValueError:  # Raised if an int conversion fails
        return False
