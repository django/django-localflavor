from django.utils.translation import ugettext_lazy as _

#: English regions http://en.wikipedia.org/wiki/List_of_ceremonial_counties_of_England
ENGLAND_REGION_CHOICES = (
    ("Bedfordshire", _("Bedfordshire")),
    ("Berkshire", _("Berkshire")),
    ("Bristol", _("Bristol")),
    ("Buckinghamshire", _("Buckinghamshire")),
    ("Cambridgeshire", _("Cambridgeshire")),
    ("Cheshire", _("Cheshire")),
    ("City of London", _("City of London")),
    ("Cornwall", _("Cornwall")),
    ("County Durham", _("County Durham")),
    ("Cumbria", _("Cumbria")),
    ("Derbyshire", _("Derbyshire")),
    ("Devon", _("Devon")),
    ("Dorset", _("Dorset")),
    ("East Riding of Yorkshire", _("East Riding of Yorkshire")),
    ("East Sussex", _("East Sussex")),
    ("Essex", _("Essex")),
    ("Gloucestershire", _("Gloucestershire")),
    ("Greater London", _("Greater London")),
    ("Greater Manchester", _("Greater Manchester")),
    ("Hampshire", _("Hampshire")),
    ("Herefordshire", _("Herefordshire")),
    ("Hertfordshire", _("Hertfordshire")),
    ("Isle of Wight", _("Isle of Wight")),
    ("Kent", _("Kent")),
    ("Lancashire", _("Lancashire")),
    ("Leicestershire", _("Leicestershire")),
    ("Lincolnshire", _("Lincolnshire")),
    ("Merseyside", _("Merseyside")),
    ("Norfolk", _("Norfolk")),
    ("North Yorkshire", _("North Yorkshire")),
    ("Northamptonshire", _("Northamptonshire")),
    ("Northumberland", _("Northumberland")),
    ("Nottinghamshire", _("Nottinghamshire")),
    ("Oxfordshire", _("Oxfordshire")),
    ("Rutland", _("Rutland")),
    ("Shropshire", _("Shropshire")),
    ("Somerset", _("Somerset")),
    ("South Yorkshire", _("South Yorkshire")),
    ("Staffordshire", _("Staffordshire")),
    ("Suffolk", _("Suffolk")),
    ("Surrey", _("Surrey")),
    ("Tyne and Wear", _("Tyne and Wear")),
    ("Warwickshire", _("Warwickshire")),
    ("West Midlands", _("West Midlands")),
    ("West Sussex", _("West Sussex")),
    ("West Yorkshire", _("West Yorkshire")),
    ("Wiltshire", _("Wiltshire")),
    ("Worcestershire", _("Worcestershire"))
)

#: Northern Ireland regions: http://en.wikipedia.org/wiki/List_of_Irish_counties_by_area
NORTHERN_IRELAND_REGION_CHOICES = (
    ("County Antrim", _("County Antrim")),
    ("County Armagh", _("County Armagh")),
    ("County Down", _("County Down")),
    ("County Fermanagh", _("County Fermanagh")),
    ("County Londonderry", _("County Londonderry")),
    ("County Tyrone", _("County Tyrone")),
)

#: Welsh regions: http://en.wikipedia.org/wiki/Preserved_counties_of_Wales
WALES_REGION_CHOICES = (
    ("Clwyd", _("Clwyd")),
    ("Dyfed", _("Dyfed")),
    ("Gwent", _("Gwent")),
    ("Gwynedd", _("Gwynedd")),
    ("Mid Glamorgan", _("Mid Glamorgan")),
    ("Powys", _("Powys")),
    ("South Glamorgan", _("South Glamorgan")),
    ("West Glamorgan", _("West Glamorgan")),
)

#: Scottish regions: http://en.wikipedia.org/wiki/Regions_and_districts_of_Scotland
SCOTTISH_REGION_CHOICES = (
    ("Borders", _("Borders")),
    ("Central Scotland", _("Central Scotland")),
    ("Dumfries and Galloway", _("Dumfries and Galloway")),
    ("Fife", _("Fife")),
    ("Grampian", _("Grampian")),
    ("Highland", _("Highland")),
    ("Lothian", _("Lothian")),
    ("Orkney Islands", _("Orkney Islands")),
    ("Shetland Islands", _("Shetland Islands")),
    ("Strathclyde", _("Strathclyde")),
    ("Tayside", _("Tayside")),
    ("Western Isles", _("Western Isles")),
)

#: Great Britain nations
GB_NATIONS_CHOICES = (
    ("England", _("England")),
    ("Northern Ireland", _("Northern Ireland")),
    ("Scotland", _("Scotland")),
    ("Wales", _("Wales")),
)

#: All regions of Great Britain
GB_REGION_CHOICES = (ENGLAND_REGION_CHOICES +
                     NORTHERN_IRELAND_REGION_CHOICES +
                     WALES_REGION_CHOICES +
                     SCOTTISH_REGION_CHOICES)
