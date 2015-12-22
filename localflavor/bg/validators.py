from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .utils import get_egn_birth_date


def egn_validator(egn):
    """
    Check Bulgarian unique citizenship number (EGN) for validity
    More details https://en.wikipedia.org/wiki/Unique_citizenship_number
    Full information in Bulgarian about algorithm is available here
    http://www.grao.bg/esgraon.html#section2
    """
    def check_checksum(egn):
        weights = (2, 4, 8, 5, 10, 9, 7, 3, 6)
        try:
            checksum = sum(weight * int(digit) for weight, digit in zip(weights, egn))
            return int(egn[-1]) == checksum % 11 % 10
        except ValueError:
            return False

    def check_valid_date(egn):
        try:
            return get_egn_birth_date(egn)
        except ValueError:
            return None

    if not (len(egn) == 10 and check_checksum(egn) and check_valid_date(egn)):
        raise ValidationError(_("The EGN is not valid"))


def eik_validator(eik):
    """
    Check Bulgarian EIK/BULSTAT codes for validity
    full information in Bulgarian about algorithm is available here
    http://bulstat.registryagency.bg/About.html
    """
    error_message = _('EIK/BULSTAT is not valid')

    def get_checksum(weights, digits):
        checksum = sum(weight * digit for weight, digit in zip(weights, digits))
        return checksum % 11

    def check_eik_base(eik):
        checksum = get_checksum(range(1, 9), eik)
        if checksum == 10:
            checksum = get_checksum(range(3, 11), eik)
        return eik[8] == checksum % 10

    def check_eik_extra(eik):
        digits = eik[8:12]
        checksum = get_checksum((2, 7, 3, 5), digits)
        if checksum == 10:
            checksum = get_checksum((4, 9, 5, 7), digits)
        return eik[-1] == checksum % 10

    try:
        eik = list(map(int, eik))
    except ValueError:
        raise ValidationError(error_message)

    if not (len(eik) in [9, 13] and check_eik_base(eik)):
        raise ValidationError(error_message)

    if len(eik) == 13 and not check_eik_extra(eik):
        raise ValidationError(error_message)
