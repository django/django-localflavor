"""Colombian-specific form helpers."""

from django.forms.fields import Select

from .co_departments import DEPARTMENT_CHOICES


class CODepartmentSelect(Select):
    """A Select widget that uses a list of Colombian states as its choices."""

    def __init__(self, attrs=None):
        super(CODepartmentSelect, self).__init__(attrs, choices=DEPARTMENT_CHOICES)
