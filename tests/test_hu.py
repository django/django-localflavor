# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.hu.forms import HUCountySelect


class HULocalFlavorTests(SimpleTestCase):
    def test_HUCountySelect(self):
        f = HUCountySelect()
        out = '''<select name="counties">
    <option value="bacs_kiskun">Bács-Kiskun</option>
    <option value="baranya">Baranya</option>
    <option value="bekes">Békés</option>
    <option value="borsod_abauj_zemplen">Borsod-Abaúj-Zemplén</option>
    <option value="csongrad">Csongrád</option>
    <option value="fejer">Fejér</option>
    <option value="gyor_moson_sopron">Győr-Moson-Sopron</option>
    <option value="hajdu_bihar">Hajdú-Bihar</option>
    <option value="heves">Heves</option>
    <option value="jasz_nagykun_szolnok">Jász-Nagykun-Szolnok</option>
    <option value="komarom_esztergom">Komárom-Esztergom</option>
    <option value="nograd">Nógrád</option>
    <option value="pest">Pest</option>
    <option value="somogy">Somogy</option>
    <option value="szabolcs_szatmar_bereg">Szabolcs-Szatmár-Bereg</option>
    <option value="tolna">Tolna</option>
    <option value="vas" selected="selected">Vas</option>
    <option value="veszprem">Veszprém</option>
    <option value="zala">Zala</option>
</select>'''
        self.assertHTMLEqual(f.render('counties', 'vas'), out)
