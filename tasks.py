import os
from invoke import run, task


@task
def clean():
    run('git clean -Xfd')


@task
def install():
    run('pip install --requirement=requirements/tests.txt')


@task
def test(lang='all'):
    test_cmd = 'coverage run `which django-admin.py` test --settings=tests.settings'
    flake_cmd = 'flake8 --ignore=W801,E128,E501,W402'

    if lang == 'all':
        run('{} localflavor'.format(flake_cmd))
        run('{} tests'.format(test_cmd))
        run('coverage report')
    elif lang not in os.listdir('localflavor'):
        print('This language {!r} is not supported yet.'.format(lang))
    else:
        run('{} localflavor/{}'.format(flake_cmd, lang))
        run('{} tests.test_{}'.format(test_cmd, lang))
        run('coverage report -m --include=localflavor/{}/*'.format(lang))

travis = test
