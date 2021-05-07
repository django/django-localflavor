import glob
import os
import os.path
import sys
from invoke import task


@task
def clean(c):
    c.run('git clean -Xfd')


@task
def test(c, country='all'):
    print('Python version: ' + sys.version)
    test_cmd = 'coverage run `which django-admin` test --settings=tests.settings'
    country = os.environ.get('COUNTRY', country)

    # Fix issue #49
    cwp = os.path.dirname(os.path.abspath(__name__))
    pythonpath = os.environ.get('PYTHONPATH', '').split(os.pathsep)
    pythonpath.append(os.path.join(cwp, 'tests'))
    os.environ['PYTHONPATH'] = os.pathsep.join(pythonpath)

    if country == 'all':
        c.run('{0} tests'.format(test_cmd))
        c.run('coverage report')
    elif country not in os.listdir('localflavor'):
        print('The country {0!r} is not supported yet.'.format(country))
    else:
        c.run('{0} tests.test_{1}'.format(test_cmd, country))
        c.run('coverage report -m --include=localflavor/{0}/*'.format(country))


@task
def compile_translations(c):
    c.run('cd localflavor; django-admin compilemessages; cd ..')


@task(post=[compile_translations])
def pull_translations(c, locale=None):
    if locale:
        c.run('tx pull -f -l {0}'.format(locale))
        po_files = ['localflavor/locale/{0}/LC_MESSAGES/django.po'.format(locale)]
    else:
        c.run('tx pull --minimum-perc=1 -f -a')
        po_files = glob.glob('localflavor/locale/*/LC_MESSAGES/django.po')
        po_files.remove('localflavor/locale/en/LC_MESSAGES/django.po')

    # Remove source lines from po files
    for po_file in po_files:
        c.run('msgcat --no-location -o {0} {0}'.format(po_file))


@task
def make_translations(c, locale='en'):
    with c.cd('localflavor'):
        if locale == 'all':
            c.run('django-admin makemessages -a')
        else:
            c.run('django-admin makemessages -l {locale}'.format(locale=locale))


@task
def docs(c):
    c.run('cd docs; make html; cd ..')
