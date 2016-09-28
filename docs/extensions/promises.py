try:
    from django.utils.encoding import force_unicode
except ImportError:
    # We are on Python 3, force_text is force_unicode.
    from django.utils.encoding import force_text as force_unicode

from django.utils.functional import Promise

from sphinx.util.inspect import object_description

list_or_tuple = lambda x: isinstance(x, (tuple, list))


def lazy_repr(obj):
    if list_or_tuple(obj):
        values = []
        for item in obj:
            values.append(lazy_repr(item))
        if isinstance(obj, tuple):
            values = tuple(values)
        return values
    elif isinstance(obj, dict):
        values = {}
        for key, value in obj.items():
            values[lazy_repr(key)] = lazy_repr(value)
        return values
    else:
        if isinstance(obj, Promise):
            obj = force_unicode(obj)
        return obj


def setup(app):
    from sphinx.ext import autodoc

    def lazy_object_description(object):
        return object_description(lazy_repr(object))

    autodoc.object_description = lazy_object_description  # noqa
