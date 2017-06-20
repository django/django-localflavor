from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.nz.forms import (NZBankAccountNumberField, NZNorthIslandCouncilSelect, NZPhoneNumberField,
                                  NZPostCodeField, NZProvinceSelect, NZRegionSelect, NZSouthIslandCouncilSelect)


class NZLocalFlavorTests(SimpleTestCase):

    def test_NZRegionSelect(self):
        nzregion = NZRegionSelect()
        expected = '''<select name="nzregion">
<option value="NZ-NTL">Northland</option>
<option value="NZ-AUK">Auckland</option>
<option value="NZ-WKO">Waikato</option>
<option value="NZ-BOP">Bay of Plenty</option>
<option value="NZ-GIS">Gisborne</option>
<option value="NZ-HKB">Hawke&#39;s Bay</option>
<option value="NZ-TKI">Taranaki</option>
<option value="NZ-MWT">Manawatu-Wanganui</option>
<option value="NZ-WGN">Wellington</option>
<option value="NZ-TAS">Tasman</option>
<option value="NZ-NSN">Nelson</option>
<option value="NZ-MBH">Marlborough</option>
<option value="NZ-WTC">West Coast</option>
<option value="NZ-CAN" selected="selected">Canterbury</option>
<option value="NZ-OTA">Otago</option>
<option value="NZ-STL">Southland</option>
</select>'''
        self.assertHTMLEqual(nzregion.render('nzregion', 'NZ-CAN'), expected)

    def test_NZProvinceSelect(self):
        nzprovince = NZProvinceSelect()
        expected = '''<select name="nzprovince">
<option value="Auckland">Auckland</option>
<option value="Taranaki">Taranaki</option>
<option value="Hawke&#39;s Bay">Hawke&#39;s Bay</option>
<option value="Wellington">Wellington</option>
<option value="Marlborough">Marlborough</option>
<option value="Nelson">Nelson</option>
<option value="Canterbury" selected="selected">Canterbury</option>
<option value="South Canterbury">South Canterbury</option>
<option value="Westland">Westland</option>
<option value="Otago">Otago</option>
<option value="Southland">Southland</option>
<option value="Chatham Islands">Chatham Islands</option>
</select>'''
        self.assertHTMLEqual(nzprovince.render('nzprovince', 'Canterbury'), expected)

    def test_NZNorthIslandCouncilSelect(self):
        nznorthisland = NZNorthIslandCouncilSelect()
        expected = '''<select name="nznorthisland">
<option value="Far North">Far North District</option>
<option value="Whangarei">Whangarei District</option>
<option value="Kaipara">Kaipara District</option>
<option value="Auckland">Auckland</option>
<option value="Thames-Coromandel">Thames-Coromandel District</option>
<option value="Hauraki">Hauraki District</option>
<option value="Waikato">Waikato District</option>
<option value="Matamata-Piako">Matamata-Piako District</option>
<option value="Hamilton">Hamilton</option>
<option value="Waipa">Waipa District</option>
<option value="South Waikato">South Waikato District</option>
<option value="Otorohanga">Otorohanga District</option>
<option value="Waitomo">Waitomo District</option>
<option value="Taupo" selected="selected">Taupo District</option>
<option value="Western Bay of Plenty">Western Bay of Plenty District</option>
<option value="Tauranga">Tauranga</option>
<option value="Opotiki">Opotiki District</option>
<option value="Whakatane">Whakatane District</option>
<option value="Rotorua\t">Rotorua District\t</option>
<option value="Kawerau">Kawerau District</option>
<option value="Gisborne">Gisborne District</option>
<option value="Wairoa">Wairoa District</option>
<option value="Hastings">Hastings District</option>
<option value="Napier">Napier</option>
<option value="Central Hawke&#39;s Bay">Central Hawke&#39;s Bay District</option>
<option value="New Plymouth">New Plymouth District</option>
<option value="Stratford">Stratford District</option>
<option value="South Taranaki">South Taranaki District</option>
<option value="Ruapehu">Ruapehu District</option>
<option value="Rangitikei">Rangitikei District</option>
<option value="Wanganui">Wanganui District</option>
<option value="Manawatu">Manawatu District</option>
<option value="Palmerston North">Palmerston North</option>
<option value="Tararua">Tararua District</option>
<option value="Horowhenua">Horowhenua District</option>
<option value="Masterton">Masterton District</option>
<option value="Kapiti Coast">Kapiti Coast District</option>
<option value="Carterton">Carterton District</option>
<option value="South Wairarapa">South Wairarapa District</option>
<option value="Upper Hutt">Upper Hutt</option>
<option value="Porirua">Porirua</option>
<option value="Hutt">Hutt</option>
<option value="Wellington">Wellington</option>
</select>'''
        self.assertHTMLEqual(nznorthisland.render('nznorthisland', 'Taupo'), expected)

    def test_NZSouthIslandCouncilSelect(self):
        nzsouthisland = NZSouthIslandCouncilSelect()
        expected = '''<select name="nzsouthisland">
<option value="Tasman">Tasman District</option>
<option value="Nelson">Nelson</option>
<option value="Marlborough">Marlborough District</option>
<option value="Buller">Buller District</option>
<option value="Grey">Grey District</option>
<option value="Westland">Westland District</option>
<option value="Kaikoura">Kaikoura District</option>
<option value="Hurunui">Hurunui District</option>
<option value="Selwyn" selected="selected">Selwyn District</option>
<option value="Waimakariri">Waimakariri District</option>
<option value="Christchurch">Christchurch</option>
<option value="Ashburton">Ashburton District</option>
<option value="Mackenzie">Mackenzie District</option>
<option value="Timaru">Timaru District</option>
<option value="Waimate">Waimate District</option>
<option value="Waitaki">Waitaki District</option>
<option value="Queenstown-Lakes">Queenstown-Lakes District</option>
<option value="Central Otago">Central Otago District</option>
<option value="Dunedin">Dunedin</option>
<option value="Clutha">Clutha District</option>
<option value="Southland">Southland District</option>
<option value="Gore">Gore District</option>
<option value="Invercargill">Invercargill</option>
</select>'''
        self.assertHTMLEqual(nzsouthisland.render('nzsouthisland', 'Selwyn'), expected)

    def test_NZPostCodeField(self):
        error_format = ['Invalid post code.']
        valid = {
            '7645': '7645',
            '8022': '8022',
        }
        invalid = {
            '12345': error_format,
            'tbas': error_format,
        }
        self.assertFieldOutput(NZPostCodeField, valid, invalid)

    def test_NZPhoneNumberField(self):
        error_format = ['Invalid phone number.']
        valid = {
            '0800 DJANGO': '0800DJANGO',
            '0800 123456': '0800123456',
            '(0800) 123456': '0800123456',
            '0800 - 123456': '0800123456',
            '0800_DJANGO': '0800DJANGO',
            '021 123 4567': '0211234567',
            '021 123 45678': '02112345678',
            '021 - 123567': '021123567',
            '+64 21 123 4567': '0064211234567',
            '++64 21 123 4567': '0064211234567',
            '0064 21 123 4567': '0064211234567',
            '03 123 4567': '031234567',
            '+ 64 3 123 4567': '006431234567',
            '++ 64 3 123 4567': '006431234567',
        }
        invalid = {
            '+64 800 DJANGO': error_format,
            '03 123 456': error_format,
        }
        self.assertFieldOutput(NZPhoneNumberField, valid, invalid)

    def test_NZBankAccountNumberField(self):
        error_format = ['Invalid bank account number.']
        valid = {
            '01-1234-1234567-12': '01-1234-1234567-012',
            '01 1234 1234567 12': '01-1234-1234567-012',
            '011234123456712': '01-1234-1234567-012',
            '01-1234-1234567-123': '01-1234-1234567-123',
            '01 1234 1234567 123': '01-1234-1234567-123',
            '0112341234567123': '01-1234-1234567-123',
        }
        invalid = {
            '01-123-1234567-1': error_format,
        }
        self.assertFieldOutput(NZBankAccountNumberField, valid, invalid)
