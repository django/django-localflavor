"""Common checksum routines."""
import warnings

from django.utils import six
from stdnum import luhn as stdnum_luhn

from localflavor.deprecation import RemovedInLocalflavor30Warning

__all__ = ['luhn', 'ean']

EAN_LOOKUP = (3, 1)


def luhn(candidate):
    """
    Checks a candidate number for validity according to the Luhn algorithm.

    Luhn algorithm is used in validation of, for example, credit cards.
    Both numeric and string candidates are accepted.

    .. deprecated:: 2.2
        Use the luhn function in the python-stdnum_ library instead.

    .. _python-stdnum: https://arthurdejong.org/python-stdnum/
    """
    warnings.warn(
        'luhn is deprecated in favor of the luhn function in the python-stdnum library.',
        RemovedInLocalflavor30Warning,
    )

    if not isinstance(candidate, six.string_types):
        candidate = str(candidate)

    # Our version returned True for empty strings.
    if candidate == '':
        return True

    return stdnum_luhn.is_valid(candidate)


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
        calculated_checksum = 9 - ((calculated_checksum - 1) % 10)
        return str(calculated_checksum) == given_checksum
    except ValueError:  # Raised if an int conversion fails
        return False
