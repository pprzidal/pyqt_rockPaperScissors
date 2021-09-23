from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
import controller


class View(QMainWindow):
    def __init__(self, c: controller.Controller):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.default_2.clicked.connect(c.reset)
        self.exit.clicked.connect(c.exit)
        self.play.clicked.connect(c.play)
        self.comboBox.addItem("Rock") # TODO include this in the ui somehow
        self.comboBox.addItem("Paper")
        self.comboBox.addItem("Scissors")

    def reset(self):
        # TODO change this
        self.round.setText('<html><head/><body><p align="center"><span style=" font-size:16pt;">0</span></p></body></html>')
        self.score_player.setText('<html><head/><body><p align="center"><span style=" font-size:16pt;">0</span></p></body></html>')
        self.score_computer.setText('<html><head/><body><p align="center"><span style=" font-size:16pt;">0</span></p></body></html>')
        self.label_2.setText('<html><head/><body><p align="center"><span style=" font-size:16pt;">letzter Spielzug</span></p></body></html>')

    def getChoice(self) -> int:
        return {"Rock": 0, "Paper": 1, "Scissors": 2}[self.comboBox.currentText()]

