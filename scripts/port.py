#!/usr/bin/env python
"""Port localflavors

Usage:
  port.py clone [--dry-run]
  port.py copy [--dry-run]
  port.py copy_locales [--dry-run]
  port.py merge_po [--dry-run]
  port.py move_tests
  port.py (-h | --help)
  port.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --dry-run     Don't actually do something.

"""
import errno
import glob
import os
import envoy
import polib
import shutil
from docopt import docopt
from os.path import join, abspath, exists, dirname, split

github_url = 'https://github.com/%(username)s/django-localflavor-%(country)s'

# repos that have 3rd party maintainers and repos
usernames = {
    'gr': 'spapas',
    'lt': 'simukis',
}

parent_path = abspath(join(dirname(__file__), '..'))
repos_path = join(parent_path, 'repos')

if not exists(repos_path):
    os.makedirs(repos_path)

countries = [
    'us', 'ar', 'au', 'at', 'be', 'br', 'ca', 'cl', 'cn', 'co', 'hr',
    'cz', 'ec', 'fi', 'fr', 'de', 'hk', 'nl', 'is', 'in', 'ie', 'id',
    'il', 'it', 'jp', 'kw', 'mk', 'mx', 'no', 'py', 'pe', 'pl', 'pt',
    'ro', 'ru', 'sk', 'si', 'za', 'es', 'se', 'ch', 'tr', 'gb', 'uy',
    'gr', 'lt',
]


def clone(dry_run=False):
    for country in countries:
        country_url = github_url % dict(country=country,
                                        username=usernames.get(country, 'django'))
        command = 'git clone %s' % country_url
        print command
        if not dry_run:
            response = envoy.run(command, cwd=repos_path)
            print response.std_out


def copy(dry_run=False):
    for country in countries:
        root_name = 'django-localflavor-%s' % country
        package_name = 'django_localflavor_%s' % country
        src = join(repos_path, root_name, package_name)
        dst = join(parent_path, 'localflavor', country)
        print 'copying', src, '-->', dst
        if not dry_run:
            shutil.copytree(src, dst)
        test_src = join(repos_path, root_name, 'tests')
        if exists(test_src):
            test_dst = join(dst, 'tests')
            print 'found test dir', test_src, '| copying to', test_dst
            if not dry_run:
                shutil.copytree(test_src, test_dst)


def copy_locales(dry_run=False):
    for country in countries:
        root_name = 'django-localflavor-%s' % country
        package_name = 'django_localflavor_%s' % country
        src = join(repos_path, root_name, package_name, 'locale')
        if not exists(src):
            continue
        if country in ['in', 'is', 'id']:
            country = '%s_' % country
        dst = join(parent_path, 'localflavor', country, 'locale')
        if exists(dst):
            continue
        print
        print 'copying', src
        print '-->', dst
        if not dry_run:
            shutil.copytree(src, dst)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def merge(src, dst):
    # Store entries in dict/set for faster access
    dst_entries = dict((entry.msgid, entry) for entry in dst)
    # Merge entries that are in the dst
    dst_entries = {}
    for i, entry in enumerate(dst):
        entry.index = i
        dst_entries[entry.msgid] = entry

    for src_entry in src:
        dst_entry = dst_entries.get(src_entry.msgid)
        if dst_entry is None:
            dst.append(src_entry)
        else:
            if dst_entry.msgstr.strip() == '':
                dst.pop(dst_entry.index)
                dst.insert(dst_entry.index, src_entry)
            else:
                print "already exists:", dst_entry.msgid


def merge_po(dry_run=False):
    locale_dir = join(parent_path, 'localflavor', 'locale')
    # create new locale dir
    if not exists(locale_dir):
        os.makedirs(locale_dir)

    for country in countries:
        # source directory
        if country in ['in', 'is', 'id']:
            country = '%s_' % country
        country_locale_dir = join(parent_path, 'localflavor', country, 'locale')

        # iterate over all languages in directory
        for country_locale_subdir in glob.glob('%s/*' % country_locale_dir):

            locale_locale_po_file = join(country_locale_subdir,
                                         'LC_MESSAGES', 'django.po')
            # get locale to update from dir name
            _, subdir_locale = split(country_locale_subdir)

            # build path to new destination locale po file, create dirs
            locale_subdir = join(locale_dir, subdir_locale, 'LC_MESSAGES')
            dest_po_path = join(locale_subdir, 'django.po')
            mkdir_p(locale_subdir)

            print 'merging', locale_locale_po_file, 'into', dest_po_path

            # either load existing file and add the entries of the current source file
            if exists(dest_po_path):
                dest_po = polib.pofile(dest_po_path, encoding='utf-8', check_for_duplicates=True)
                src_po = polib.pofile(locale_locale_po_file, encoding='utf-8')
                merge(src_po, dest_po)
            # or just load the source file directly
            else:
                dest_po = polib.pofile(locale_locale_po_file, encoding='utf-8')

            # update the project-id-version to be consistent
            dest_po.metadata['Project-Id-Version'] = 'django-localflavor'
            # save new po file
            dest_po.save(dest_po_path)
            # and compile it
            dest_po.save_as_mofile(join(locale_subdir, 'django.mo'))
            # print 'percent translated for', dest_po_path, po.percent_translated()

        # throw away the old locale subdir
        if exists(country_locale_dir):
            shutil.rmtree(country_locale_dir)

        # run makemessages with locale to see if it errors out
        # write custom fixes per language


def move_tests():
    locale_dir = join(parent_path, 'localflavor')

    for country in countries:
        country_path = join(locale_dir, country)
        test_path = join(country_path, 'tests')
        test_module = join(test_path, 'tests.py')

        possible_modules = [join(test_path, mod)
                            for mod in ['forms.py', 'models.py']]

        complex_tests = False

        # print 'testing', test_module

        if exists(test_module):
            for possible in possible_modules:
                if exists(possible):
                    print 'complex:', possible, 'exists'
                    complex_tests = True
            if not complex_tests:
                print 'move', test_module, '->', join(country_path, 'tests.py')
                shutil.move(test_module, join(country_path, 'tests.py'))
                shutil.rmtree(test_path)


if __name__ == '__main__':
    args = docopt(__doc__, version='port.py 1.0')

    if args.get('clone'):
        clone(args['--dry-run'])
    elif args.get('copy'):
        copy(args['--dry-run'])
    elif args.get('merge_po'):
        merge_po(args['--dry-run'])
    elif args.get('move_tests'):
        move_tests()
    elif args.get('copy_locales'):
        copy_locales(args['--dry-run'])
