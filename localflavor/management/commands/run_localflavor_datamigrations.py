from django.apps import registry
from django.core.management import BaseCommand
from django.db.transaction import atomic

from localflavor.mx.models import MXStateField


def find_fields(field_cls):
    return (
        (model, field.name)
        for model in registry.apps.get_models()
        for field in model._meta.get_fields()
        if isinstance(field, field_cls)
    )


def update_field_values(field_cls, from_, to, stdout=None):
    for model, field_name in find_fields(field_cls):

        if stdout:
            stdout.write(
                "Updating field {0} on model {1} from {2} to {3}".format(
                    model.__class__.__name__, field_name, from_, to
                )
            )

        filter_kwargs = {field_name: from_}
        update_kwargs = {field_name: to}
        count = model.objects.filter(**filter_kwargs).update(**update_kwargs)

        if stdout:
            stdout.write(" - Updated {0} rows".format(count))


class Command(BaseCommand):
    @atomic
    def handle(self, *args, **options):
        update_field_values(MXStateField, from_='DIF', to='CDMX', stdout=self.stdout)
