# -*- coding: utf-8 -*-
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'localflavor',
    'localflavor.ar.tests',
    'localflavor.at.tests',
    'localflavor.au.tests',
    'localflavor.be.tests',
    'localflavor.br.tests',
    'localflavor.ca.tests',
    'localflavor.ch.tests',
    'localflavor.cl.tests',
    'localflavor.cn.tests',
    'localflavor.co.tests',
    'localflavor.cz.tests',
    'localflavor.de.tests',
    'localflavor.ec.tests',
    'localflavor.es.tests',
    'localflavor.fi.tests',
    'localflavor.fr.tests',
    'localflavor.gb.tests',
    'localflavor.gr.tests',
    'localflavor.hk.tests',
    'localflavor.hr.tests',
    'localflavor.id_.tests',
    'localflavor.ie.tests',
    'localflavor.il.tests',
    'localflavor.in_.tests',
    'localflavor.is_.tests',
    'localflavor.it.tests',
    'localflavor.jp.tests',
    'localflavor.kw.tests',
    'localflavor.lt.tests',
    'localflavor.mk.tests',
    'localflavor.mx.tests',
    'localflavor.nl.tests',
    'localflavor.no.tests',
    'localflavor.pl.tests',
    'localflavor.pt.tests',
    'localflavor.py_.tests',
    'localflavor.ro.tests',
    'localflavor.ru.tests',
    'localflavor.se.tests',
    'localflavor.si.tests',
    'localflavor.sk.tests',
    'localflavor.tr.tests',
    'localflavor.us.tests',
    'localflavor.uy.tests',
    'localflavor.za.tests',
]

if 'EXTERNAL_DISCOVER_RUNNER' in os.environ:
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
    INSTALLED_APPS += ['discover_runner']

SECRET_KEY = 'spam-spam-spam-spam'
