import os
import glob
import shutil

here = os.path.dirname(__file__)

parent = os.path.join(here, '..')

tests_dir = os.path.join(parent, 'tests')

if not os.path.exists(tests_dir):
    os.makedirs(tests_dir)


for country_dir in glob.glob('%s/localflavor/*' % parent):
    _, country_slug = os.path.split(country_dir)
    if country_slug.endswith('_'):
        country_slug = country_slug[:-1]

    print 'checking country dir', country_dir, country_slug
    test_file = os.path.join(country_dir, 'tests.py')
    if os.path.isfile(test_file):
        print 'found test file', test_file
        shutil.move(test_file, os.path.join(tests_dir, 'test_%s.py' % country_slug))

    test_module = os.path.join(country_dir, 'tests')
    if os.path.isdir(test_module):
        print 'found test module', test_module
        shutil.move(test_module, os.path.join(tests_dir, 'test_%s' % country_slug))
