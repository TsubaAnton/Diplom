from django.test import SimpleTestCase
from importlib import import_module


class ASGITestCase(SimpleTestCase):
    def test_asgi_application(self):
        module = import_module('config.asgi')
        self.assertTrue(hasattr(module, 'application'))
