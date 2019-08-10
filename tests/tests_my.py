from django.test import SimpleTestCase

from localflavor.my.forms import MyKadField


class MYLocalFlavorTests(SimpleTestCase):

    def test_MyKadField(self):
        error_format = ['Invalid MyKad number.']
        valid = {
            '900127-01-1234': '900127-01-1234',
            '920328-04-4567': '920328-04-4567',
            '940731-07-7891': '940731-07-7891',
            '941031-10-1011': '941031-10-1011',
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
        self.assertFieldOutput(MyKadField, valid, invalid)

        def test_MyKadField_without_hyphen(self):
            error_format = ['Invalid MyKad number.']
            valid = {
                '900127011234': '900127011234',
                '920328044567': '920328044567',
                '940731077891': '940731077891',
                '941031101011': '941031101011',
            }
            invalid = {
                '940827001234': error_format,
                '940827171234': error_format,
                '940827181234': error_format,
                '940827191234': error_format,
                '940827201234': error_format,
                '940827691234': error_format,
                '940827701234': error_format,
                '940827731234': error_format,
                '940827801234': error_format,
                '940827811234': error_format,
                '940827941234': error_format,
                '940827951234': error_format,
                '940827961234': error_format,
                '940827971234': error_format,
            }
            self.assertFieldOutput(
                MyKadField, valid, invalid, field_args=None,
                field_kwargs={'hyphen': False}
            )
