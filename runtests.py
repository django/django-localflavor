import sys
from os.path import abspath, dirname

from django.conf import settings
import localflavor.tests.settings


sys.path.insert(0, abspath(dirname(__file__)))


if not settings.configured:
    settings.configure(**localflavor.tests.settings.__dict__)


def runtests():
    from django.test.simple import DjangoTestSuiteRunner
    failures = DjangoTestSuiteRunner(failfast=False).run_tests([])
    sys.exit(failures)
