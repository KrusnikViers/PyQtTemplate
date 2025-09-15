import re
import unittest

from base.settings import Settings


class TestSettings(unittest.TestCase):
    def test_validate_stored_keys(self):
        keys_set = set()
        for settings_value in Settings:
            stored_key = settings_value.value.name

            self.assertTrue(stored_key, "Stored key for {} is empty.".format(settings_value.name))
            self.assertTrue(re.match(r'^[\w/\-]*$', stored_key),
                            'Stored settings key {} has characters that are not alphanumeric, /, - or _.'.format(
                                stored_key))
            self.assertTrue(stored_key.islower(),
                            'Stored key {} should be in lower register to avoid cross-system conflicts.'.format(
                                stored_key))

            self.assertFalse(stored_key in keys_set, 'Duplicate stored key: {}'.format(stored_key))
            keys_set.add(stored_key)

    def test_validate_default_value_types(self):
        for setting in Settings:
            self.assertTrue(isinstance(setting.value.default, setting.value.type),
                            'Default value for {} should be {}'.format(setting.name, setting.value.type))
