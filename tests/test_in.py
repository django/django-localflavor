from django.test import SimpleTestCase

from localflavor.in_.forms import INAadhaarNumberField, INStateField, INStateSelect, INZipCodeField


class INLocalFlavorTests(SimpleTestCase):

    def test_INPStateSelect(self):
        f = INStateSelect()
        out = '''<select name="state">
<option value="KA">Karnataka</option>
<option value="AP" selected="selected">Andhra Pradesh</option>
<option value="KL">Kerala</option>
<option value="TN">Tamil Nadu</option>
<option value="MH">Maharashtra</option>
<option value="UP">Uttar Pradesh</option>
<option value="GA">Goa</option>
<option value="GJ">Gujarat</option>
<option value="RJ">Rajasthan</option>
<option value="HP">Himachal Pradesh</option>
<option value="TG">Telangana</option>
<option value="AR">Arunachal Pradesh</option>
<option value="AS">Assam</option>
<option value="BR">Bihar</option>
<option value="CT">Chattisgarh</option>
<option value="HR">Haryana</option>
<option value="JH">Jharkhand</option>
<option value="MP">Madhya Pradesh</option>
<option value="MN">Manipur</option>
<option value="ML">Meghalaya</option>
<option value="MZ">Mizoram</option>
<option value="NL">Nagaland</option>
<option value="OR">Odisha</option>
<option value="PB">Punjab</option>
<option value="SK">Sikkim</option>
<option value="TR">Tripura</option>
<option value="UT">Uttarakhand</option>
<option value="WB">West Bengal</option>
<option value="AN">Andaman and Nicobar Islands</option>
<option value="CH">Chandigarh</option>
<option value="DH">Dadra and Nagar Haveli and Daman and Diu</option>
<option value="DL">Delhi</option>
<option value="JK">Jammu and Kashmir</option>
<option value="LD">Lakshadweep</option>
<option value="LA">Ladakh</option>
<option value="PY">Puducherry</option>
</select>'''
        self.assertHTMLEqual(f.render('state', 'AP'), out)

    def test_INZipCodeField(self):
        error_format = ['Enter a zip code in the format XXXXXX or XXX XXX.']
        valid = {
            '360311': '360311',
            '360 311': '360311',
        }
        invalid = {
            '36 0311': error_format,
            '3603111': error_format,
            '360 31': error_format,
            '36031': error_format,
            'O2B 2R3': error_format
        }
        self.assertFieldOutput(INZipCodeField, valid, invalid)

    def test_INAadhaarNumberField(self):
        error_format = ['Enter a valid Aadhaar number in XXXX XXXX XXXX or '
                        'XXXX-XXXX-XXXX format.']
        valid = {
            '3603-1178-8988': '3603 1178 8988',
            '1892 3114 7727': '1892 3114 7727',
        }
        invalid = {
            '9910 182': error_format,
            '3603111': error_format,
            '000 0000 0000': error_format,
            '0000 0000 0000': error_format,
            '18888 8882 8288': error_format
        }
        self.assertFieldOutput(INAadhaarNumberField, valid, invalid)

    def test_INStateField(self):
        error_format = ['Enter an Indian state or territory.']
        valid = {
            'an': 'AN',
            'AN': 'AN',
            'andaman and nicobar': 'AN',
            'andra pradesh': 'AP',
            'andrapradesh': 'AP',
            'andhrapradesh': 'AP',
            'ap': 'AP',
            'andhra pradesh': 'AP',
            'ar': 'AR',
            'arunachal pradesh': 'AR',
            'assam': 'AS',
            'as': 'AS',
            'bihar': 'BR',
            'br': 'BR',
            'cg': 'CG',
            'chattisgarh': 'CG',
            'ch': 'CH',
            'chandigarh': 'CH',
            'daman and diu': 'DD',
            'dd': 'DD',
            'dl': 'DL',
            'delhi': 'DL',
            'dn': 'DN',
            'dadra and nagar haveli': 'DN',
            'ga': 'GA',
            'goa': 'GA',
            'gj': 'GJ',
            'gujarat': 'GJ',
            'himachal pradesh': 'HP',
            'hp': 'HP',
            'hr': 'HR',
            'haryana': 'HR',
            'jharkhand': 'JH',
            'jh': 'JH',
            'jammu and kashmir': 'JK',
            'jk': 'JK',
            'karnataka': 'KA',
            'karnatka': 'KA',
            'ka': 'KA',
            'kerala': 'KL',
            'kl': 'KL',
            'ld': 'LD',
            'lakshadweep': 'LD',
            'maharastra': 'MH',
            'mh': 'MH',
            'maharashtra': 'MH',
            'meghalaya': 'ML',
            'ml': 'ML',
            'mn': 'MN',
            'manipur': 'MN',
            'madhya pradesh': 'MP',
            'mp': 'MP',
            'mizoram': 'MZ',
            'mizo': 'MZ',
            'mz': 'MZ',
            'nl': 'NL',
            'nagaland': 'NL',
            'orissa': 'OR',
            'odisa': 'OR',
            'orisa': 'OR',
            'or': 'OR',
            'pb': 'PB',
            'punjab': 'PB',
            'py': 'PY',
            'pondicherry': 'PY',
            'rajasthan': 'RJ',
            'rajastan': 'RJ',
            'rj': 'RJ',
            'sikkim': 'SK',
            'sk': 'SK',
            'tamil nadu': 'TN',
            'tn': 'TN',
            'tamilnadu': 'TN',
            'tamilnad': 'TN',
            'telangana': 'TG',
            'tg': 'TG',
            'tr': 'TR',
            'tripura': 'TR',
            'ua': 'UA',
            'uttarakhand': 'UA',
            'up': 'UP',
            'uttar pradesh': 'UP',
            'westbengal': 'WB',
            'bengal': 'WB',
            'wb': 'WB',
            'west bengal': 'WB'
        }
        invalid = {
            'florida': error_format,
            'FL': error_format,
        }
        self.assertFieldOutput(INStateField, valid, invalid)
