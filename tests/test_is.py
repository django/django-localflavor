from django.test import SimpleTestCase

from localflavor.is_.forms import ISIdNumberField, ISPostalCodeSelect


class ISLocalFlavorTests(SimpleTestCase):
    def test_ISPostalCodeSelect(self):
        f = ISPostalCodeSelect()
        out = '''<select name="foo">
<option value="101">101 Reykjavík</option>
<option value="102">102 Reykjavík</option>
<option value="103">103 Reykjavík</option>
<option value="104">104 Reykjavík</option>
<option value="105">105 Reykjavík</option>
<option value="107">107 Reykjavík</option>
<option value="108">108 Reykjavík</option>
<option value="109">109 Reykjavík</option>
<option value="110">110 Reykjavík</option>
<option value="111">111 Reykjavík</option>
<option value="112">112 Reykjavík</option>
<option value="113">113 Reykjavík</option>
<option value="116">116 Reykjavík</option>
<option value="121">121 Reykjavík</option>
<option value="123">123 Reykjavík</option>
<option value="124">124 Reykjavík</option>
<option value="125">125 Reykjavík</option>
<option value="127">127 Reykjavík</option>
<option value="128">128 Reykjavík</option>
<option value="129">129 Reykjavík</option>
<option value="130">130 Reykjavík</option>
<option value="132">132 Reykjavík</option>
<option value="161">161 Reykjavík</option>
<option value="162">162 Reykjavík - Dreifbýli</option>
<option value="170">170 Seltjarnarnesi</option>
<option value="172">172 Seltjarnarnesi</option>
<option value="190">190 Vogum</option>
<option value="191">191 Vogum</option>
<option value="200">200 Kópavogi</option>
<option value="201">201 Kópavogi</option>
<option value="202">202 Kópavogi</option>
<option value="203">203 Kópavogi</option>
<option value="206">206 Kópavogur</option>
<option value="210">210 Garðabæ</option>
<option value="212">212 Garðabæ</option>
<option value="220">220 Hafnarfirði</option>
<option value="221">221 Hafnarfirði</option>
<option value="222">222 Hafnarfirði</option>
<option value="225">225 Garðabæ</option>
<option value="230">230 Reykjanesbæ</option>
<option value="232">232 Reykjanesbæ</option>
<option value="233">233 Reykjanesbæ</option>
<option value="235">235 Keflavíkurflugvöllur</option>
<option value="240">240 Grindavík</option>
<option value="241">241 Grindavík</option>
<option value="245">245 Suðurnesjabæ</option>
<option value="246">246 Suðurnesjabæ</option>
<option value="250">250 Suðurnesjabæ</option>
<option value="251">251 Suðurnesjabæ</option>
<option value="260">260 Reykjanesbæ</option>
<option value="262">262 Reykjanesbæ</option>
<option value="270">270 Mosfellsbæ</option>
<option value="271">271 Mosfellsbæ</option>
<option value="276">276 Mosfellsbæ</option>
<option value="300">300 Akranesi</option>
<option value="301">301 Akranesi</option>
<option value="302">302 Akranesi</option>
<option value="310">310 Borgarnesi</option>
<option value="311">311 Borgarnesi</option>
<option value="320">320 Reykholt í Borgarfirði</option>
<option value="340">340 Stykkishólmi</option>
<option value="341">341 Stykkishólmi</option>
<option value="342">342 Stykkishólmur</option>
<option value="345">345 Flatey á Breiðafirði</option>
<option value="350">350 Grundarfirði</option>
<option value="351">351 Grundarfirði</option>
<option value="355">355 Ólafsvík</option>
<option value="356">356 Snæfellsbæ</option>
<option value="360">360 Hellissandi</option>
<option value="370">370 Búðardal</option>
<option value="371">371 Búðardal</option>
<option value="380">380 Reykhólahreppi</option>
<option value="381">381 Reykhólahreppi</option>
<option value="400">400 Ísafirði</option>
<option value="401">401 Ísafirði</option>
<option value="410">410 Hnífsdal</option>
<option value="415">415 Bolungarvík</option>
<option value="416">416 Bolungarvík</option>
<option value="420">420 Súðavík</option>
<option value="421">421 Súðavík</option>
<option value="425">425 Flateyri</option>
<option value="426">426 Flateyri</option>
<option value="430">430 Suðureyri</option>
<option value="431">431 Suðureyri</option>
<option value="450">450 Patreksfirði</option>
<option value="451">451 Patreksfirði</option>
<option value="460">460 Tálknafirði</option>
<option value="461">461 Tálknafirði</option>
<option value="465">465 Bíldudal</option>
<option value="466">466 Bíldudal</option>
<option value="470">470 Þingeyri</option>
<option value="471">471 Þingeyri</option>
<option value="500">500 Stað</option>
<option value="510">510 Hólmavík</option>
<option value="511">511 Hólmavík</option>
<option value="512">512 Hólmavík</option>
<option value="520">520 Drangsnesi</option>
<option value="524">524 Árneshreppi</option>
<option value="530">530 Hvammstanga</option>
<option value="531">531 Hvammstanga</option>
<option value="540">540 Blönduósi</option>
<option value="541">541 Blönduósi</option>
<option value="545">545 Skagaströnd</option>
<option value="546">546 Skagaströnd</option>
<option value="550">550 Sauðárkróki</option>
<option value="551">551 Sauðárkróki</option>
<option value="560">560 Varmahlíð</option>
<option value="561">561 Varmahlíð</option>
<option value="565">565 Hofsós</option>
<option value="566">566 Hofsós</option>
<option value="570">570 Fljótum</option>
<option value="580">580 Siglufirði</option>
<option value="581">581 Siglufirði</option>
<option value="600">600 Akureyri</option>
<option value="601">601 Akureyri</option>
<option value="602">602 Akureyri</option>
<option value="603">603 Akureyri</option>
<option value="604">604 Akureyri</option>
<option value="605">605 Akureyri</option>
<option value="606">606 Akureyri</option>
<option value="607">607 Akureyri</option>
<option value="610">610 Grenivík</option>
<option value="611">611 Grímsey</option>
<option value="616">616 Grenivík</option>
<option value="620">620 Dalvík</option>
<option value="621">621 Dalvík</option>
<option value="625">625 Ólafsfirði</option>
<option value="626">626 Ólafsfirði</option>
<option value="630">630 Hrísey</option>
<option value="640">640 Húsavík</option>
<option value="641">641 Húsavík</option>
<option value="645">645 Fosshólli</option>
<option value="650">650 Laugum</option>
<option value="660">660 Mývatni</option>
<option value="670">670 Kópaskeri</option>
<option value="671">671 Kópaskeri</option>
<option value="675">675 Raufarhöfn</option>
<option value="676">676 Raufarhöfn</option>
<option value="680">680 Þórshöfn</option>
<option value="681">681 Þórshöfn</option>
<option value="685">685 Bakkafirði</option>
<option value="686">686 Bakkafirði</option>
<option value="690">690 Vopnafirði</option>
<option value="691">691 Vopnafirði</option>
<option value="700">700 Egilsstöðum</option>
<option value="701">701 Egilsstöðum</option>
<option value="710">710 Seyðisfirði</option>
<option value="711">711 Seyðisfirði</option>
<option value="715">715 Mjóafirði</option>
<option value="720">720 Borgarfirði (eystri)</option>
<option value="721">721 Borgarfirði (eystri)</option>
<option value="730">730 Reyðarfirði</option>
<option value="731">731 Reyðarfirði</option>
<option value="735">735 Eskifirði</option>
<option value="736">736 Eskifirði</option>
<option value="740">740 Neskaupstað</option>
<option value="741">741 Neskaupsstað</option>
<option value="750">750 Fáskrúðsfirði</option>
<option value="751">751 Fáskrúðsfirði</option>
<option value="755">755 Stöðvarfirði</option>
<option value="756">756 Stöðvarfirði</option>
<option value="760">760 Breiðdalsvík</option>
<option value="761">761 Breiðdalsvík</option>
<option value="765">765 Djúpavogi</option>
<option value="766">766 Djúpavogi</option>
<option value="780">780 Höfn í Hornafirði</option>
<option value="781">781 Höfn í Hornafirði</option>
<option value="785">785 Öræfum</option>
<option value="800">800 Selfossi</option>
<option value="801">801 Selfossi</option>
<option value="802">802 Selfossi</option>
<option value="803">803 Selfoss</option>
<option value="804">804 Selfoss</option>
<option value="805">805 Selfoss</option>
<option value="806">806 Selfoss</option>
<option value="810">810 Hveragerði</option>
<option value="815">815 Þorlákshöfn</option>
<option value="816">816 Ölfus</option>
<option value="820">820 Eyrarbakka</option>
<option value="825">825 Stokkseyri</option>
<option value="840">840 Laugarvatni</option>
<option value="845">845 Flúðum</option>
<option value="846">846 Flúðum</option>
<option value="850">850 Hellu</option>
<option value="851">851 Hellu</option>
<option value="860">860 Hvolsvelli</option>
<option value="861">861 Hvolsvelli</option>
<option value="870">870 Vík</option>
<option value="871">871 Vík</option>
<option value="880">880 Kirkjubæjarklaustri</option>
<option value="881">881 Kirkjubæjarklaustri</option>
<option value="900">900 Vestmannaeyjum</option>
<option value="902">902 Vestmannaeyjum</option>
</select>'''
        self.assertHTMLEqual(f.render('foo', 'bar'), out)

    def test_ISIdNumberField(self):
        error_atleast = ['Ensure this value has at least 10 characters (it has 9).']
        error_invalid = ['Enter a valid Icelandic identification number. The format is XXXXXX-XXXX.']
        error_atmost = ['Ensure this value has at most 11 characters (it has 12).']
        error_notvalid = ['The Icelandic identification number is not valid.']
        valid = {
            '2308803449': '230880-3449',
            '230880-3449': '230880-3449',
            '230880 3449': '230880-3449',
            '2308803440': '230880-3440',
        }
        invalid = {
            '230880343': error_atleast + error_invalid,
            '230880343234': error_atmost + error_invalid,
            'abcdefghijk': error_invalid,
            '2308803439': error_notvalid,

        }
        self.assertFieldOutput(ISIdNumberField, valid, invalid)
