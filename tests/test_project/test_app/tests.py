from django.core.management import call_command
from django.test import TestCase

from localflavor.management.commands.run_localflavor_datamigrations import update_field_values
from localflavor.mx.models import MXStateField

from .models import MyModel


class DataMigrationTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.models = [
            MyModel.objects.create(state='DIF')
            for _ in range(10)
        ]

    def test_management_command(self):
        call_command('run_localflavor_datamigrations')
        self.assertEqual(MyModel.objects.count(), 10)
        self.assertEqual(MyModel.objects.filter(state='DIF').count(), 0)

    def test_update_field_values(self):
        update_field_values(MXStateField, 'DIF', 'Hello')
        self.assertEqual(MyModel.objects.count(), 10)
        self.assertEqual(MyModel.objects.filter(state='DIF').count(), 0)
        self.assertEqual(MyModel.objects.filter(state='Hello').count(), 10)
