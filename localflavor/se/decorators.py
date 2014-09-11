from .se_counties import numerical_county_code, full_county_name


def county_decorator(field_names=()):
    """Decorator that adds get_FIELDNAME_numerical_code() and get_FIELDNAME_full_name() methods
    to django models for all FIELDNAME values supplied in the field_names tuple. Ideally
    this can be used on all model fields that uses COUNTY_CHOICES for the choices argument.

    @county_decorator(field_names('field',))
    class MyClass:
        field = models.CharField(choices=se_counties=COUNTY_CHOICES)
    """

    def decorate(cls):
        for field_name in field_names:

            _get_numerical_code = lambda self: numerical_county_code(getattr(self, field_name))
            _get_full_name = lambda self: full_county_name(getattr(self, field_name))

            setattr(cls, "get_" + field_name + "_numerical_code", _get_numerical_code)
            setattr(cls, "get_" + field_name + "_full_name", _get_full_name)

        return cls
    return decorate
