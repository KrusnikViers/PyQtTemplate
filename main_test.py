import unittest

from main import Application


class MainApplicationTest(unittest.TestCase):
    def test_application_construction(self):
        try:
            Application()
        except Exception as e:
            self.fail('Application creation raises an exception: {}'.format(repr(e)))
