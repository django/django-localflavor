# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import SimpleTestCase

from localflavor.it.forms import (ITPhoneNumberField, ITRegionProvinceSelect, ITRegionSelect,
                                  ITSocialSecurityNumberField, ITVatNumberField, ITZipCodeField)


class ITLocalFlavorTests(SimpleTestCase):
    def test_ITRegionSelect(self):
        f = ITRegionSelect()
        out = '''<select name="regions">
<option value="ABR">Abruzzo</option>
<option value="BAS">Basilicata</option>
<option value="CAL">Calabria</option>
<option value="CAM">Campania</option>
<option value="EMR">Emilia-Romagna</option>
<option value="FVG">Friuli-Venezia Giulia</option>
<option value="LAZ">Lazio</option>
<option value="LIG">Liguria</option>
<option value="LOM">Lombardia</option>
<option value="MAR">Marche</option>
<option value="MOL">Molise</option>
<option value="PMN" selected="selected">Piemonte</option>
<option value="PUG">Puglia</option>
<option value="SAR">Sardegna</option>
<option value="SIC">Sicilia</option>
<option value="TOS">Toscana</option>
<option value="TAA">Trentino-Alto Adige</option>
<option value="UMB">Umbria</option>
<option value="VAO">Valle d\u2019Aosta</option>
<option value="VEN">Veneto</option>
</select>'''
        self.assertHTMLEqual(f.render('regions', 'PMN'), out)

    def test_ITRegionProvinceSelect(self):
        f = ITRegionProvinceSelect()
        out = '''<select name="region_provinces">
<optgroup label="Abruzzo">
<option value="CH">Chieti</option>
<option value="AQ">L\u2019Aquila</option>
<option value="PE" selected="selected">Pescara</option>
<option value="TE">Teramo</option>
</optgroup>
<optgroup label="Basilicata">
<option value="MT">Matera</option>
<option value="PZ">Potenza</option>
</optgroup>
<optgroup label="Calabria">
<option value="CZ">Catanzaro</option>
<option value="CS">Cosenza</option>
<option value="KR">Crotone</option>
<option value="RC">Reggio Calabria</option>
<option value="VV">Vibo Valentia</option>
</optgroup>
<optgroup label="Campania">
<option value="AV">Avellino</option>
<option value="BN">Benevento</option>
<option value="CE">Caserta</option>
<option value="NA">Napoli</option>
<option value="SA">Salerno</option>
</optgroup>
<optgroup label="Emilia-Romagna">
<option value="BO">Bologna</option>
<option value="FE">Ferrara</option>
<option value="FC">Forl\xec-Cesena</option>
<option value="MO">Modena</option>
<option value="PR">Parma</option>
<option value="PC">Piacenza</option>
<option value="RA">Ravenna</option>
<option value="RE">Reggio Emilia</option>
<option value="RN">Rimini</option>
</optgroup>
<optgroup label="Friuli-Venezia Giulia">
<option value="GO">Gorizia</option>
<option value="PN">Pordenone</option>
<option value="TS">Trieste</option>
<option value="UD">Udine</option>
</optgroup>
<optgroup label="Lazio">
<option value="FR">Frosinone</option>
<option value="LT">Latina</option>
<option value="RI">Rieti</option>
<option value="RM">Roma</option>
<option value="VT">Viterbo</option>
</optgroup>
<optgroup label="Liguria">
<option value="GE">Genova</option>
<option value="IM">Imperia</option>
<option value="SP">La Spezia</option>
<option value="SV">Savona</option>
</optgroup>
<optgroup label="Lombardia">
<option value="BG">Bergamo</option>
<option value="BS">Brescia</option>
<option value="CO">Como</option>
<option value="CR">Cremona</option>
<option value="LC">Lecco</option>
<option value="LO">Lodi</option>
<option value="MN">Mantova</option>
<option value="MI">Milano</option>
<option value="MB">Monza e Brianza</option>
<option value="PV">Pavia</option>
<option value="SO">Sondrio</option>
<option value="VA">Varese</option>
</optgroup>
<optgroup label="Marche">
<option value="AN">Ancona</option>
<option value="AP">Ascoli Piceno</option>
<option value="FM">Fermo</option>
<option value="MC">Macerata</option>
<option value="PU">Pesaro e Urbino</option>
</optgroup>
<optgroup label="Molise">
<option value="CB">Campobasso</option>
<option value="IS">Isernia</option>
</optgroup>
<optgroup label="Piemonte">
<option value="AL">Alessandria</option>
<option value="AT">Asti</option>
<option value="BI">Biella</option>
<option value="CN">Cuneo</option>
<option value="NO">Novara</option>
<option value="TO">Torino</option>
<option value="VB">Verbano Cusio Ossola</option>
<option value="VC">Vercelli</option>
</optgroup>
<optgroup label="Puglia">
<option value="BA">Bari</option>
<option value="BT">Barletta-Andria-Trani</option>
<option value="BR">Brindisi</option>
<option value="FG">Foggia</option>
<option value="LE">Lecce</option>
<option value="TA">Taranto</option>
</optgroup>
<optgroup label="Sardegna">
<option value="CA">Cagliari</option>
<option value="CI">Carbonia-Iglesias</option>
<option value="VS">Medio Campidano</option>
<option value="NU">Nuoro</option>
<option value="OG">Ogliastra</option>
<option value="OT">Olbia-Tempio</option>
<option value="OR">Oristano</option>
<option value="SS">Sassari</option>
</optgroup>
<optgroup label="Sicilia">
<option value="AG">Agrigento</option>
<option value="CL">Caltanissetta</option>
<option value="CT">Catania</option>
<option value="EN">Enna</option>
<option value="ME">Messina</option>
<option value="PA">Palermo</option>
<option value="RG">Ragusa</option>
<option value="SR">Siracusa</option>
<option value="TP">Trapani</option>
</optgroup>
<optgroup label="Toscana">
<option value="AR">Arezzo</option>
<option value="FI">Firenze</option>
<option value="GR">Grosseto</option>
<option value="LI">Livorno</option>
<option value="LU">Lucca</option>
<option value="MS">Massa-Carrara</option>
<option value="PI">Pisa</option>
<option value="PT">Pistoia</option>
<option value="PO">Prato</option>
<option value="SI">Siena</option>
</optgroup>
<optgroup label="Trentino-Alto Adige">
<option value="BZ">Bolzano/Bozen</option>
<option value="TN">Trento</option>
</optgroup>
<optgroup label="Umbria">
<option value="PG">Perugia</option>
<option value="TR">Terni</option>
</optgroup>
<optgroup label="Valle d\u2019Aosta">
<option value="AO">Aosta</option>
</optgroup>
<optgroup label="Veneto">
<option value="BL">Belluno</option>
<option value="PD">Padova</option>
<option value="RO">Rovigo</option>
<option value="TV">Treviso</option>
<option value="VE">Venezia</option>
<option value="VR">Verona</option>
<option value="VI">Vicenza</option>
</optgroup>
</select>'''
        self.assertHTMLEqual(f.render('region_provinces', 'PE'), out)

    def test_ITZipCodeField(self):
        error_invalid = ['Enter a valid zip code.']
        valid = {
            '00100': '00100',
        }
        invalid = {
            ' 00100': error_invalid,
        }
        self.assertFieldOutput(ITZipCodeField, valid, invalid)

    def test_ITSocialSecurityNumberField(self):
        error_invalid = ['Enter a valid Tax code.']
        valid = {
            'LVSGDU99T71H501L': 'LVSGDU99T71H501L',
            'LBRRME11A01L736W': 'LBRRME11A01L736W',
            'lbrrme11a01l736w': 'LBRRME11A01L736W',
            'LBR RME 11A01 L736W': 'LBRRME11A01L736W',
        }
        invalid = {
            'LBRRME11A01L736A': error_invalid,
            '%BRRME11A01L736W': error_invalid,
        }
        self.assertFieldOutput(ITSocialSecurityNumberField, valid, invalid)

    def test_ITSocialSecurityNumberField_for_entities(self):
        error_invalid = ['Enter a valid Tax code.']
        valid = {
            '07973780013': '07973780013',
            '7973780013': '07973780013',
            7973780013: '07973780013',
        }
        invalid = {
            '07973780014': error_invalid,
            'A7973780013': error_invalid,
        }
        self.assertFieldOutput(ITSocialSecurityNumberField, valid, invalid)

    def test_ITVatNumberField(self):
        error_invalid = ['Enter a valid VAT number.']
        valid = {
            '07973780013': '07973780013',
            '7973780013': '07973780013',
            7973780013: '07973780013',
        }
        invalid = {
            '07973780014': error_invalid,
            'A7973780013': error_invalid,
        }
        self.assertFieldOutput(ITVatNumberField, valid, invalid)

    def test_ITPhoneNumberField(self):
        error_format = ['Enter a valid Italian phone number.']
        valid = {
            '+39 347 1234567': '347 1234567',
            '39 347 123 4567': '347 1234567',
            '347-1234567': '347 1234567',
            '3471234567': '347 1234567',
            '+39 347 12345678': '347 12345678',
            '39 347 123 45678': '347 12345678',
            '347-12345678': '347 12345678',
            '34712345678': '347 12345678',
            '+39 347 123456': '347 123456',
            '39 347 123 456': '347 123456',
            '347-123456': '347 123456',
            '347123456': '347 123456',
            '+39 0861 12345678': '0861 12345678',
            '39 0861 1234 5678': '0861 12345678',
            '0861-12345678': '0861 12345678',
            '0861 12345': '0861 12345',
        }
        invalid = {
            '+44 347 1234567': error_format,
            '14471234567': error_format,
            '0861 123456789': error_format,
            '08661234567890': error_format,
        }
        self.assertFieldOutput(ITPhoneNumberField, valid, invalid)
