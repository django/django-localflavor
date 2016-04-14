__version__ = '1.2'


class DeprecatedPhoneNumber(object):
    def __init__(self, *args, **kwargs):
        import warnings
        warnings.warn(
            "%s is deprecated and will be removed in version 1.5."
            " Please migrate to django-phonenumber-field" % self.__class__.__name__,
            DeprecationWarning
        )

        super(self.__class__, self).__init__(*args, **kwargs)
