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

    def exit(self) -> None:
        """
        Callback for "exit" button
        :return:
        """
        # TODO maybe do some cleanup if needed
        self.view.close()

    def play(self) -> None:
        """
        Callback for "play" button
        :return: doesnt return anything
        """
        pchoice = self.view.getChoice()
        stats = self.model.play(pchoice)
        # TODO das sollte eig. nicht im Controller passieren
        self.view.round.setText(f"{stats[0]}")
        self.view.score_player.setText(f"{stats[1]}")
        self.view.score_computer.setText(f"{stats[2]}")
        self.view.label_2.setText(f"Spieler [{self.model.toString(stats[4])}], Computer [{self.model.toString(stats[3])}]")


if __name__ == "__main__":
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
