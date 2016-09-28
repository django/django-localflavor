# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

"""
A list of Venezuelan regions for use as `choices` in a formfield.

Data based from http://en.wikipedia.org/wiki/Regions_of_Venezuela
"""

#: A list of Venezuelan regions for use as `choices` in a formfield.
REGION_CHOICES = (
    ('501', _(u'Región Capital')),
    ('502', _(u'Región Central')),
    ('503', _(u'Región de los Llanos')),
    ('504', _(u'Región Centro Occidental')),
    ('505', _(u'Región Zuliana')),
    ('506', _(u'Región de los Andes')),
    ('507', _(u'Región Nor-Oriental')),
    ('508', _(u'Región Insular')),
    ('509', _(u'Región Guayana')),
    ('509', _(u'Región Sur Occidental')),
)
