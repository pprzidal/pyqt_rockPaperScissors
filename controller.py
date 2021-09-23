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
        print(pchoice)
        self.model.play(pchoice)
        tuple = self.model.stats()
        self.view.round.setText(f"{tuple[0]}")
        self.view.score_player.setText(f"{tuple[1]}")
        self.view.score_computer.setText(f"{tuple[2]}")
        self.view.label_2.setText(f"letzter Spielzug: [computer:{tuple[3]}] [spieler:{tuple[4]}]")


if __name__ == "__main__":
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
