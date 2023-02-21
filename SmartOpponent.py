import AbstractOpponent


class SmartOpponent(AbstractOpponent.AbstractOpponent):
    def __init__(self):
        self._hist = []

    def choice(self) -> int:
        players_favourite = {"Rock": 0, "Paper": 0, "Scissors": 0}
        # players_winrate = {"Rock": 0, "Paper": 0, "Scissors": 0}
        for entry in self._hist:
            players_favourite[entry["player"]] += 1
            # players_winrate[entry["player"]] = players_winrate[entry["player"]] + (1 if entry["won"] == "player" else 0)  / players_favourite[entry["player"]]
        for k in players_favourite:
            print(f"{k}\t{players_favourite[k]}")
        """
        for k in players_winrate:
            print(f"{k}\t{players_winrate[k]}")
        """
        return 0

    def _complementary(self, ):

    def addToHistory(self, lastChoice: dict):
        self._hist.append(lastChoice)
        """
        {"player": "Rock", "computer": "Scissors", "won": "player"}
        """

