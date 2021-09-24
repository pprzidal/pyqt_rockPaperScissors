from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
import controller

"""
"""
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
        self.round.setText('0')
        self.score_player.setText('0')
        self.score_computer.setText('0')
        self.label_2.setText('letzter Spielzug')

    def getChoice(self) -> int:
        return {"Rock": 0, "Paper": 1, "Scissors": 2}[self.comboBox.currentText()]

