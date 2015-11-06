# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.br.forms import (BRZipCodeField, BRCNPJField, BRCPFField,
                                  BRPhoneNumberField, BRStateSelect,
                                  BRStateChoiceField, BRProcessoField)


class BRLocalFlavorTests(SimpleTestCase):
    def test_BRZipCodeField(self):
        error_format = ['Enter a zip code in the format XXXXX-XXX.']
        valid = {
            '12345-123': '12345-123',
        }
        invalid = {
            '12345_123': error_format,
            '1234-123': error_format,
            'abcde-abc': error_format,
            '12345-': error_format,
            '-123': error_format,
        }
        self.assertFieldOutput(BRZipCodeField, valid, invalid)

    def test_BRCNPJField(self):
        error_format = ['Invalid CNPJ number.']
        valid = {
            '64.132.916/0001-88': '64.132.916/0001-88',
            '64-132-916/0001-88': '64-132-916/0001-88',
            '64132916/0001-88': '64132916/0001-88',
        }
        invalid = {
            '../-12345678901210': error_format,
            '12-345-678/9012-10': error_format,
            '12.345.678/9012-10': error_format,
            '12345678/9012-10': error_format,
            '64.132.916/0001-XX': error_format,
        }
        self.assertFieldOutput(BRCNPJField, valid, invalid)

    def test_BRCPFField(self):
        error_format = ['Invalid CPF number.']
        error_atmost_chars = ['Ensure this value has at most 14 characters (it has 15).']
        error_atleast_chars = ['Ensure this value has at least 11 characters (it has 10).']
        error_atmost = ['This field requires at most 11 digits or 14 characters.']
        valid = {
            '663.256.017-26': '663.256.017-26',
            '66325601726': '66325601726',
            '375.788.573-20': '375.788.573-20',
            '84828509895': '84828509895',
        }
        invalid = {
            '..-48929465454': error_format,
            '489.294.654-54': error_format,
            '295.669.575-98': error_format,
            '111.111.111-11': error_format,
            '11111111111': error_format,
            '222.222.222-22': error_format,
            '22222222222': error_format,
            '539.315.127-22': error_format,
            '375.788.573-XX': error_format,
            '375.788.573-000': error_atmost_chars,
            '123.456.78': error_atleast_chars,
            '123456789555': error_atmost,
        }
        self.assertFieldOutput(BRCPFField, valid, invalid)

    def test_BRPhoneNumberField(self):
        error_format = [('Phone numbers must be in either of the following '
                         'formats: XX-XXXX-XXXX or XX-XXXXX-XXXX.')]
        valid = {
            '41-3562-3464': '41-3562-3464',
            '4135623464': '41-3562-3464',
            '41 3562-3464': '41-3562-3464',
            '41 3562 3464': '41-3562-3464',
            '(41) 3562 3464': '41-3562-3464',
            '41.3562.3464': '41-3562-3464',
            '41.93562.3464': '41-93562-3464',
            '41.3562-3464': '41-3562-3464',
            ' (41) 3562.3464': '41-3562-3464',
            ' (41) 98765.3464': '41-98765-3464',
            '(16) 91342-4325': '16-91342-4325',
        }
        invalid = {
            '11-914-925': error_format,
            '11-9144-43925': error_format,
            '11-91342-94325': error_format,
            '411-9134-9435': error_format,
            '+55-41-3562-3464': error_format,
            '41 3562–3464': error_format,
        }
        self.assertFieldOutput(BRPhoneNumberField, valid, invalid)

    def test_BRProcessoField(self):
        error_format = ['Invalid Process number.']
        error_atmost_chars = [
            'Ensure this value has at most 25 characters (it has 27).'
        ]
        error_atleast_chars = [
            'Ensure this value has at least 20 characters (it has 19).'
        ]
        valid = {
            '0013753-68.2014.8.21.0003': '0013753-68.2014.8.21.0003',
            '0002684-10.2012.8.21.0003': '0002684-10.2012.8.21.0003',
            '00026841020128210003': '00026841020128210003',
            '0019536-41.2014.8.21.0003': '0019536-41.2014.8.21.0003',
            '0017279-66.2007.811.0003': '0017279-66.2007.811.0003',
        }
        invalid = {
            '-....00137536820148210003': error_format,
            '00137531820148210003': error_format,
            '0137531820148210003': error_atleast_chars,
            '001375318201482100031111123': error_atmost_chars,
        }
        self.assertFieldOutput(BRProcessoField, valid, invalid)

    def test_BRStateSelect(self):
        f = BRStateSelect()
        out = '''<select name="states">
<option value="AC">Acre</option>
<option value="AL">Alagoas</option>
<option value="AP">Amap\xe1</option>
<option value="AM">Amazonas</option>
<option value="BA">Bahia</option>
<option value="CE">Cear\xe1</option>
<option value="DF">Distrito Federal</option>
<option value="ES">Esp\xedrito Santo</option>
<option value="GO">Goi\xe1s</option>
<option value="MA">Maranh\xe3o</option>
<option value="MT">Mato Grosso</option>
<option value="MS">Mato Grosso do Sul</option>
<option value="MG">Minas Gerais</option>
<option value="PA">Par\xe1</option>
<option value="PB">Para\xedba</option>
<option value="PR" selected="selected">Paran\xe1</option>
<option value="PE">Pernambuco</option>
<option value="PI">Piau\xed</option>
<option value="RJ">Rio de Janeiro</option>
<option value="RN">Rio Grande do Norte</option>
<option value="RS">Rio Grande do Sul</option>
<option value="RO">Rond\xf4nia</option>
<option value="RR">Roraima</option>
<option value="SC">Santa Catarina</option>
<option value="SP">S\xe3o Paulo</option>
<option value="SE">Sergipe</option>
<option value="TO">Tocantins</option>
</select>'''
        self.assertHTMLEqual(f.render('states', 'PR'), out)

    def test_BRStateChoiceField(self):
        error_invalid = ['Select a valid brazilian state. That state is not one of the available states.']
        valid = {
            'AC': 'AC',
            'AL': 'AL',
            'AP': 'AP',
            'AM': 'AM',
            'BA': 'BA',
            'CE': 'CE',
            'DF': 'DF',
            'ES': 'ES',
            'GO': 'GO',
            'MA': 'MA',
            'MT': 'MT',
            'MS': 'MS',
            'MG': 'MG',
            'PA': 'PA',
            'PB': 'PB',
            'PR': 'PR',
            'PE': 'PE',
            'PI': 'PI',
            'RJ': 'RJ',
            'RN': 'RN',
            'RS': 'RS',
            'RO': 'RO',
            'RR': 'RR',
            'SC': 'SC',
            'SP': 'SP',
            'SE': 'SE',
            'TO': 'TO',
        }
        invalid = {
            'pr': error_invalid,
        }
        self.assertFieldOutput(BRStateChoiceField, valid, invalid)
