import unittest
import re

from base.settings import Settings, StoredSettings


class TestSettings(unittest.TestCase):
    def test_validate_stored_keys(self):
        keys_set = set()
        for settings_value in StoredSettings:
            stored_key = settings_value.value.stored_name

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
        for settings_value in StoredSettings:
            self.assertTrue(isinstance(settings_value.value.default_value, settings_value.value.type),
                            'Default value for {} should be {}'.format(settings_value.name, settings_value.value.type))
