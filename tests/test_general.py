# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import importlib
import pkgutil
import sys

from django import forms
from django.db import models
from django.test.testcases import TestCase
from django.utils import six

import localflavor


class GeneralTests(TestCase):

    @classmethod
    def _find_localflavor_subclasses_py32(cls, base_class):
        classes = []
        for attr in dir(localflavor):
            if attr.startswith('_'):
                continue
            sub_module = importlib.import_module(localflavor.__name__ + '.' + attr)
            if hasattr(sub_module, '__path__'):
                sub_module_fields = cls._find_subclasses_for_package(base_class, sub_module)
                if len(sub_module_fields) > 0:
                    classes.extend(sub_module_fields)
        return classes

    @classmethod
    def _find_subclasses_for_package(cls, base_class, package):
        classes = []
        for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__, prefix=package.__name__ + '.',
                                                              onerror=lambda x: None):
            if ispkg:
                continue
            module = importlib.import_module(modname)
            for f in dir(module):
                if f.startswith('_'):
                    continue
                item = getattr(module, f)
                if package.__name__ in six.text_type(item):
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

        # Finding the localflavor model classes directly with walk_packages doesn't work with Python 3.2. The workaround
        # is to find the classes in all of the submodules.
        if sys.version_info[:2] == (3, 2):
            model_classes = self._find_localflavor_subclasses_py32(models.Field)
        else:
            model_classes = self._find_subclasses_for_package(models.Field, localflavor)
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
        # Finding the localflavor model classes directly with walk_packages doesn't work with Python 3.2. The workaround
        # is to find the classes in all of the submodules.
        if sys.version_info[:2] == (3, 2):
            form_classes = self._find_localflavor_subclasses_py32(forms.CharField)
        else:
            form_classes = self._find_subclasses_for_package(forms.CharField, localflavor)
        self.assertTrue(len(form_classes) > 0, 'No localflavor forms.CharField classes were found.')

        for cls in form_classes:
            failure_message = '{} does not handle does not properly handle values that are None.'.format(cls.__name__)
            # Django < 1.11 doesn't support empty_value
            try:
                field = cls(required=False, empty_value=None)
                self.assertIsNone(field.clean(None), failure_message)
            except TypeError:
                field = cls(required=False)
                self.assertEqual('', field.clean(None), failure_message)
