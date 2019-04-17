from django.test import TestCase

from localflavor.md import forms

from .forms import MDPlaceForm


class MDLocalFlavorTests(TestCase):

    def setUp(self):
        self.data = {
            'idno': '1231231231231',
            'company_type_1': 'SRL',
            'company_type_2': 'II',
            'license_plate': 'KBC 123',
        }

    def _get_form(self):
        return MDPlaceForm(self.data)

    def _get_model(self):
        form = self._get_form()
        if form.is_valid():
            return form.save()

    def test_MDIDNOField(self):
        error_format = ['Enter a valid IDNO number.']
        valid = {
            '2006042220032': '2006042220032',
        }
        invalid = {
            '1111': error_format,
            'foo': error_format,
        }
        self.assertFieldOutput(forms.MDIDNOField, valid, invalid)

    def test_MDLicensePlateField(self):
        error_format = ['Enter a valid license plate.']
        valid = {
            'abj 123': 'abj 123',
            'K BC 123': 'K BC 123',
            'FL BC 123': 'FL BC 123',

            'RM P 001': 'RM P 001',
            'RM G 001': 'RM G 001',
            'RM A 123': 'RM A 123',

            'CD 112 AA': 'CD 112 AA',
            'TC 113 AA': 'TC 113 AA',
            'CD 111 A': 'CD 111 A',

            'RM 1123': 'RM 1123',

            'MIC 1234': 'MIC 1234',
            'MAI 1234': 'MAI 1234',

            'H 1234': 'H 1234',
            'FA 1234': 'FA 1234',
            'DG 1234': 'DG 1234',
            'SP 123': 'SP 123',
        }
        invalid = {
            'KK BC 123': error_format,
            'KKBC 123': error_format,
            'TC 113 AAA': error_format,
            'MAI 112': error_format,
            'SP 1121': error_format,
            'SP11211234': error_format,
        }
        self.assertFieldOutput(forms.MDLicensePlateField, valid, invalid)

    def test_MD_model(self):
        model = self._get_model()

        self.assertEqual(model.idno, '1231231231231')
        self.assertEqual(model.company_type_1, 'SRL')
        self.assertEqual(model.company_type_2, 'II')
        self.assertEqual(model.license_plate, 'KBC 123')

        model.clean_fields()

    def test_get_display_methods(self):
        model = self._get_model()
        self.assertEqual(model.get_company_type_1_display(), 'Societate cu răspundere limitată')
        self.assertEqual(model.get_company_type_2_display(), 'Întreprindere Individuală')

    def test_MDCompanyTypeSelect(self):
        form = forms.MDCompanyTypesSelect()
        expected = '''
        <select name="companies">
            <option value="II">Întreprindere Individuală</option>
            <option value="SA">Societate pe acţiuni</option>
            <option value="SNC">Societate în nume colectiv</option>
            <option value="SC">Societatea în comandită</option>
            <option value="CP">Cooperativa de producţie</option>
            <option value="CI">Cooperativa de întreprinzători</option>
            <option value="SRL" selected="selected">Societate cu răspundere limitată</option>
            <option value="GT">Gospodăria ţărănească</option>
        </select>'''
        companies_form = form.render('companies', 'SRL')
        self.assertHTMLEqual(expected, companies_form)

    def test_MDRegionSelect(self):
        form = forms.MDRegionSelect()
        expected = '''<option value="C" selected>Chișinău</option>'''
        companies_form = form.render('regions', 'C')
        self.assertTrue(expected in companies_form)
