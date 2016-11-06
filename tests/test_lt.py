# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.lt.forms import LTCountySelect, LTIDCodeField, LTMunicipalitySelect, LTPhoneField, LTPostalCodeField


class LTLocalFlavorTests(SimpleTestCase):

    def test_LTIDCodeField(self):
        error_len = ['ID Code consists of exactly 11 decimal digits.']
        error_check = ['Wrong ID Code checksum.']
        error_date = ['ID Code contains invalid date.']

        valid = {
            '33309240064': '33309240064',
            '35002125431': '35002125431',
            '61205010081': '61205010081',
            '48504140959': '48504140959',
        }

        invalid = {
            '3456': error_len,
            '123456789101': error_len,
            '33309240065': error_check,
            'hello': error_len,
            '134535443i2': error_len,
            '48504140956': error_check,
            '48504140953': error_check,
            '50520150003': error_date,
            '50501009554': error_date,
            '80101017318': error_date,
        }

        self.assertFieldOutput(LTIDCodeField, valid, invalid)

    def test_LTPostalCodeField(self):
        errors = LTPostalCodeField().error_messages

        valid = {'00000': 'LT-00000',
                 'LT-00000': 'LT-00000',
                 'lt - 12345': 'LT-12345'}
        invalid = {'000000': [errors['invalid']],
                   '0000': [errors['invalid']],
                   'LT-00': [errors['invalid']],
                   'LT-0000': [errors['invalid']],
                   'LT-000000': [errors['invalid']]}
        self.assertFieldOutput(LTPostalCodeField, valid, invalid)

    def test_LTCountySelect(self):
        f = LTCountySelect()
        expected = """
            <select name="test">
            <option value="alytus">Alytus</option>
            <option value="kaunas">Kaunas</option>
            <option value="klaipeda">Klaipėda</option>
            <option value="mariampole">Mariampolė</option>
            <option value="panevezys">Panevėžys</option>
            <option value="siauliai">Šiauliai</option>
            <option value="taurage">Tauragė</option>
            <option value="telsiai">Telšiai</option>
            <option value="utena">Utena</option>
            <option value="vilnius">Vilnius</option>
            </select>
        """
        self.assertHTMLEqual(f.render('test', None), expected)

    def test_LTMunicipalitySelect(self):
        f = LTMunicipalitySelect()
        expected = """
            <select name="test">
            <option value="akmene">Akmenė district</option>
            <option value="alytus_c">Alytus city</option>
            <option value="alytus">Alytus district</option>
            <option value="anyksciai">Anykščiai district</option>
            <option value="birstonas">Birštonas</option>
            <option value="birzai">Biržai district</option>
            <option value="druskininkai">Druskininkai</option>
            <option value="elektrenai">Elektrėnai</option>
            <option value="ignalina">Ignalina district</option>
            <option value="jonava">Jonava district</option>
            <option value="joniskis">Joniškis district</option>
            <option value="jurbarkas">Jurbarkas district</option>
            <option value="kaisiadorys">Kaišiadorys district</option>
            <option value="kalvarija">Kalvarija</option>
            <option value="kaunas_c">Kaunas city</option>
            <option value="kaunas">Kaunas district</option>
            <option value="kazluruda">Kazlų Rūda</option>
            <option value="kedainiai">Kėdainiai district</option>
            <option value="kelme">Kelmė district</option>
            <option value="klaipeda_c">Klaipėda city</option>
            <option value="klaipeda">Klaipėda district</option>
            <option value="kretinga">Kretinga district</option>
            <option value="kupiskis">Kupiškis district</option>
            <option value="lazdijai">Lazdijai district</option>
            <option value="marijampole">Marijampolė</option>
            <option value="mazeikiai">Mažeikiai district</option>
            <option value="moletai">Molėtai district</option>
            <option value="neringa">Neringa</option>
            <option value="pagegiai">Pagėgiai</option>
            <option value="pakruojis">Pakruojis district</option>
            <option value="palanga">Palanga city</option>
            <option value="panevezys_c">Panevėžys city</option>
            <option value="panevezys">Panevėžys district</option>
            <option value="pasvalys">Pasvalys district</option>
            <option value="plunge">Plungė district</option>
            <option value="prienai">Prienai district</option>
            <option value="radviliskis">Radviliškis district</option>
            <option value="raseiniai">Raseiniai district</option>
            <option value="rietavas">Rietavas</option>
            <option value="rokiskis">Rokiškis district</option>
            <option value="skuodas">Skuodas district</option>
            <option value="sakiai">Šakiai district</option>
            <option value="salcininkai">Šalčininkai district</option>
            <option value="siauliai_c">Šiauliai city</option>
            <option value="siauliai">Šiauliai district</option>
            <option value="silale">Šilalė district</option>
            <option value="silute">Šilutė district</option>
            <option value="sirvintos">Širvintos district</option>
            <option value="svencionys">Švenčionys district</option>
            <option value="taurage">Tauragė district</option>
            <option value="telsiai">Telšiai district</option>
            <option value="trakai">Trakai district</option>
            <option value="ukmerge">Ukmergė district</option>
            <option value="utena">Utena district</option>
            <option value="varena">Varėna district</option>
            <option value="vilkaviskis">Vilkaviškis district</option>
            <option value="vilnius_c">Vilnius city</option>
            <option value="vilnius">Vilnius district</option>
            <option value="visaginas">Visaginas</option>
            <option value="zarasai">Zarasai district</option>
            </select>
        """
        self.assertHTMLEqual(f.render('test', None), expected)

    def test_LTPhoneField(self):
        errors = LTPhoneField().error_messages
        invalid = {'8 600 00 00o': [errors['non-digit']],
                   '8 600 00 000 o': [errors['non-digit']],
                   'o 600 00 000': [errors['non-digit']]}
        self.assertFieldOutput(LTPhoneField, {}, invalid)

    def test_LTPhoneField_emergency(self):
        errors = LTPhoneField().error_messages

        valid = {'112': '112', '01': '01', '02': '02', '03': '03', '04': '04'}
        invalid = {'1112': [errors['no-parse']]}
        self.assertFieldOutput(LTPhoneField, valid, invalid,
                               field_kwargs={'emergency': True,
                                             'mobile': False,
                                             'landline': False})

        self.assertFieldOutput(LTPhoneField, {}, {'112': [errors['no-parse']]},
                               field_kwargs={'emergency': False,
                                             'mobile': False,
                                             'landline': False})

    def test_LTPhoneField_mobile(self):
        errors = LTPhoneField().error_messages
        valid = {'8 600 00 000': '+37060000000',
                 '370 600 00 000': '+37060000000',
                 '+370 612 34 567': '+37061234567'}
        invalid = {'8 600 00 00': [errors['no-parse']],
                   '370 600 00 00': [errors['no-parse']],
                   '370 600 00 0': [errors['no-parse']],
                   '860 000 00 000': [errors['no-parse']]}

        self.assertFieldOutput(LTPhoneField, valid, invalid,
                               field_kwargs={'landline': False})

        self.assertFieldOutput(LTPhoneField, {},
                               {'8 600 00 000': [errors['no-parse']],
                                '370 600 00 000': [errors['no-parse']],
                                '+370 612 34 567': [errors['no-parse']]},
                               field_kwargs={'mobile': False,
                                             'landline': False})

    def test_LTPhoneField_service(self):
        errors = LTPhoneField().error_messages
        valid = {'8 800 00 000': '+37080000000',
                 '370 800 00 000': '+37080000000',
                 '+370 800 34 567': '+37080034567'}
        invalid = {'8 800 00 00': [errors['no-parse']],
                   '370 800 00 00': [errors['no-parse']],
                   '370 800 00 0': [errors['no-parse']],
                   '860 800 00 000': [errors['no-parse']],
                   '8 812 00 000': [errors['no-parse']],
                   '370 812 00 000': [errors['no-parse']]}

        self.assertFieldOutput(LTPhoneField, valid, invalid,
                               field_kwargs={'landline': False,
                                             'mobile': False,
                                             'service': True})

        self.assertFieldOutput(LTPhoneField, {},
                               {'8 800 00 000': [errors['no-parse']],
                                '370 800 00 000': [errors['no-parse']],
                                '+370 800 34 567': [errors['no-parse']]},
                               field_kwargs={'mobile': False,
                                             'landline': False,
                                             'service': False})

    def test_LTPhoneField_landline_local(self):
        errors = LTPhoneField().error_messages

        valid = {"2123456": "+37052123456",
                 "123456": "123456",
                 "12345": "12345"}
        invalid = {"1234": [errors['no-parse']]}

        self.assertFieldOutput(LTPhoneField, valid, invalid,
                               field_kwargs={'landline': True,
                                             'mobile': False,
                                             'landline_local': True})

        invalid = {"2123456": [errors['no-parse']],
                   "123456": [errors['no-parse']],
                   "12345": [errors['no-parse']],
                   "1234": [errors['no-parse']]}

        self.assertFieldOutput(LTPhoneField, {}, invalid,
                               field_kwargs={'mobile': False})

        self.assertRaises(ValueError, LTPhoneField, landline=False,
                          landline_local=True)

    def test_LTPhoneField_landline(self):
        errors = LTPhoneField().error_messages

        valid = {'850000000': '+37050000000',
                 '37050000000': '+37050000000',
                 '+37050000000': '+37050000000'}
        invalid = {'3705000000': [errors['no-parse']],
                   '370500000000': [errors['no-parse']],
                   '50000000': [errors['no-parse']],
                   '800023456': [errors['no-parse']]}

        self.assertFieldOutput(LTPhoneField, valid, invalid,
                               field_kwargs={'mobile': False})
