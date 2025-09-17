from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import QStatusBar, QWidget, QLabel


class StatusBar(QStatusBar):
    def __init__(self, parent: QWidget, main_message: str = ''):
        super().__init__(parent)

        self.setSizeGripEnabled(False)
        self.setStyleSheet('color: #666; background-color: #fff; margin-left: 9px;')

        self._persistent_status: str = main_message
        self._ui_status_label = QLabel()
        self.addWidget(self._ui_status_label, stretch=1)

        # QStatusBar does not style temporary messages properly, thus the manual implementation.
        self._timer = QTimer(self)
        self._timer.setSingleShot(True)
        self._timer.setInterval(5000)
        self._timer.timeout.connect(self._reset_on_timer)

        self.set_status(self._persistent_status)

    @Slot(str)
    def set_temporary_status(self, message: str) -> None:
        self._timer.stop()
        self._timer.start()
        self._ui_status_label.setText(message)

    @Slot(str)
    def set_status(self, message: str) -> None:
        self._persistent_status = message
        if not self._timer.isActive():
            self._ui_status_label.setText(self._persistent_status)

    @Slot()
    def _reset_on_timer(self) -> None:
        self._ui_status_label.setText(self._persistent_status)
