from django.test import SimpleTestCase

from localflavor.ee.forms import EEBusinessRegistryCode, EECountySelect, EEPersonalIdentificationCode, EEZipCodeField


class EELocalFlavorTests(SimpleTestCase):
    def test_EECountySelect(self):
        f = EECountySelect()
        out = '''<select name="county">
<option value="37" selected="selected">Harju County</option>
<option value="39">Hiiu County</option>
<option value="44">Ida-Viru County</option>
<option value="49">J\xf5geva County</option>
<option value="51">J\xe4rva County</option>
<option value="57">L\xe4\xe4ne County</option>
<option value="59">L\xe4\xe4ne-Viru County</option>
<option value="65">P\xf5lva County</option>
<option value="67">P\xe4rnu County</option>
<option value="70">Rapla County</option>
<option value="74">Saare County</option>
<option value="78">Tartu County</option>
<option value="82">Valga County</option>
<option value="84">Viljandi County</option>
<option value="86">V\xf5ru County</option>
</select>'''
        self.assertHTMLEqual(f.render('county', '37'), out)

    def test_EEZipCodeField(self):
        error_format = ['Enter a zip code in the format XXXXX.']
        valid = {
            '15165': '15165',
            '50090': '50090',
        }
        invalid = {
            '15I65': error_format,
            '999999': error_format,
            '01234': error_format,
        }
        self.assertFieldOutput(EEZipCodeField, valid, invalid)

    def test_EEPersonalIdentificationCode(self):
        invalid = ['Enter a valid Estonian personal identification code.']
        invalid_format = ['Enter an 11-digit Estonian personal identification code.']
        valid = {
            '32805100214': '32805100214',
            '61202291237': '61202291237',  # leap year
            '10001010002': '10001010002',  # checksum base 1
            '69912319998': '69912319998',  # checksum base 3
        }
        invalid = {
            '1234567890': invalid_format,
            '98765432100': invalid_format,  # invalid century
            '33333333333': invalid,  # invalid checksum
            '10102300002': invalid,  # invalid date
            '10000000001': invalid,  # invalid month/day
            '61402291232': invalid,  # not leap year
        }
        self.assertFieldOutput(EEPersonalIdentificationCode, valid, invalid)

    def test_EEBusinessRegistryCode(self):
        invalid = ['Enter a valid Estonian business registry code.']
        invalid_format = ['Enter an 8-digit Estonian business registry code.']
        valid = {
            '80053370': '80053370',
            '11694365': '11694365',  # checksum base 1
            '10223576': '10223576',  # checksum base 3
        }
        invalid = {
            '4329865': invalid_format,
            '33333333': invalid,  # invalid checksum
        }
        self.assertFieldOutput(EEBusinessRegistryCode, valid, invalid)
