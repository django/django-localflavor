import importlib
import pkgutil

from django import forms
from django.db import models
from django.test.testcases import TestCase

import localflavor


class GeneralTests(TestCase):

    @staticmethod
    def _find_localflavor_subclasses(base_class):
        classes = []
        for importer, modname, ispkg in pkgutil.walk_packages(path=localflavor.__path__, prefix=localflavor.__name__ + '.',
                                                              onerror=lambda x: None):
            if ispkg:
                continue
            module = importlib.import_module(modname)
            for f in dir(module):
                if f.startswith('_'):
                    continue
                item = getattr(module, f)
                if localflavor.__name__ in str(item):
                    try:
                        if issubclass(item, base_class):
                            classes.append(item)
                    except TypeError:
                        # item is not a class.
                        pass
        return classes

    def test_model_field_deconstruct_methods_with_default_options(self):
        # This test can only check the choices and max_length options. Specific tests are required for model fields
        # with options that users can set. See to the IBAN tests for an example.

        model_classes = self._find_localflavor_subclasses(models.Field)
        self.assertTrue(len(model_classes) > 0, 'No localflavor models.Field classes were found.')

        for cls in model_classes:
            test_instance = cls()
            name, path, args, kwargs = test_instance.deconstruct()

            # 'choices' should not be in the kwargs output of deconstruct because storing choices changes to the
            # migrations doesn't add value to the migration. Any data changes will use a data migration management
            # command.
            self.assertNotIn('choices', kwargs,
                             '\'choices\' should not be returned by {}.deconstruct().'.format(cls.__name__))

            # 'max_length' should be in the kwargs output of deconstruct so that a schema migration will be generated if
            # the max_length field changes.
            self.assertIn('max_length', kwargs, '\'max_length\' not returned by {}.deconstruct().'.format(cls.__name__))

            # The attribute values should match an instance created with the args and kwargs output of deconstruct.
            new_instance = cls(*args, **kwargs)
            for attr in ('choices', 'max_length'):
                self.assertEqual(getattr(test_instance, attr), getattr(new_instance, attr))

    def test_forms_char_field_empty_value_allows_none(self):
        form_classes = self._find_localflavor_subclasses(forms.CharField)
        self.assertTrue(len(form_classes) > 0, 'No localflavor forms.CharField classes were found.')

        for cls in form_classes:
            failure_message = '{} does not handle does not properly handle values that are None.'.format(cls.__name__)
            field = cls(required=False, empty_value=None)
            self.assertIsNone(field.clean(None), failure_message)
