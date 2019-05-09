from django.test import SimpleTestCase

from localflavor.sg.forms import SGNRICFINField, SGPostCodeField


class SGLocalFlavorTests(SimpleTestCase):
    def test_SGPostCodeField(self):
        error_format = ['Enter a 6-digit postal code.']
        valid = {
            '247964': '247964',
            '050335': '050335',
            '520110': '520110',
            '521110': '521110',
        }
        invalid = {
            '0000': error_format,
            '0123': error_format,
            'e23fee': error_format,
        }
        self.assertFieldOutput(SGPostCodeField, valid, invalid)

    def test_SGNRICFINField(self):
        error_format = ['Invalid NRIC/FIN.']
        valid = {
            's8675985c': 'S8675985C',
            'S8776318H': 'S8776318H',
            ' G0746467W': 'G0746467W',
            'T1399266A': 'T1399266A',
            'F5401671U ': 'F5401671U',
        }
        invalid = {
            'S5777125G': error_format,
            'T4461323J': error_format,
            'A2119569M': error_format,
            'F8155379N': error_format,
            'G1087200K': error_format,
        }
        self.assertFieldOutput(SGNRICFINField, valid, invalid)
