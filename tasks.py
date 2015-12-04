import os
import os.path
import sys
from invoke import run, task


@task
def clean():
    run('git clean -Xfd')


@task
def test(country='all'):
    print('Python version: ' + sys.version)
    test_cmd = 'coverage run `which django-admin.py` test --settings=tests.settings'
    flake_cmd = 'flake8 --ignore=W801,E128,E501,W402'
    country = os.environ.get('COUNTRY', country)

    # Fix issue #49
    cwp = os.path.dirname(os.path.abspath(__name__))
    pythonpath = os.environ.get('PYTHONPATH', '').split(os.pathsep)
    pythonpath.append(os.path.join(cwp, 'tests'))
    os.environ['PYTHONPATH'] = os.pathsep.join(pythonpath)

    if country == 'all':
        run('{0} localflavor'.format(flake_cmd))
        run('{0} tests'.format(test_cmd))
        run('coverage report')
    elif country not in os.listdir('localflavor'):
        print('The country {0!r} is not supported yet.'.format(country))
    else:
        run('{0} localflavor/{1}'.format(flake_cmd, country))
        run('{0} tests.test_{1}'.format(test_cmd, country))
        run('coverage report -m --include=localflavor/{0}/*'.format(country))


@task
def compile_translations():
    run('cd localflavor; django-admin.py compilemessages; cd ..')


@task(post=[compile_translations])
def pull_translations(locale=None):
    if locale:
        run('tx pull -f -l {0}'.format(locale))
    else:
        run('tx pull --minimum-perc=1 -f -a')


@task(post=[compile_translations])
def make_translations(locale=None):
    if locale:
        run('cd localflavor; '
            'django-admin.py makemessages -l {0}; '.format(locale))
    else:
        run('cd localflavor; django-admin.py makemessages -a')


@task
def docs():
    run('cd docs; make html; cd ..')
