from PyQt6.QtWidgets import QApplication
import model, view, sys
from RandomOpponent import RandomOpponent

"""
"""


class Controller:
    def __init__(self):
        self.model = model.Model(RandomOpponent())
        self.view = view.View(self)

    def reset(self) -> None:
        self.model.reset()
        self.view.reset()

    def exit(self):
        # TODO maybe do some cleanup if needed
        self.view.close()

    def play(self):
        pchoice = self.view.getChoice()
        self.model.play(pchoice)


if __name__ == "__main__":
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
