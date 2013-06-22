from django.utils.encoding import force_unicode
from django.utils.functional import Promise

from sphinx.util.inspect import safe_repr

list_or_tuple = lambda x: isinstance(x, (tuple, list))


def lazy_repr(obj):
    if list_or_tuple(obj):
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
        items = lazy_repr(obj)
        repr_list = []

        if list_or_tuple(items):
            repr_list.append('(')
            items_length = len(items)
            for i, item in enumerate(items, 1):

                if list_or_tuple(item):
                    item_repr_list = ['(']
                    item_length = len(item)
                    for j, x in enumerate(item, 1):
                        if isinstance(x, int):
                            x_repr = '%s' % x
                        else:
                            x_repr = "'%s'" % x
                        if j == item_length:
                            item_repr_list.append("%s" % x_repr)
                        else:
                            item_repr_list.append("%s, " % x_repr)

                    if i == items_length:
                        item_repr_list.append(')')
                    else:
                        item_repr_list.append('), ')

                else:
                    if isinstance(item, int):
                        item_repr = '%s' % item
                    else:
                        item_repr = "'%s'" % item
                    item_repr_list = ["'%s'" % item_repr]

                repr_list.append(''.join(item_repr_list))

            repr_list.append(')')

            return ''.join(repr_list)

        return safe_repr(obj)

    autodoc.safe_repr = lazy_safe_repr  # noqa
