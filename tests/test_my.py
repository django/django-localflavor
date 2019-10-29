from django.test import SimpleTestCase

from localflavor.my.forms import MyKadFormField


class MYLocalFlavorTests(SimpleTestCase):

    def test_MyKadFormField(self):
        error_format = ['Invalid MyKad number.']
        valid = {
            '900127-01-1234': '900127011234',
            '920328-04-4567': '920328044567',
            '940731-07-7891': '940731077891',
            '941031-10-1011': '941031101011',
            '910127011235': '910127011235',
            '930328044577': '930328044577',
            '940731077891': '940731077891',
        }
        invalid = {
            '940827-00-1234': error_format,
            '940827-17-1234': error_format,
            '940827-18-1234': error_format,
            '940827-19-1234': error_format,
            '940827-20-1234': error_format,
            '940827-69-1234': error_format,
            '940827-70-1234': error_format,
            '940827-73-1234': error_format,
            '940827-80-1234': error_format,
            '940827-81-1234': error_format,
            '940827-94-1234': error_format,
            '940827-95-1234': error_format,
            '940827-96-1234': error_format,
            '940827-97-1234': error_format,
        }
        self.assertFieldOutput(MyKadFormField, valid, invalid)

    def test_my_kad_form_field_formatting(self):
        form_field = MyKadFormField()

        self.assertIsNone(form_field.prepare_value(None))
        self.assertEqual(
            form_field.prepare_value('940731077891'), '940731-07-7891'
        )

        self.assertEqual(form_field.to_python('940731077891'), '940731077891')
        self.assertEqual(form_field.to_python('940731-07-7891'), '940731077891')
