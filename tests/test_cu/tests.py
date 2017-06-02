# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from localflavor.cu.forms import (
    CURegionField, CUProvinceField, CUZipCodeField, CUIdentityCardNumberField, CUPhoneNumberField
)

from .forms import CUSomewhereForm


class CULocalFlavorTests(TestCase):

    def setUp(self):
        self.data = {
            'province_1': 'PRI',
            'province_2': 'HAB',
            'region_1': 'OCC',
            'region_2': 'CTL',
            'zip_code': '20100',
            'id_number': '91021527832',
            'phone_number': '76895689',
        }

    def _get_form(self):
        return CUSomewhereForm(self.data)

    def _get_model(self):
        return self._get_form().save()

    def test_CURegionField(self):
        error_format = ['Enter a cuban region.']
        valid = {
            'occidental': 'OCC',
            'central': 'CTL',
            'oriental': 'OTL',
            # abbreviations
            'occ': 'OCC',
            'ctl': 'CTL',
            # with unneeded spaces
            '  otl  ': 'OTL',
        }
        invalid = {
            'invalid region': error_format,
        }
        self.assertFieldOutput(CURegionField, valid, invalid)

    def test_CUProvinceField(self):
        error_format = ['Enter a cuban province.']
        valid = {
            'pinar del río': 'PRI',
            'villa clara': 'VCL',
            # abbreviations
            'pr': 'PRI',
            'pri': 'PRI',
            'vc': 'VCL',
            'vcl': 'VCL',
            # with unneeded spaces
            '  pinar': 'PRI',
            '  las villas  ': 'VCL',
        }
        invalid = {
            'invalid province': error_format,
        }
        self.assertFieldOutput(CUProvinceField, valid, invalid)

    def test_CUZipCodeField(self):
        invalid_format = ['Enter a valid zip code in the format XXXXX.']
        valid = {
            '20100': '20100',
            '10400': '10400',
            '90100': '90100',
        }
        invalid = {
            'ABCDE': invalid_format,
            'A451B': invalid_format,
            '02010': invalid_format,
            '00200': invalid_format,
            '200': invalid_format,
            '102003': invalid_format,
        }
        self.assertFieldOutput(CUZipCodeField, valid, invalid)

    def test_CUIdentityCardNumberField(self):
        invalid_format = ['Enter a valid identity card number in the format XXXXXXXXXXX.']
        invalid_birthday = ['Enter a valid date (yymmdd) for the first 6 digits.']
        valid = {
            '09021527832': '09021527832',
            '45121201568': '45121201568',
            '85051802457': '85051802457',
        }
        invalid = {
            'AHSJKSJHSKS': invalid_format,
            '78SJKS458KS': invalid_format,
            '0902152783': invalid_format,
            '090215278324': invalid_format,
            '09023027832': invalid_birthday,
            '09043127832': invalid_birthday,
        }
        self.assertFieldOutput(CUIdentityCardNumberField, valid, invalid)

    def test_CUPhoneNumberField(self):
        invalid_format = ['Enter a valid phone number in the format XXXXXXXX.']
        valid = {
            '48759658': '48759658',
            '76648978': '76648978',
            '34568978': '34568978',
            '22568978': '22568978',
        }
        invalid = {
            'ASTESDJK': invalid_format,
            '45TE89J5': invalid_format,
            '4875965': invalid_format,
            '487596580': invalid_format,
            '08759658': invalid_format,
            '98759658': invalid_format,
            '88759658': invalid_format,
        }
        self.assertFieldOutput(CUPhoneNumberField, valid, invalid)

    def test_get_display_methods(self):
        somewhere = self._get_model()
        self.assertEqual(somewhere.get_province_1_display(), 'Pinar del Río')
        self.assertEqual(somewhere.get_province_2_display(), 'La Habana')
        self.assertEqual(somewhere.get_region_1_display(), 'Occidental')
        self.assertEqual(somewhere.get_region_2_display(), 'Central')

    def test_CURegionSelect_html(self):
        region_select_html = """
<select name="region_2" id="id_region_2">
<option value="">---------</option>
<option value="OCC">Occidental</option>
<option selected="selected" value="CTL">Central</option>
<option value="OTL">Oriental</option>
</select>"""
        self.assertHTMLEqual(str(self._get_form()['region_2']), region_select_html)

    def test_CUProvinceSelect_html(self):
        province_select_html = """
<select name="province_2" id="id_province_2">
<option value="">---------</option>
<option value="PRI">Pinar del Río</option>
<option value="ART">Artemisa</option>
<option value="MAY">Mayabeque</option>
<option selected="selected" value="HAB">La Habana</option>
<option value="MTZ">Matanzas</option>
<option value="CFG">Cienfuegos</option>
<option value="VCL">Villa Clara</option>
<option value="SSP">Sancti Spíritus</option>
<option value="CAV">Ciego de Ávila</option>
<option value="CMG">Camagüey</option>
<option value="LTU">Las Tunas</option>
<option value="HOL">Holguín</option>
<option value="GRA">Granma</option>
<option value="SCU">Santiago de Cuba</option>
<option value="GTM">Guantánamo</option>
<option value="IJV">Isla de la Juventud</option>
</select>"""
        self.assertHTMLEqual(str(self._get_form()['province_2']), province_select_html)

    def test_errors_messages(self):
        self.data.update({
            'province_1': '!!!',
            'province_2': '!!!',
            'region_1': '!!!',
            'region_2': '!!!',
            'zip_code': '!!!',
            'id_number': '!!!',
            'phone_number': '!!!',
        })

        form = self._get_form()
        self.assertFalse(form.is_valid())

        choice_messages = ['Select a valid choice. !!! is not one of the available choices.']
        self.assertEqual(form.errors['province_1'], ['Enter a cuban province.'])
        self.assertEqual(form.errors['province_2'], choice_messages)
        self.assertEqual(form.errors['region_1'], ['Enter a cuban region.'])
        self.assertEqual(form.errors['region_2'], choice_messages)
        self.assertEqual(form.errors['zip_code'], ["Enter a valid zip code in the format XXXXX."])
        self.assertEqual(form.errors['id_number'], ["Enter a valid identity card number in the format XXXXXXXXXXX."])
        self.assertEqual(form.errors['phone_number'], ["Enter a valid phone number in the format XXXXXXXX."])
