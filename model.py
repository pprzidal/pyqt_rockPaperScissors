import RandomOpponent
from AbstractOpponent import AbstractOpponent


class Model:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def __init__(self, opponent: AbstractOpponent):
        self._player_score = 0
        self._computer_score = 0
        self._playerLast = 0
        self._computerLast = 0
        self._round = 0
        self._opponent = opponent

    def play(self, players_choice: int, dchoice=-1):
        self._playerLast = players_choice
        ochoice = self._opponent.choice() if dchoice == -1 else dchoice
        self._computerLast = ochoice
        # TODO find even simpler solution
        if (players_choice == self.ROCK and ochoice == self.SCISSORS) or (players_choice == self.SCISSORS and ochoice == self.PAPER) or (players_choice == self.PAPER and ochoice == self.ROCK):
            self._player_score += 1
        elif players_choice != ochoice:
            self._computer_score += 1
        self._round += 1

    def reset(self):
        self._player_score = 0
        self._computer_score = 0
        self._round = 0

    def stats(self):
        return (self._round, self._player_score, self._computer_score, self._computerLast, self._playerLast)


def toString(a: int):
    return {0: "Rock", 1: "Paper", 2: "Scissors"}[a]


if __name__ == "__main__":
    # Test is kinda shitty
    rps = Model(RandomOpponent.RandomOpponent())
    for players_choice in range(3):
        for ochoice in range(3):
            print(f"Player: {toString(players_choice)}, Opponent: {toString(ochoice)}")
            rps.play(players_choice, ochoice)
            if rps._player_score == 1: print("Player won")
            elif rps._computer_score == 1: print("Opponent won")
            else: print("Tie")
            rps.reset()