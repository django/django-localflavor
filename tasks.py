import os
from invoke import run, task


@task
def clean():
    run('git clean -Xfd')


@task
def install():
    run('pip install --requirement=tests/requirements.txt')


@task
def test(lang='all'):
    test_cmd = 'coverage run `which django-admin.py` test --settings=tests.settings'
    flake_cmd = 'flake8 --ignore=W801,E128,E501,W402'

    if lang == 'all':
        run('{0} localflavor'.format(flake_cmd))
        run('{0} tests'.format(test_cmd))
        run('coverage report')
    elif lang not in os.listdir('localflavor'):
        print('This language {0!r} is not supported yet.'.format(lang))
    else:
        run('{0} localflavor/{1}'.format(flake_cmd, lang))
        run('{0} tests.test_{1}'.format(test_cmd, lang))
        run('coverage report -m --include=localflavor/{0}/*'.format(lang))


@task
def translations(pull=False):
    if pull:
        run('tx pull -a')
    run('cd localflavor; django-admin.py makemessages -a; django-admin.py compilemessages; cd ..')


@task
def docs():
    run('cd docs; make html; cd ..')
