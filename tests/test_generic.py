from __future__ import unicode_literals

from django.test import SimpleTestCase
from django.utils import formats

from localflavor.generic.forms import (DateField, DateTimeField,
                                       SplitDateTimeField)


class DateTimeFieldTestCase(SimpleTestCase):

    default_date_input_formats = (
        '%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y', '%b %d %Y', '%b %d, %Y',
        '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y',
        '%d %B, %Y',
    )

    default_datetime_input_formats = (
        '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%d/%m/%Y %H:%M:%S',
        '%d/%m/%Y %H:%M', '%d/%m/%Y', '%d/%m/%y %H:%M:%S', '%d/%m/%y %H:%M',
        '%d/%m/%y',
    )

    def assertInputFormats(self, field, formats):
        self.assertSequenceEqual(field.input_formats, formats)


class DateFieldTests(DateTimeFieldTestCase):

    def setUp(self):
        self.default_input_formats = self.default_date_input_formats

    def test_init_no_input_formats(self):
        field = DateField()
        self.assertInputFormats(field, self.default_input_formats)

    def test_init_empty_input_formats(self):
        field = DateField(input_formats=())
        self.assertInputFormats(field, self.default_input_formats)

    def test_init_custom_input_formats(self):
        input_formats = ('%m/%d/%Y', '%m/%d/%y')
        field = DateField(input_formats=input_formats)
        self.assertInputFormats(field, input_formats)


class DateTimeFieldTests(DateTimeFieldTestCase):

    def setUp(self):
        self.default_input_formats = self.default_datetime_input_formats

    def test_init_no_input_formats(self):
        field = DateTimeField()
        self.assertInputFormats(field, self.default_input_formats)

    def test_init_empty_input_formats(self):
        field = DateTimeField(input_formats=())
        self.assertInputFormats(field, self.default_input_formats)

    def test_init_custom_input_formats(self):
        input_formats = ('%m/%d/%Y %H:%M', '%m/%d/%y %H:%M')
        field = DateTimeField(input_formats=input_formats)
        self.assertInputFormats(field, input_formats)


class SplitDateTimeFieldTests(DateTimeFieldTestCase):

    default_time_input_formats = formats.get_format_lazy('TIME_INPUT_FORMATS')

    def test_init_no_input_formats(self):
        field = SplitDateTimeField()
        date_field, time_field = field.fields
        self.assertInputFormats(date_field, self.default_date_input_formats)
        self.assertInputFormats(time_field, self.default_time_input_formats)

    def test_init_empty_input_formats(self):
        field = SplitDateTimeField(input_date_formats=(),
                                   input_time_formats=())
        date_field, time_field = field.fields
        self.assertInputFormats(date_field, self.default_date_input_formats)
        self.assertInputFormats(time_field, ())

    def test_init_custom_input_formats(self):
        date_input_formats = ('%m/%d/%Y', '%m/%d/%y')
        time_input_formats = ('%H:%M', '%H:%M:%S')
        field = SplitDateTimeField(input_date_formats=date_input_formats,
                                   input_time_formats=time_input_formats)
        date_field, time_field = field.fields
        self.assertInputFormats(date_field, date_input_formats)
        self.assertInputFormats(time_field, time_input_formats)
