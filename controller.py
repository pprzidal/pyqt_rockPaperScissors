from PyQt6.QtWidgets import QApplication
import model, view, sys, RandomOpponent, SmartOpponent


class Controller:
    def __init__(self, smart=False):
        """
        "Constructor" (i know it's not really a constructor)
        """
        print(smart)
        self.model = model.RockPaperScissors(RandomOpponent.RandomOpponent() if not smart else SmartOpponent.SmartOpponent())
        self.view = view.View(self)

    def reset(self) -> None:
        """
        Resets the UI and the Model
        :return: nothing
        """
        self.model.reset()
        self.view.reset()

    def exit(self) -> None:
        """
        Callback for "exit" button
        :return: doesnt return anything
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
        self.view.setRound(stats[0])
        self.view.setPlayerScore(stats[1])
        self.view.setComputerScore(stats[2])
        self.view.setChoices(f"Spieler [{self.model.toString(stats[4])}], Computer [{self.model.toString(stats[3])}]")


if __name__ == "__main__":
    app = QApplication([])
    c = Controller(smart=sys.argv[1] == "--smart" if len(sys.argv) == 2 else False)
    c.view.show()
    sys.exit(app.exec())
