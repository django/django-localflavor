from django.test import SimpleTestCase

from localflavor.ie.forms import EircodeField, IECountySelect


class IELocalFlavorTests(SimpleTestCase):
    def test_IECountySelect(self):
        f = IECountySelect()
        out = """<select name="counties">
<option value="carlow">Carlow</option>
<option value="cavan">Cavan</option>
<option value="clare">Clare</option>
<option value="cork">Cork</option>
<option value="donegal">Donegal</option>
<option value="dublin" selected="selected">Dublin</option>
<option value="galway">Galway</option>
<option value="kerry">Kerry</option>
<option value="kildare">Kildare</option>
<option value="kilkenny">Kilkenny</option>
<option value="laois">Laois</option>
<option value="leitrim">Leitrim</option>
<option value="limerick">Limerick</option>
<option value="longford">Longford</option>
<option value="louth">Louth</option>
<option value="mayo">Mayo</option>
<option value="meath">Meath</option>
<option value="monaghan">Monaghan</option>
<option value="offaly">Offaly</option>
<option value="roscommon">Roscommon</option>
<option value="sligo">Sligo</option>
<option value="tipperary">Tipperary</option>
<option value="waterford">Waterford</option>
<option value="westmeath">Westmeath</option>
<option value="wexford">Wexford</option>
<option value="wicklow">Wicklow</option>
</select>"""
        self.assertHTMLEqual(f.render("counties", "dublin"), out)

    def test_EircodeField(self):
        error_invalid = ["Enter a valid Eircode."]
        valid = {
            "A65 F4E2": "A65F4E2",
            "a65f4e2": "A65F4E2",
            "D6w123A": "D6W123A",
            " f28 e50f ": "F28E50F",
        }
        invalid = {
            "A65F 4EI": error_invalid,
            "A65  F4EI": error_invalid,
            "A 65 F4EI": error_invalid,
            "D4W 1234": error_invalid,
            "Z99ABCF": error_invalid,
            "a65 123b": error_invalid,
            " b0gUS": error_invalid,
        }
        self.assertFieldOutput(EircodeField, valid, invalid)

    def test_EircodeField_error_message_can_be_overridden(self):
        valid = {}
        invalid = {"1NV 4L1D": ["Enter a bloody eircode!"]}
        kwargs = {"error_messages": {"invalid": "Enter a bloody eircode!"}}
        self.assertFieldOutput(EircodeField, valid, invalid, field_kwargs=kwargs)

    def test_EircodeField_formatting(self):
        field = EircodeField()
        self.assertEqual(field.prepare_value("A65 F4E2"),  "A65 F4E2")
        self.assertEqual(field.prepare_value("a65f4e2"), "A65 F4E2",)
        self.assertEqual(field.prepare_value("D6w123A"), "D6W 123A")
        self.assertEqual(field.prepare_value(" f28 e50f "), "F28 E50F")
        self.assertEqual(field.prepare_value(None), '')
        self.assertEqual(field.prepare_value(''), '')
