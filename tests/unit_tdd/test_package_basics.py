from unittest import TestCase
import importlib


class TestPackageBasics(TestCase):
    def test_if_package_exists(self):

        self.assertIsNotNone(importlib.find_loader(
            'pydoautomator'), 'module does not exist!')
