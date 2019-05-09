from django.test import SimpleTestCase

from localflavor.br import models
from localflavor.br.forms import (BRCNPJField, BRCPFField, BRProcessoField, BRStateChoiceField, BRStateSelect,
                                  BRZipCodeField)
from tests.test_br.forms import BRPersonProfileForm


class BRLocalFlavorTests(SimpleTestCase):
    def test_BRZipCodeField(self):
        error_format = ['Enter a postal code in the format 00000-000.']
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

        for postal_code, _ in invalid.items():
            form = BRPersonProfileForm({
                'postal_code': postal_code
            })

            self.assertFalse(form.is_valid())
            self.assertEqual(form.errors['postal_code'], error_format)

    def test_BRCNPJField(self):
        error_format = {
            'invalid': ['Invalid CNPJ number.'],
            'only_long_version': ['Ensure this value has at least 16 characters (it has 14).'],
            # The long version can be 16 or 18 characters long so actual error message is set dynamically when the
            # invalid_long dict is generated.
            'only_short_version': ['Ensure this value has at most 14 characters (it has %s).'],
        }

        long_version_valid = {
            '64.132.916/0001-88': '64.132.916/0001-88',
            '64-132-916/0001-88': '64-132-916/0001-88',
            '64132916/0001-88': '64132916/0001-88',
        }
        short_version_valid = {
            '64132916000188': '64132916000188',
        }
        valid = long_version_valid.copy()
        valid.update(short_version_valid)

        invalid = {
            '../-12345678901234': error_format['invalid'],
            '12-345-678/9012-10': error_format['invalid'],
            '12.345.678/9012-10': error_format['invalid'],
            '12345678/9012-10': error_format['invalid'],
            '64.132.916/0001-XX': error_format['invalid'],
        }
        self.assertFieldOutput(BRCNPJField, valid, invalid)

        # The short versions should be invalid when 'min_length=16' passed to the field.
        invalid_short = dict([(k, error_format['only_long_version']) for k in short_version_valid.keys()])
        self.assertFieldOutput(BRCNPJField, long_version_valid, invalid_short, field_kwargs={'min_length': 16})

        # The long versions should be invalid when 'max_length=14' passed to the field.
        invalid_long = dict([(k, [error_format['only_short_version'][0] % len(k)]) for k in long_version_valid.keys()])
        self.assertFieldOutput(BRCNPJField, short_version_valid, invalid_long, field_kwargs={'max_length': 14})

        for cnpj, invalid_msg in invalid.items():
            form = BRPersonProfileForm({
                'cnpj': cnpj
            })

            self.assertFalse(form.is_valid())
            self.assertEqual(form.errors['cnpj'], invalid_msg)

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
            '375.788.573-000': error_atmost_chars + error_format,
            '123.456.78': error_atleast_chars + error_format,
            '123456789555': error_atmost,
        }
        self.assertFieldOutput(BRCPFField, valid, invalid)

        for cpf, invalid_msg in invalid.items():
            form = BRPersonProfileForm({
                'cpf': cpf
            })

            self.assertFalse(form.is_valid())
            self.assertIn(form.errors['cpf'][0], invalid_msg)

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

    def test_model_form_valid(self):
        data_to_test = [
            {
                'cpf': '84828509895',
                'cnpj': '64132916000188',
                'postal_code': '08552-170'
            },
            {
                'cpf': '84828509895',
                'cnpj': '64132916/0001-88',
                'postal_code': '08552-170'
            },
            {
                'cpf': '663.256.017-26',
                'cnpj': '64.132.916/0001-88',
                'postal_code': '08552-170'
            }
        ]

        for case in data_to_test:
            form = BRPersonProfileForm(case)
            self.assertTrue(form.is_valid())


class BRLocalFlavorModelTests(SimpleTestCase):

    def test_BRCNPJField(self):
        instance = models.BRCNPJField()
        name, path, args, kwargs = instance.deconstruct()
        new_instance = models.BRCNPJField(*args, **kwargs)
        self.assertEqual(instance.max_length, new_instance.max_length)
        self.assertEqual(instance.description, new_instance.description)
        self.assertEqual(instance.validators, new_instance.validators)

    def test_BRCPFField(self):
        instance = models.BRCPFField()
        name, path, args, kwargs = instance.deconstruct()
        new_instance = models.BRCPFField(*args, **kwargs)
        self.assertEqual(instance.max_length, new_instance.max_length)
        self.assertEqual(instance.description, new_instance.description)
        self.assertEqual(instance.validators, new_instance.validators)

    def test_BRPostalCodeField(self):
        instance = models.BRPostalCodeField()
        name, path, args, kwargs = instance.deconstruct()
        new_instance = models.BRPostalCodeField(*args, **kwargs)
        self.assertEqual(instance.max_length, new_instance.max_length)
        self.assertEqual(instance.description, new_instance.description)
        self.assertEqual(instance.validators, new_instance.validators)
