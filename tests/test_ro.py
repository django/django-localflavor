from django.test import SimpleTestCase

from localflavor.ro.forms import ROCIFField, ROCNPField, ROCountyField, ROCountySelect, ROPostalCodeField


class ROLocalFlavorTests(SimpleTestCase):
    def test_ROCountySelect(self):
        f = ROCountySelect()
        out = '''<select name="county">
                <option value="AB">Alba</option>
                <option value="AR">Arad</option>
                <option value="AG">Arge\u0219</option>
                <option value="BC">Bac\u0103u</option>
                <option value="BH">Bihor</option>
                <option value="BN">Bistri\u021ba-N\u0103s\u0103ud</option>
                <option value="BT">Boto\u0219ani</option>
                <option value="BV">Bra\u0219ov</option>
                <option value="BR">Br\u0103ila</option>
                <option value="B">Bucure\u0219ti</option>
                <option value="BZ">Buz\u0103u</option>
                <option value="CS">Cara\u0219-Severin</option>
                <option value="CL">C\u0103l\u0103ra\u0219i</option>
                <option value="CJ" selected="selected">Cluj</option>
                <option value="CT">Constan\u021ba</option>
                <option value="CV">Covasna</option>
                <option value="DB">D\xe2mbovi\u021ba</option>
                <option value="DJ">Dolj</option>
                <option value="GL">Gala\u021bi</option>
                <option value="GR">Giurgiu</option>
                <option value="GJ">Gorj</option>
                <option value="HR">Harghita</option>
                <option value="HD">Hunedoara</option>
                <option value="IL">Ialomi\u021ba</option>
                <option value="IS">Ia\u0219i</option>
                <option value="IF">Ilfov</option>
                <option value="MM">Maramure\u0219</option>
                <option value="MH">Mehedin\u021bi</option>
                <option value="MS">Mure\u0219</option>
                <option value="NT">Neam\u021b</option>
                <option value="OT">Olt</option>
                <option value="PH">Prahova</option>
                <option value="SM">Satu Mare</option>
                <option value="SJ">S\u0103laj</option>
                <option value="SB">Sibiu</option>
                <option value="SV">Suceava</option>
                <option value="TR">Teleorman</option>
                <option value="TM">Timi\u0219</option>
                <option value="TL">Tulcea</option>
                <option value="VS">Vaslui</option>
                <option value="VL">V\xe2lcea</option>
                <option value="VN">Vrancea</option>
                </select>
                '''
        self.assertHTMLEqual(f.render('county', 'CJ'), out)

    def test_ROCIFField(self):
        error_invalid = ['Enter a valid CIF.']
        error_atmost = ['Ensure this value has at most 10 characters (it has 11).']
        error_atleast = ['Ensure this value has at least 2 characters (it has 1).']
        valid = {
            '21694681': '21694681',
            '21694681 ': '21694681',
            'RO21694681': '21694681',
        }
        invalid = {
            '21694680': error_invalid,
            '21694680000': error_atmost,
            '0': error_atleast + error_invalid,
        }
        self.assertFieldOutput(ROCIFField, valid, invalid)

    def test_ROCNPField(self):
        error_invalid = ['Enter a valid CNP.']
        error_atleast = ['Ensure this value has at least 13 characters (it has 10).']
        error_atmost = ['Ensure this value has at most 13 characters (it has 14).']
        valid = {
            '1981211204489': '1981211204489',
        }
        invalid = {
            '1981211204487': error_invalid,
            '1981232204489': error_invalid,
            '9981211204489': error_invalid,
            '9981211209': error_atleast + error_invalid,
            '19812112044891': error_atmost,
        }
        self.assertFieldOutput(ROCNPField, valid, invalid)

    def test_ROCountyField(self):
        error_format = ['Enter a Romanian county code or name.']
        valid = {
            'CJ': 'CJ',
            'cj': 'CJ',
            'Argeș': 'AG',
            'argeș': 'AG',
        }
        invalid = {
            'Arges': error_format,
        }
        self.assertFieldOutput(ROCountyField, valid, invalid)

    def test_ROPostalCodeField(self):
        error_atleast = ['Ensure this value has at least 6 characters (it has 5).']
        error_atmost = ['Ensure this value has at most 6 characters (it has 7).']
        error_invalid = ['Enter a valid postal code in the format XXXXXX']

        valid = {
            '400473': '400473',
        }
        invalid = {
            '40047': error_atleast + error_invalid,
            '4004731': error_atmost + error_invalid,
        }
        self.assertFieldOutput(ROPostalCodeField, valid, invalid)
