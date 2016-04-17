# -*- coding: utf-8 -*-
from django.test import SimpleTestCase
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import override

from localflavor.no.forms import NOMunicipalitySelect, NOPhoneNumberField, NOSocialSecurityNumber, NOZipCodeField


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

    def test_NOPhoneNumberField(self):
        error_format = [_('A phone number must be 8 digits and may have country code')]
        valid = {
            '12345678': '12345678',
            '12 34 56 78': '12 34 56 78',
            '123 45 678': '123 45 678',
            '+4712345678': '+4712345678',
            '+47 12345678': '+47 12345678',
            '+47 12 34 56 78': '+47 12 34 56 78',
            '+47 123 45 678': '+47 123 45 678',
        }
        invalid = {
            '12': error_format,  # to few digits
            'abcdefgh': error_format,  # illegal characters
            '1234567890': error_format,  # to many digits
            '+4512345678': error_format,  # wrong country code
        }
        self.assertFieldOutput(NOPhoneNumberField, valid, invalid)

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
