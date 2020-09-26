from unittest import TestCase
import importlib
import pydoautomator
import inspect


class TestPackageBasics(TestCase):
    def test_if_package_exists(self):

        self.assertIsNotNone(importlib.find_loader(
            'pydoautomator'), 'module does not exist!')

    def test_if_Droplet_exists_in_package(self):
        self.assertTrue(
            hasattr(pydoautomator, 'Droplet'),
            'Droplet does not exists in package'
        )

    def test_Droplet_should_be_not_none(self):
        self.assertIsNotNone(
            pydoautomator.Droplet,
            'Droplet has None value!'
        )

    def test_if_Droplet_is_a_class(self):
        self.assertTrue(
            inspect.isclass(pydoautomator.Droplet),
            'pydoautomator.Droplet is not a class'
        )

    def test_if_Droplet_is_from_droplet_submodule(self):
        self.assertTrue(
            pydoautomator.Droplet.__module__ == 'pydoautomator.droplet',
            'pydoautomator.Droplet is NOT a module from pydoautomator.droplet'
        )

    def test_create_droplet_should_exist(self):
        self.assertTrue(
            hasattr(pydoautomator.Droplet, 'create_droplet')
        )
