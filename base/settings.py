# Usage: Settings object can be cached, but it is cheap to recreate it as needed.
# Applicable for both settings that are visible to the user, or simply caching values between sessions.
# To use, add new values to the |StoredSettings| enum.
# Prefer to have similar prefixes for related settings groups.


from enum import Enum
from typing import TypeVar, Type, NamedTuple

from PySide6.QtCore import QSettings

from base.info import PROJECT_NAME, PUBLISHER_NAME

_SType = TypeVar("_SType")


class _StoredSettingsMeta[_SType](NamedTuple):
    stored_name: str
    type: Type[_SType]
    default_value: _SType


# Add new values to be stored in this enum.
class StoredSettings(Enum):
    # Example: MY_VALUE = _StoredSettingMeta('base/my_value', int, 42)
    pass


class Settings:
    @staticmethod
    def _qt_adapter():
        return QSettings(PUBLISHER_NAME, PROJECT_NAME)

    @classmethod
    def set(cls, key: StoredSettings, value: _StoredSettingsMeta) -> None:
        assert isinstance(value, key.value.type)
        cls._qt_adapter().setValue(key.value.stored_name, value)

    @classmethod
    def get(cls, key: StoredSettings) -> _SType:
        return cls._qt_adapter().value(key.value.stored_name, defaultValue=key.value.default_value, type=key.value.type)
