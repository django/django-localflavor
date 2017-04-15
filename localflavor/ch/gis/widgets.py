from django.contrib.gis.forms import BaseGeometryWidget


class GeoAdminWidget(BaseGeometryWidget):
    """
    A GIS widget allowing edition of geometries through a slippy map provided
    by geo.admin.ch.
    Map access from host != localhost needs a registration process.
    """
    template_name = 'gis/openlayers-geoadmin.html'
    map_srid = 21781

    class Media:
        js = (
            'http://api.geo.admin.ch/loader.js?mode=full',
            'gis/js/OLMapWidget.js',
        )
