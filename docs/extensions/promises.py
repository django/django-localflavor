from django.utils.encoding import force_unicode
from django.utils.functional import Promise

from sphinx.util.inspect import safe_repr


def lazy_repr(obj):
    if isinstance(obj, (tuple, list)):
        values = []
        for item in obj:
            values.append(lazy_repr(item))
        if isinstance(obj, tuple):
            values = tuple(values)
        return values
    else:
        if isinstance(obj, Promise):
            obj = force_unicode(obj)
        return obj


def setup(app):
    from sphinx.ext import autodoc

    def lazy_safe_repr(obj):
        return safe_repr(lazy_repr(obj))

    autodoc.safe_repr = lazy_safe_repr  # noqa
