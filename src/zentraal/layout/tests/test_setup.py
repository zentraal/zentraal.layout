# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from zentraal.layout.testing import ZENTRAAL_LAYOUT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that zentraal.layout is properly installed."""

    layer = ZENTRAAL_LAYOUT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if zentraal.layout is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'zentraal.layout'))

    def test_browserlayer(self):
        """Test that IZentraalLayoutLayer is registered."""
        from zentraal.layout.interfaces import (
            IZentraalLayoutLayer)
        from plone.browserlayer import utils
        self.assertIn(IZentraalLayoutLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ZENTRAAL_LAYOUT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['zentraal.layout'])

    def test_product_uninstalled(self):
        """Test if zentraal.layout is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'zentraal.layout'))

    def test_browserlayer_removed(self):
        """Test that IZentraalLayoutLayer is removed."""
        from zentraal.layout.interfaces import \
            IZentraalLayoutLayer
        from plone.browserlayer import utils
        self.assertNotIn(IZentraalLayoutLayer, utils.registered_layers())
