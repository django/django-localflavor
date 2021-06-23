from django.test import SimpleTestCase
from django.utils.translation import gettext_lazy as _
from django.utils.translation import override

from localflavor.no.forms import NOBankAccountNumber, NOMunicipalitySelect, NOSocialSecurityNumber, NOZipCodeField


class NOLocalFlavorTests(SimpleTestCase):
    def test_NOZipCodeField(self):
        error_format = [_('Enter a zip code in the format XXXX.')]
        valid = {
            '1234': '1234',
        }
        invalid = {
            '12': error_format,  # to few digits
            'abcd': error_format,  # illegal characters
            '12345': error_format,  # to many digits
        }
        self.assertFieldOutput(NOZipCodeField, valid, invalid)

    def test_NOBankAccountNumber(self):
        error_format = [_('Enter a valid Norwegian bank account number.')]
        error_checksum = [_('Invalid control digit. Enter a valid Norwegian bank account number.')]
        error_length = [_('Invalid length. Norwegian bank account numbers are 11 digits long.')]

        # A good source of loads of highly-likely-to-be-valid examples are available at
        # http://www.skatteetaten.no/no/Person/Skatteoppgjor/Restskatt/Kontonummer-til-skatteoppkreverkontorene/
        valid = {
            '7694 05 12057': '76940512057',
            '7694.05.12057': '76940512057',
            '7694.05.12057  ': '76940512057',
            '1111.00.22222': '11110022222',
            '5555.88.43216': '55558843216',
            '63450618537': '63450618537',
            ' 6345.06.20027 ': '63450620027',
        }
        invalid = {
            '76940512056': error_checksum,  # invalid check digit
            '1111.00.22228': error_checksum,  # invalid check digit
            'abcdefgh': error_format,  # illegal characters, though it'll fail to create the checksum
            '1111a00b22222': error_format,  # illegal characters
            '769405120569': error_length,  # invalid length (and control number for that matter)
        }
        self.assertFieldOutput(NOBankAccountNumber, valid, invalid)

    def test_NOBankAccountNumber_formatting(self):
        form = NOBankAccountNumber()
        self.assertEqual(form.prepare_value('76940512057'), '7694.05.12057')
        self.assertEqual(form.prepare_value(' 7694 05 12057 '), '7694.05.12057')
        self.assertEqual(form.prepare_value('7694. 05.1205'), '7694.05.1205')
        self.assertEqual(form.prepare_value('7694.05.120.5'), '7694.05.1205')
        # In the event there's already empty/blank/null values present.
        # Any invalid data should be stopped by form.validate, which the above test should take care of.
        self.assertEqual(form.prepare_value(None), '')
        self.assertEqual(form.prepare_value(''), '')

    def test_NOSocialSecurityNumber(self):
        error_format = [_('Enter a valid Norwegian social security number.')]

        # Valid examples can be found at
        # http://www.fnrinfo.no/Verktoy/FinnLovlige_Dato.aspx
        valid = {
            '12031399902': '12031399902',
            '12031399589': '12031399589',
            '12031398876': '12031398876',
        }
        invalid = {
            '12': error_format,
            'abcdefgh': error_format,
            '40151398876': error_format,
        }
        self.assertFieldOutput(NOSocialSecurityNumber, valid, invalid)

    def test_NOMunicipalitySelect(self):
        with override('en'):
            f = NOMunicipalitySelect()
            out = '''<select name="municipalities">
    <option value="akershus" selected="selected">Akershus</option>
    <option value="austagder">Aust-Agder</option>
    <option value="buskerud">Buskerud</option>
    <option value="finnmark">Finnmark</option>
    <option value="hedmark">Hedmark</option>
    <option value="hordaland">Hordaland</option>
    <option value="janmayen">Jan Mayen</option>
    <option value="moreogromsdal">Møre og Romsdal</option>
    <option value="nordtrondelag">Nord-Trøndelag</option>
    <option value="nordland">Nordland</option>
    <option value="oppland">Oppland</option>
    <option value="oslo">Oslo</option>
    <option value="rogaland">Rogaland</option>
    <option value="sognogfjordane">Sogn og Fjordane</option>
    <option value="svalbard">Svalbard</option>
    <option value="sortrondelag">Sør-Trøndelag</option>
    <option value="telemark">Telemark</option>
    <option value="troms">Troms</option>
    <option value="vestagder">Vest-Agder</option>
    <option value="vestfold">Vestfold</option>
    <option value="ostfold">Østfold</option>
</select>'''
        self.assertHTMLEqual(f.render('municipalities', 'akershus'), out)
