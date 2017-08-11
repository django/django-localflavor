
class EmptyValueCompatMixin(object):
    """
    forms.CharField in Django >= 1.11 has an 'empty_value' keyword argument for representing a value for "empty".

    https://docs.djangoproject.com/en/1.11/ref/forms/fields/#django.forms.CharField.empty_value

    This mixin adds self.empty_value set to an empty string for Django <= 1.10. This allows localflavor form fields to
    use self.empty_value consistently across Django versions.

    This mixin does not add an 'empty_value' keyword argument to versions of Django that don't already support it.

    This mixin can be removed when localflavor removes support for Django <= 1.10.
    """
    def __init__(self, *args, **kwargs):
        super(EmptyValueCompatMixin, self).__init__(*args, **kwargs)
        if not hasattr(self, 'empty_value'):
            self.empty_value = ''
