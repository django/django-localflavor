# coding: utf-8
from __future__ import unicode_literals

from django.test import SimpleTestCase
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import override

from localflavor.dk.forms import DKMunicipalitySelect, DKPhoneNumberField, DKPostalCodeField


class DKLocalFlavorTests(SimpleTestCase):

    def test_DKPostalCodeField(self):
        error_format = [_("Enter a postal code in the format XXXX.")]
        valid = {
            "4600": "4600",
        }
        invalid = {
            "12": error_format,  # to few digits
            "abcd": error_format,  # illegal characters
            "12345": error_format,  # to many digits
        }
        self.assertFieldOutput(DKPostalCodeField, valid, invalid)

    def test_DKPhoneNumberField(self):
        error_format = [
            _("A phone number must be 8 digits and may have country code")
        ]
        valid = {
            "12345678": "12345678",
            "12 34 56 78": "12 34 56 78",
            "+4512345678": "+4512345678",
            "+45 12345678": "+45 12345678",
            "+45 12 34 56 78": "+45 12 34 56 78",
        }
        invalid = {
            "12": error_format,  # too few digits
            "abcdefgh": error_format,  # illegal characters
            "1234567890": error_format,  # too many digits
            "+4712345678": error_format,  # wrong country code
        }
        self.assertFieldOutput(DKPhoneNumberField, valid, invalid)

    def test_DKMunicipalitySelect(self):
        with override("en"):
            f = DKMunicipalitySelect()
            out = """
<select name="municipalities">
    <optgroup label="Region Hovedstaden">
        <option value="albertslund">Albertslund</option>
        <option value="alleroed">Allerød</option>
        <option value="ballerup">Ballerup</option>
        <option value="bornholm">Bornholm</option>
        <option value="broendby">Brøndby</option>
        <option value="dragoer">Dragør</option>
        <option value="egedal">Egedal</option>
        <option value="fredensborg">Fredensborg</option>
        <option value="frederiksberg">Frederiksberg</option>
        <option value="frederikssund">Frederikssund</option>
        <option value="furesoe">Furesø</option>
        <option value="gentofte">Gentofte</option>
        <option value="gladsaxe">Gladsaxe</option>
        <option value="glostrup">Glostrup</option>
        <option value="gribskov">Gribskov</option>
        <option value="halsnaes">Halsnæs</option>
        <option value="helsingoer">Helsingør</option>
        <option value="herlev">Herlev</option>
        <option value="hilleroed">Hillerød</option>
        <option value="hvidovre">Hvidovre</option>
        <option value="hoeje-taastrup">Høje-Taastrup</option>
        <option value="hoersholm">Hørsholm</option>
        <option value="ishoej">Ishøj</option>
        <option value="koebenhavn">København</option>
        <option value="lyngby-taarbaek">Lyngby-Taarbæk</option>
        <option value="rudersdal">Rudersdal</option>
        <option value="roedovre">Rødovre</option>
        <option value="taarnby">Tårnby</option>
        <option value="vallensbaek">Vallensbæk</option>
    </optgroup>
    <optgroup label="Region Midtjylland">
        <option value="favrskov">Favrskov</option>
        <option value="hedensted">Hedensted</option>
        <option value="herning">Herning</option>
        <option value="holstebro">Holstebro</option>
        <option value="horsens">Horsens</option>
        <option value="ikast-Brande">Ikast-Brande</option>
        <option value="lemvig">Lemvig</option>
        <option value="norddjurs">Norddjurs</option>
        <option value="odder">Odder</option>
        <option value="randers">Randers</option>
        <option value="ringkoebing-skjern">Ringkøbing-Skjern</option>
        <option value="samsoe">Samsø</option>
        <option value="silkeborg">Silkeborg</option>
        <option value="skanderborg">Skanderborg</option>
        <option value="skive">Skive</option>
        <option value="struer">Struer</option>
        <option value="syddjurs">Syddjurs</option>
        <option value="viborg">Viborg</option>
        <option value="aarhus">Aarhus</option>
    </optgroup>
    <optgroup label="Region Nordjylland">
        <option value="broenderslev">Brønderslev</option>
        <option value="frederikshavn">Frederikshavn</option>
        <option value="hjoerring">Hjørring</option>
        <option value="jammerbugt">Jammerbugt</option>
        <option value="laesoe">Læsø</option>
        <option value="mariagerfjord">Mariagerfjord</option>
        <option value="morsoe">Morsø</option>
        <option value="rebild">Rebild</option>
        <option value="thisted">Thisted</option>
        <option value="vesthimmerland">Vesthimmerland</option>
        <option value="aalborg">Aalborg</option>
    </optgroup>
    <optgroup label="Region Sjælland">
        <option value="faxe">Faxe</option>
        <option value="greve">Greve</option>
        <option value="guldborgsund">Guldborgsund</option>
        <option value="holbaek">Holbæk</option>
        <option value="kalundborg">Kalundborg</option>
        <option value="koege" selected="selected">Køge</option>
        <option value="lejre">Lejre</option>
        <option value="lolland">Lolland</option>
        <option value="naestved">Næstved</option>
        <option value="odsherred">Odsherred</option>
        <option value="ringsted">Ringsted</option>
        <option value="roskilde">Roskilde</option>
        <option value="slagelse">Slagelse</option>
        <option value="solroed">Solrød</option>
        <option value="soroe">Sorø</option>
        <option value="stevns">Stevns</option>
        <option value="vordingborg">Vordingborg</option>
    </optgroup>
    <optgroup label="Region Syddanmark">
        <option value="assens">Assens</option>
        <option value="billund">Billund</option>
        <option value="esbjerg">Esbjerg</option>
        <option value="fanoe">Fanø</option>
        <option value="fredericia">Fredericia</option>
        <option value="faaborg-Midtfyn">Faaborg-Midtfyn</option>
        <option value="haderslev">Haderslev</option>
        <option value="kerteminde">Kerteminde</option>
        <option value="kolding">Kolding</option>
        <option value="langeland">Langeland</option>
        <option value="middelfart">Middelfart</option>
        <option value="nordfyn">Nordfyn</option>
        <option value="nyborg">Nyborg</option>
        <option value="odense">Odense</option>
        <option value="svendborg">Svendborg</option>
        <option value="soenderborg">Sønderborg</option>
        <option value="toender">Tønder</option>
        <option value="varde">Varde</option>
        <option value="vejen">Vejen</option>
        <option value="vejle">Vejle</option>
        <option value="aeroe">Ærø</option>
        <option value="aabenraa">Aabenraa</option>
    </optgroup>
</select>"""

        self.assertHTMLEqual(f.render("municipalities", "koege"), out)
