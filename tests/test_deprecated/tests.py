from __future__ import unicode_literals

import warnings

from django.db.models import Model
from django.test import SimpleTestCase, override_settings

from localflavor.au import models as au_models
from localflavor.au.forms import AUPhoneNumberField
from localflavor.be.forms import BEPhoneNumberField
from localflavor.br.forms import BRPhoneNumberField
from localflavor.ca.forms import CAPhoneNumberField
from localflavor.ch.forms import CHPhoneNumberField
from localflavor.cn.forms import CNCellNumberField, CNPhoneNumberField
from localflavor.dk.forms import DKPhoneNumberField
from localflavor.es.forms import ESPhoneNumberField
from localflavor.fr.forms import FRPhoneNumberField
from localflavor.generic.deprecation import RemovedInLocalflavor20Warning
from localflavor.gr.forms import GRMobilePhoneNumberField, GRPhoneNumberField
from localflavor.hk.forms import HKPhoneNumberField
from localflavor.hr.forms import HRPhoneNumberField
from localflavor.id_.forms import IDPhoneNumberField
from localflavor.il.forms import ILMobilePhoneNumberField
from localflavor.in_.forms import INPhoneNumberField
from localflavor.is_.forms import ISPhoneNumberField
from localflavor.it.forms import ITPhoneNumberField
from localflavor.nl import models as nl_models
from localflavor.nl.forms import NLPhoneNumberField
from localflavor.no.forms import NOPhoneNumberField
from localflavor.nz.forms import NZPhoneNumberField
from localflavor.pk import models as pk_models
from localflavor.pk.forms import PKPhoneNumberField
from localflavor.pt.forms import PTPhoneNumberField
from localflavor.ro.forms import ROPhoneNumberField
from localflavor.sg.forms import SGPhoneNumberField
from localflavor.si.forms import SIPhoneNumberField
from localflavor.tr.forms import TRPhoneNumberField
from localflavor.us import models as us_models
from localflavor.us.forms import USPhoneNumberField


class DeprecatedFieldsTests(SimpleTestCase):
    @override_settings(SILENCED_SYSTEM_CHECKS=[])
    def test_PhoneNumberField_deprecated(self):
        class PhoneNumberModel(Model):
            nl_phone_number = nl_models.NLPhoneNumberField()
            au_phone_number = au_models.AUPhoneNumberField()
            us_phone_number = us_models.PhoneNumberField()
            pk_phone_number = pk_models.PKPhoneNumberField()

        model = PhoneNumberModel()

        self.assertTrue(all('is deprecated.' in warn.msg[0] for warn in model.check()))

    def test_PhoneNumberFormField_deprecated(self):
        with warnings.catch_warnings(record=True) as recorded:
            warnings.simplefilter("always")
            AUPhoneNumberField()
            BEPhoneNumberField()
            BRPhoneNumberField()
            CAPhoneNumberField()
            CHPhoneNumberField()
            CNPhoneNumberField()
            CNCellNumberField()
            DKPhoneNumberField()
            ESPhoneNumberField()
            FRPhoneNumberField()
            GRPhoneNumberField()
            GRMobilePhoneNumberField()
            HKPhoneNumberField()
            HRPhoneNumberField()
            IDPhoneNumberField()
            ILMobilePhoneNumberField()
            INPhoneNumberField()
            ISPhoneNumberField()
            ITPhoneNumberField()
            NLPhoneNumberField()
            NOPhoneNumberField()
            NZPhoneNumberField()
            PKPhoneNumberField()
            PTPhoneNumberField()
            ROPhoneNumberField()
            SGPhoneNumberField()
            SIPhoneNumberField()
            TRPhoneNumberField()
            USPhoneNumberField()

        self.assertTrue(all(w.category is RemovedInLocalflavor20Warning for w in recorded))
