from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        # self.round.setAlignment(QtCore.Qt.AlignHCenter)
        # QtCore.Qt.center(self.round)


if __name__ == '__main__':
    import sys
    app = QApplication([])
    v = View()
    v.show()
    sys.exit(app.exec())