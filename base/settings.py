# Usage: Settings object is safe to be cached, and cheap to recreate if needed.
# Add new values to the `Settings` enum for both settings that are visible to the user, or simply caching some values
# between sessions.

from dataclasses import dataclass
from enum import Enum
from typing import TypeVar, Type, Generic

from PySide6.QtCore import QSettings, QRect

from base.info import PROJECT_NAME, PUBLISHER_NAME

_SType = TypeVar("_SType")


@dataclass
class _SettingsMeta(Generic[_SType]):
    name: str
    type: Type[_SType]
    default: _SType


# Add new values to be stored in this enum.
class Settings(Enum):
    # Example: MY_VALUE = _SettingsMeta('base/my_setting', int, 42)
    # They could be used as Settings.MY_VALUE.set(43) and Settings.MY_VALUE.get()
    UI_MAIN_WINDOW_GEOMETRY = _SettingsMeta('ui/main_window_geometry', QRect, QRect())

    @staticmethod
    def _qt_adapter():
        # TODO: Make sure that the settings will be synced on exit, and do not sync unnecessarily.
        # QSettings implementation takes care of the values caching.
        return QSettings(PUBLISHER_NAME, PROJECT_NAME)

    def set(self, value) -> None:
        assert isinstance(value, self.value.type)
        self._qt_adapter().setValue(self.value.name, value)

    def get(self) -> _SType:
        return self._qt_adapter().value(self.value.name, defaultValue=self.value.default, type=self.value.type)
