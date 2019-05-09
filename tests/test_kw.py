from django.test import SimpleTestCase

from localflavor.kw.forms import KWAreaSelect, KWCivilIDNumberField, KWGovernorateSelect


class KWLocalFlavorTests(SimpleTestCase):
    maxDiff = None
    def test_KWCivilIDNumberField(self):
        error_invalid = ['Enter a valid Kuwaiti Civil ID number']
        valid = {
            '282040701483': '282040701483',
            '300092400929': '300092400929',
            '304022600325': '304022600325',
        }
        invalid = {
            '289332013455': error_invalid,
            '300000000005': error_invalid,
            '289332Ol3455': error_invalid,
            '2*9332013455': error_invalid,
        }
        self.assertFieldOutput(KWCivilIDNumberField, valid, invalid)

    def test_KWGovernorateSelect(self):
        f = KWGovernorateSelect()
        result = '''<select name="governorates">
<option value="AH">Ahmadi</option>
<option value="FA">Farwaniyah</option>
<option value="JA">Jahra</option>
<option value="KU" selected="selected">Capital</option>
<option value="HA">Hawalli</option>
<option value="MU">Mubarak Al Kabir</option>
</select>'''
        self.assertHTMLEqual(f.render('governorates', 'KU'), result)

    def test_KWAreaSelect(self):
        f = KWAreaSelect()
        result = \
            '''<select name="areas">
<optgroup label="Kuwait City">
<option value="AS">Abdullah Al-Salem</option>
<option value="AD">Adailiya</option>
<option value="BQ">Bneid Al Qar</option>
<option value="DY">Daiya</option>
<option value="DS">Dasma</option>
<option value="DN">Dasman</option>

<option value="DH">Doha</option>
<option value="FH">Faiha</option>
<option value="GR">Granada</option>
<option value="JA">Jaber Al Ahmad</option>
<option value="JB">Jibla</option>
<option value="KF">Kaifan</option>
<option value="KH">Khaldiya</option>
<option value="KC">Kuwait City</option>
<option value="KZ">Kuwait Free Trade Zone</option>
<option value="MS">Mansouriya</option>
<option value="MR">Mirqab</option>
<option value="MC">Mubarekiya Camps</option>
<option value="NT">Nahdha</option>
<option value="NS">North West Al-Sulaibikhat</option>
<option value="NZ">Nuzha</option>
<option value="QD">Qadsiya</option>
<option value="QA">Qairawan</option>
<option value="QT">Qortuba</option>
<option value="RW">Rawda</option>
<option value="SH">Salhiya</option>
<option value="SM">Shamiya</option>
<option value="SQ">Sharq</option>
<option value="SA">Shuwaikh Administrative</option>
<option value="SI">Shuwaikh Industrial</option>
<option value="SR">Shuwaikh Residential</option>
<option value="ST">Sulaibikhat</option>
<option value="SU">Surra</option>
<option value="YR">Yarmouk</option>
</optgroup>
<optgroup label="Farwaniya">
<option value="AB">Abbasiya</option>
<option value="AM">Abdullah Al Mubarak Al Sabah</option>
<option value="AK">Abraq Khaitan</option>
<option value="DJ">Al-Dajeej</option>
<option value="SD">Al-Shadadiya</option>
<option value="AN">Andalous</option>
<option value="AR">Ardiya</option>
<option value="AI">Ardiya Small Industrial</option>
<option value="AZ">Ardiya Storage Zone</option>
<option value="FR">Farwaniya</option>
<option value="FD">Firdous</option>
<option value="IS">Ishbiliya</option>
<option value="JS">Jeleeb Al-Shuyoukh</option>
<option value="KT">Khaitan</option>
<option value="OM">Omariya</option>
<option value="RA">Rabia</option>
<option value="RI">Rai</option>
<option value="RH">Rehab</option>
<option value="RG">Rigai</option>
<option value="SN">Sabah Al Nasser</option>
<option value="SK">South Khaitan - Exhibits</option>
</optgroup>
<optgroup label="Mubarak Al Kabir">
<option value="AH">Abu Al Hasaniya</option>
<option value="AF">Abu Fatira</option>
<option value="AA">Adan</option>
<option value="MS">Al-Masayel</option>
<option value="CS">Coast Strip B</option>
<option value="FN">Fnaitees</option>
<option value="ME">Messila</option>
<option value="MK">Mubarak Al Kabeer</option>
<option value="QU">Qurain</option>
<option value="QS">Qusor</option>
<option value="SS">Sabah Al Salem</option>
<option value="SL">Sabhan Industrial Area</option>
<option value="SW">South Wista</option>
<option value="WA">West Abu Fatira Small Industrial</option>
</optgroup>
<optgroup label="Hawally">
<option value="AQ">Al-Siddeeq</option>
<option value="AJ">Anjafa</option>
<option value="BY">Bayan</option>
<option value="HT">Hateen</option>
<option value="HW">Hawally</option>
<option value="JR">Jabriya</option>
<option value="MH">Maidan Hawally</option>
<option value="MI">Mishref</option>
<option value="MA">Mubarak Al-Abdullah</option>
<option value="RU">Rumaithiya</option>
<option value="AL">Al-Salam</option>
<option value="SY">Salmiya</option>
<option value="LW">Salwa</option>
<option value="SB">Shaab</option>
<option value="DA">Shuhada</option>
<option value="ZH">Zahra</option>
</optgroup>
<optgroup label="Ahmadi">
<option value="BH">Abu Halifa</option>
<option value="MD">Ahmadi</option>
<option value="KI">Al Khiran</option>
<option value="AW">Al Wafrah</option>
<option value="JU">Al-Julaia_&#39;a</option>
<option value="NU">Al-Nuwaiseeb</option>
<option value="RQ">Al-Riqqa</option>
<option value="SE">Ali Sabah Al Salem</option>
<option value="HI">Assabahiyah</option>
<option value="BN">Bnaider</option>
<option value="DR">Dahar</option>
<option value="EQ">Eqaila</option>
<option value="FA">Fahad Al Ahmad</option>
<option value="FE">Fahaheel</option>
<option value="FI">Fintas</option>
<option value="HD">Hadiya</option>
<option value="JI">Jaber Al Ali</option>
<option value="MB">Mahboula</option>
<option value="MG">Mangaf</option>
<option value="BA">Sabah Al Ahmad</option>
<option value="DU">Al Dubaiya</option>
<option value="MU">Mina Abdullah</option>
<option value="HU">Shuaiba Block 1</option>
<option value="WI">West Industrial Shuaiba</option>
<option value="ZR">Zour</option>
</optgroup>
<optgroup label="Jahra">
<option value="S1">Al Sulaibiya Industrial 1</option>
<option value="S2">Al Sulaibiya Industrial 2</option>
<option value="IA">Amgarah Industrial Area</option>
<option value="JH">Jahra</option>
<option value="NA">Naeem</option>
<option value="NM">Naseem</option>
<option value="OY">Oyoun</option>
<option value="QR">Qasr</option>
<option value="BD">Saad Al Abdullah</option>
<option value="S0">Sulaibiya</option>
<option value="TA">Taima&#39;</option>
<option value="WH">Waha</option>
</optgroup>
</select>'''
        self.assertHTMLEqual(f.render('areas', ''), result)
