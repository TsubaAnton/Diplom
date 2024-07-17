from django.test import SimpleTestCase
from importlib import import_module


class WSGITestCase(SimpleTestCase):
    def test_wsgi_application(self):
        module = import_module('config.wsgi')
        self.assertTrue(hasattr(module, 'application'))
