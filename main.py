import sys

from PySide6.QtCore import Slot, Qt, QCoreApplication
from PySide6.QtWidgets import QApplication, QMessageBox


class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        # Replace this with your components.
        self.base_window = QMessageBox()
        self.base_window.setText('PyQtTemplate base message')
        self.base_window.show()


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = Application()
    sys.exit(app.exec())
