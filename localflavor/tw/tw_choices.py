from django.utils.translation import gettext_lazy as _

#: An alphabetical list of cities and counties for use as `choices` in a formfield.
#: Based on the administrative divisions of Taiwan.
#: https://en.wikipedia.org/wiki/List_of_administrative_divisions_of_Taiwan
TW_ADMINISTRATIVE_DIVISION_CHOICES = (
    ("changhua_county", _("Changhua County")),  # 彰化縣
    ("chiayi_city", _("Chiayi City")),  # 嘉義市
    ("chiayi_county", _("Chiayi County")),  # 嘉義縣
    ("hsinchu_city", _("Hsinchu City")),  # 新竹市
    ("hsinchu_county", _("Hsinchu County")),  # 新竹縣
    ("hualien_county", _("Hualien County")),  # 花蓮縣
    ("kaohsiung_city", _("Kaohsiung City")),  # 高雄市
    ("keelung_city", _("Keelung City")),  # 基隆市
    ("kinmen_county", _("Kinmen County")),  # 金門縣
    ("lienchiang_county", _("Lienchiang County")),  # 連江縣
    ("miaoli_county", _("Miaoli County")),  # 苗栗縣
    ("nantou_county", _("Nantou County")),  # 南投縣
    ("new_taipei_city", _("New Taipei City")),  # 新北市
    ("penghu_county", _("Penghu County")),  # 澎湖縣
    ("pingtung_county", _("Pingtung County")),  # 屏東縣
    ("taichung_city", _("Taichung City")),  # 台中市
    ("tainan_city", _("Tainan City")),  # 台南市
    ("taipei_city", _("Taipei City")),  # 台北市
    ("taitung_county", _("Taitung County")),  # 台東縣
    ("taoyuan_city", _("Taoyuan City")),  # 桃園市
    ("yilan_county", _("Yilan County")),  # 宜蘭縣
    ("yunlin_county", _("Yunlin County")),  # 雲林縣
)
