"""Common checksum routines."""
import warnings

from django.utils import six
from stdnum import ean as stdnum_ean
from stdnum import luhn as stdnum_luhn

from localflavor.deprecation import RemovedInLocalflavor30Warning

__all__ = ['luhn', 'ean']


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

    .. deprecated:: 2.2
       Use the ean function in the python-stdnum_ library instead.

    .. _python-stdnum: https://arthurdejong.org/python-stdnum/
    """
    warnings.warn(
        'ean is deprecated in favor of the ean function in the python-stdnum library.',
        RemovedInLocalflavor30Warning,
    )

    if not isinstance(candidate, six.string_types):
        candidate = str(candidate)

    return stdnum_ean.is_valid(candidate)
