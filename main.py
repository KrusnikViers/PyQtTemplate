import sys

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QApplication

from ui.main_window.main_window import MainWindow


class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        self.main_window = MainWindow()
        self.main_window.application_exit_requested.connect(self.on_exit_requested)

    @Slot()
    def on_exit_requested(self):
        # Do any pre-exit checks here. Return before the following lines to interrupt application closing.
        self.main_window.application_closing = True
        self.main_window.close()
        self.quit()


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = Application()
    sys.exit(app.exec())
