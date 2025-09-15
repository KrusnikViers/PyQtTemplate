# Usage: Settings object can be cached, but it is cheap to recreate it as needed. QSettings implementation takes
# care of the values caching.
# Applicable for both settings that are visible to the user, or simply caching values between sessions.
# To use, add new values to the |Settings| enum.
# Prefer to have similar prefixes for related settings groups.


from dataclasses import dataclass
from enum import Enum
from typing import TypeVar, Type, Generic

from PySide6.QtCore import QSettings

from base.info import PROJECT_NAME, PUBLISHER_NAME

_SType = TypeVar("_SType")


@dataclass
class _SettingsMeta(Generic[_SType]):
    name: str
    type: Type[_SType]
    default: _SType


# Add new values to be stored in this enum.
class Settings(Enum):
    S_ONE = _SettingsMeta('one', int, 42)
    S_TWO = _SettingsMeta('two', int, 4)

    # Example: MY_VALUE = _SettingsMeta('base/my_setting', int, 42)
    # They could be used as Settings.MY_VALUE.set(43) and Settings.MY_VALUE.get()

    @staticmethod
    def _qt_adapter():
        return QSettings(PUBLISHER_NAME, PROJECT_NAME)

    def set(self, value) -> None:
        assert isinstance(value, self.value.type)
        self._qt_adapter().setValue(self.value.name, value)

    def get(self) -> _SType:
        return self._qt_adapter().value(self.value.name, defaultValue=self.value.default, type=self.value.type)
