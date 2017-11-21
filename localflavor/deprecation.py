import warnings


class RemovedInLocalflavor20Warning(DeprecationWarning):
    pass


class DeprecatedPhoneNumberFormFieldMixin(object):
    def __init__(self):
        super(DeprecatedPhoneNumberFormFieldMixin, self).__init__()
        warnings.warn(
            "{} is deprecated in favor of the django-phonenumber-field library.".format(
                self.__class__.__name__
            ),
            RemovedInLocalflavor20Warning,
        )


class DeprecatedPhoneNumberField(object):
    def __init__(self):
        self.system_check_deprecated_details = {
            'msg': self.__class__.__name__ + " is deprecated.",
            'hint': 'Use django-phonenumber-field library instead.'
        }
