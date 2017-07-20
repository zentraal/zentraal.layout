# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import zentraal.layout


class ZentraalLayoutLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=zentraal.layout)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'zentraal.layout:default')


ZENTRAAL_LAYOUT_FIXTURE = ZentraalLayoutLayer()


ZENTRAAL_LAYOUT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ZENTRAAL_LAYOUT_FIXTURE,),
    name='ZentraalLayoutLayer:IntegrationTesting'
)


ZENTRAAL_LAYOUT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ZENTRAAL_LAYOUT_FIXTURE,),
    name='ZentraalLayoutLayer:FunctionalTesting'
)


ZENTRAAL_LAYOUT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ZENTRAAL_LAYOUT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ZentraalLayoutLayer:AcceptanceTesting'
)
