from enum import Enum
from pathlib import Path

from PySide6.QtGui import QIcon


def _load_icon(name: str) -> QIcon:
    icon_path = Path(__file__).parent / name
    assert icon_path.is_file()
    return QIcon(str(icon_path))


class IconsList(Enum):
    # Adding icons: ICON_NAME = _load_icon('icon.svg')
    pass
