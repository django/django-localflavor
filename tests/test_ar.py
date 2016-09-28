from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.ar.forms import ARCBUField, ARCUITField, ARDNIField, ARPostalCodeField, ARProvinceSelect


class ARLocalFlavorTests(SimpleTestCase):
    def test_ARProvinceSelect(self):
        f = ARProvinceSelect()
        out = '''<select name="provincias">
<option value="B">Buenos Aires</option>
<option value="K">Catamarca</option>
<option value="H">Chaco</option>
<option value="U">Chubut</option>
<option value="C">Ciudad Aut\xf3noma de Buenos Aires</option>
<option value="X">C\xf3rdoba</option>
<option value="W">Corrientes</option>
<option value="E">Entre R\xedos</option>
<option value="P">Formosa</option>
<option value="Y">Jujuy</option>
<option value="L">La Pampa</option>
<option value="F">La Rioja</option>
<option value="M">Mendoza</option>
<option value="N">Misiones</option>
<option value="Q">Neuqu\xe9n</option>
<option value="R">R\xedo Negro</option>
<option value="A" selected="selected">Salta</option>
<option value="J">San Juan</option>
<option value="D">San Luis</option>
<option value="Z">Santa Cruz</option>
<option value="S">Santa Fe</option>
<option value="G">Santiago del Estero</option>
<option value="V">Tierra del Fuego, Ant\xe1rtida e Islas del Atl\xe1ntico Sur</option>
<option value="T">Tucum\xe1n</option>
</select>'''
        self.assertHTMLEqual(f.render('provincias', 'A'), out)

    def test_ARPostalCodeField(self):
        error_format = ['Enter a postal code in the format NNNN or ANNNNAAA.']
        error_atmost = ['Ensure this value has at most 8 characters (it has 9).']
        error_atleast = ['Ensure this value has at least 4 characters (it has 3).']
        valid = {
            '5000': '5000',
            'C1064AAB': 'C1064AAB',
            'c1064AAB': 'C1064AAB',
            'C1064aab': 'C1064AAB',
            '4400': '4400',
            'C1064AAB': 'C1064AAB',
        }
        invalid = {
            'C1064AABB': error_atmost + error_format,
            'C1064AA': error_format,
            'C1064AB': error_format,
            '106AAB': error_format,
            '500': error_atleast + error_format,
            '5PPP': error_format,
        }
        self.assertFieldOutput(ARPostalCodeField, valid, invalid)

    def test_ARDNIField(self):
        error_length = ['This field requires 7 or 8 digits.']
        error_digitsonly = ['This field requires only numbers.']
        valid = {
            '20123456': '20123456',
            '20.123.456': '20123456',
            '20123456': '20123456',
            '20.123.456': '20123456',
            '20.123456': '20123456',
            '9123456': '9123456',
            '9.123.456': '9123456',
        }
        invalid = {
            '101234566': error_length,
            'W0123456': error_digitsonly,
            '10,123,456': error_digitsonly,
        }
        self.assertFieldOutput(ARDNIField, valid, invalid)

    def test_ARCUITField(self):
        error_format = ['Enter a valid CUIT in XX-XXXXXXXX-X or XXXXXXXXXXXX format.']
        error_invalid = ['Invalid CUIT.']
        error_legal_type = ['Invalid legal type. Type must be 27, 20, 30, 23, 24 or 33.']
        valid = {
            '20-10123456-9': '20-10123456-9',
            '20-10123456-9': '20-10123456-9',
            '27-10345678-4': '27-10345678-4',
            '20101234569': '20-10123456-9',
            '27103456784': '27-10345678-4',
            '30011111110': '30-01111111-0',
            '24117166062': '24-11716606-2',
            '33500001599': '33-50000159-9',
            '23000052264': '23-00005226-4',
        }
        invalid = {
            '2-10123456-9': error_format,
            '210123456-9': error_format,
            '20-10123456': error_format,
            '20-10123456-': error_format,
            '20-10123456-5': error_invalid,
            '27-10345678-1': error_invalid,
            '27-10345678-1': error_invalid,
            '11211111110': error_legal_type,
        }
        self.assertFieldOutput(ARCUITField, valid, invalid)

    def test_ARCBUField(self):
        error_format = ['Enter a valid CBU in XXXXXXXXXXXXXXXXXXXXXX format.']
        error_length = ['CBU must be exactly 22 digits long.']
        error_checksum = ['Invalid CBU.']
        valid = {
            '2237628810898098715378': '2237628810898098715378',
            '5433758936130717465023': '5433758936130717465023',
            '5729195067928761667584': '5729195067928761667584',
            '9498175528566296510521': '9498175528566296510521',
            '7362966507842824472644': '7362966507842824472644',
            '8693513393883886497274': '8693513393883886497274',
            '1542952861593836535608': '1542952861593836535608',
            '5833008953419074707467': '5833008953419074707467',
            '9687027721961737239525': '9687027721961737239525',
            '8048819274216931992586': '8048819274216931992586'
        }

        invalid = {
            'abc123def456-9024-2313': error_format,
            '142512591859898123123': error_length,
            '12312452521512526125566': error_length,
            '1234567891234567891234': error_checksum,
            '1234562374545894589234': error_checksum,
            '0987653759257883891234': error_checksum,
        }
        self.assertFieldOutput(ARCBUField, valid, invalid)
