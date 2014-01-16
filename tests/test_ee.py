from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.ee.forms import (EEZipCodeField, EEPersonalIdentificationCode,
                                  EECountySelect)


class EELocalFlavorTests(SimpleTestCase):
    def test_EECountySelect(self):
        f = EECountySelect()
        out = '''<select name="county">
<option value="37" selected="selected">Harjumaa</option>
<option value="39">Hiiumaa</option>
<option value="44">Ida-Virumaa</option>
<option value="49">J\xf5gevamaa</option>
<option value="51">J\xe4rvamaa</option>
<option value="57">L\xe4\xe4nemaa</option>
<option value="59">L\xe4\xe4ne-Virumaa</option>
<option value="65">P\xf5lvamaa</option>
<option value="67">P\xe4rnumaa</option>
<option value="70">Raplamaa</option>
<option value="74">Saaremaa</option>
<option value="78">Tartumaa</option>
<option value="82">Valgamaa</option>
<option value="84">Viljandimaa</option>
<option value="86">V\xf5rumaa</option>
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
