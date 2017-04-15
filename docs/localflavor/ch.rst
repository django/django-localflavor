Switzerland (``ch``)
====================

Forms
-----

.. automodule:: localflavor.ch.forms
    :members:

GIS widget
----------

Needs Django >= 1.6.

.. automodule:: localflavor.ch.gis.widgets
    :members:

Map usage from geo.admin.ch is free as long as you locally run your app (on
localhost). As soon as your map is accessed through a fully qualified domain
name (e.g. on a production server), you need to registrate your domain name
with `geo.admin.ch authorities`__ unless tiles will be blocked.
You will then obtain a free annual quota of 25'000 Megapixels of tile bandwidth
for your site (See also `Conditions of use`__).

__ http://www.geo.admin.ch/internet/geoportal/de/home/services/geoservices/display_services/api_services/order_form.html
__ http://www.toposhop.admin.ch/en/shop/terms/use/geoservice_free

Data
----

.. autodata:: localflavor.ch.ch_states.STATE_CHOICES
