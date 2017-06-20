# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import importlib
import pkgutil
import sys

from django.db.models import Field
from django.test.testcases import TestCase
from django.utils import six

import localflavor


class GeneralTests(TestCase):

    def _find_package_model_fields(self, package):
        model_fields = []
        for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__, prefix=package.__name__ + '.',
                                                              onerror=lambda x: None):
            if ispkg:
                continue

            module = importlib.import_module(modname)
            for f in dir(module):
                if f.startswith('_'):
                    continue

                item = getattr(module, f)
                if package.__name__ in six.text_type(item) and type(item) == type and issubclass(item, Field):
                    model_fields.append(item)

        return model_fields

    def test_model_field_deconstruct_methods_with_default_options(self):
        # This test can only check the choices and max_length options. Specific tests are required for model fields
        # with options that users can set. See to the IBAN tests for an example.

        # Finding the localflavor model fields directly with walk_packages doesn't work with Python 3.2. The workaround
        # is to find the model fields in all of the submodules.
        if sys.version_info[:2] == (3, 2):
            model_fields = []
            for attr in dir(localflavor):
                if attr.startswith('_'):
                    continue
                sub_module = importlib.import_module(localflavor.__name__ + '.' + attr)
                sub_module_fields = self._find_package_model_fields(sub_module)
                if len(sub_module_fields) > 0:
                    model_fields.extend(sub_module_fields)
        else:
            model_fields = self._find_package_model_fields(localflavor)
        self.assertTrue(len(model_fields) > 0, 'No localflavor model fields were found.')

        for cls in model_fields:
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
