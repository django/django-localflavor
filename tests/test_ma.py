from django.test import SimpleTestCase

from localflavor.ma.forms import MAPostalCodeField, MAProvinceField, MAProvinceSelect, MARegionField, MARegionSelect

PROVINCE_SELECT_OUTPUT = '''
    <select name="province">
        <option value="01">01 - Al Hoceima</option>
        <option value="02">02 - Larache</option>
        <option value="03">03 - M’Diq - Fnideq</option>
        <option value="04">04 - Tetouan</option>
        <option value="05">05 - Chefchaouene</option>
        <option value="06">06 - Tanger - Assilah</option>
        <option value="07">07 - Fahs - Anjra</option>
        <option value="08">08 - Ouezzane</option>
        <option value="09">09 - Driouch</option>
        <option value="10">10 - Nador</option>
        <option value="11">11 - Berkan</option>
        <option value="12">12 - Taourirt</option>
        <option value="13">13 - Jerada</option>
        <option value="14">14 - Guercif</option>
        <option value="15">15 - Feguig</option>
        <option value="16">16 - Oujda - Angad</option>
        <option value="17">17 - El Hajeb</option>
        <option value="18">18 - Ifrane</option>
        <option value="19">19 - Boulemane</option>
        <option value="20">20 - Taza</option>
        <option value="21">21 - Taounate</option>
        <option value="22">22 - Sefrou</option>
        <option value="23">23 - Fès</option>
        <option value="24">24 - Meknès</option>
        <option value="25">25 - Moulay Yacoub</option>
        <option value="26">26 - Khémisset</option>
        <option value="27" selected="selected">27 - Rabat</option>
        <option value="28">28 - Skhirate - Temara</option>
        <option value="29">29 - Kénitra</option>
        <option value="30">30 - Salé</option>
        <option value="31">31 - Sidi Slimane</option>
        <option value="32">32 - Sidi Kacem</option>
        <option value="33">33 - Casablanca</option>
        <option value="34">34 - Mohamedia</option>
        <option value="35">35 - Nouaceur</option>
        <option value="36">36 - Mediouna</option>
        <option value="37">37 - Benslimane</option>
        <option value="38">38 - Berrachid</option>
        <option value="39">39 - El Jadida</option>
        <option value="40">40 - Sidi Bennour</option>
        <option value="41">41 - Settat</option>
        <option value="42">42 - Azilal</option>
        <option value="43">43 - Fquih Ben Saleh</option>
        <option value="44">44 - Beni Mellal</option>
        <option value="45">45 - Khouribga</option>
        <option value="46">46 - Khénifra</option>
        <option value="47">47 - Safi</option>
        <option value="48">48 - Al Haouz</option>
        <option value="49">49 - Rhamna</option>
        <option value="50">50 - Essaouira</option>
        <option value="51">51 - Youssoufia</option>
        <option value="52">52 - Marrakech</option>
        <option value="53">53 - Chichaoua</option>
        <option value="54">54 - El Kelaa Des Sraghna</option>
        <option value="55">55 - Agadir - Idda Outanane</option>
        <option value="56">56 - Inezgane - Ait Melloul</option>
        <option value="57">57 - Chtouka - Ait Baha</option>
        <option value="58">58 - Tiznit</option>
        <option value="59">59 - Tata</option>
        <option value="60">60 - Taroudant</option>
        <option value="61">61 - Errachidia</option>
        <option value="62">62 - Tinghir</option>
        <option value="63">63 - Zagoura</option>
        <option value="64">64 - Midelt</option>
        <option value="65">65 - Ouarzazate</option>
        <option value="66">66 - Es -Semara</option>
        <option value="67">67 - Laayoune</option>
        <option value="68">68 - Boujdour</option>
        <option value="69">69 - Terfaya</option>
        <option value="70">70 - Aousserd</option>
        <option value="71">71 - Oued Eddahab</option>
        <option value="72">72 - Assa - Zag</option>
        <option value="73">73 - Sidi Ifni</option>
        <option value="74">74 - Tantan</option>
        <option value="75">75 - Guelmim</option>
    </select>
'''

REGION_SELECT_OUTPUT = '''
    <select name="region">
        <option value="01">01 - Tanger-Tétouan-Al Hoceïma</option>
        <option value="02">02 - L’Oriental</option>
        <option value="03">03 - Fès-Meknès</option>
        <option value="04" selected="selected">04 - Rabat-Salé-Kénitra</option>
        <option value="05">05 - Béni Mellal-Khénifra</option>
        <option value="06">06 - Casablanca-Settat</option>
        <option value="07">07 - Marrakech-Safi</option>
        <option value="08">08 - Drâa-Tafilalet</option>
        <option value="09">09 - Souss-Massa</option>
        <option value="10">10 - Guelmim-Oued Noun</option>
        <option value="11">11 - Laâyoune-Sakia El Hamra</option>
        <option value="12">12 - Dakhla-Oued Ed Dahab</option>
    </select>
'''

class MALocalFlavorTests(SimpleTestCase):
    def test_MAPostalCodeField(self):
        error_format = ['Enter a postal code in the format XXXXX.']
        valid = {
            '11030': '11030',
            '11000': '11000',
        }
        invalid = {
            '1E510': error_format,
            '110002': ['Ensure this value has at most '
                       '5 characters (it has 6).'] + error_format,
        }
        self.assertFieldOutput(MAPostalCodeField, valid, invalid)

    def test_MAProvinceField(self):
        f = MAProvinceField()
        self.assertHTMLEqual(f.widget.render('province', '27'), PROVINCE_SELECT_OUTPUT)

    def test_MARegionfield(self):
        f = MARegionField()
        self.assertHTMLEqual(f.widget.render('region', '04'), REGION_SELECT_OUTPUT)

    def test_MAProvinceSelect(self):
        f = MAProvinceSelect()
        self.assertHTMLEqual(f.render('province', '27'), PROVINCE_SELECT_OUTPUT)

    def test_MARegionSelect(self):
        f = MARegionSelect()
        self.assertHTMLEqual(f.render('region', '04'), REGION_SELECT_OUTPUT)
