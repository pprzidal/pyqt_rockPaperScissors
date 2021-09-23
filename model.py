from AbstractOpponent import AbstractOpponent


class Model:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def __init__(self, opponent: AbstractOpponent):
        self._player_score = 0
        self._computer_score = 0
        self._round = 0
        self._opponent = opponent

    def play(self, players_choice: int):
        ochoice = self._opponent.choice()
        # TODO find even simpler solution
        if players_choice > ochoice or (players_choice == Model.ROCK and ochoice == Model.SCISSORS) and not (players_choice == Model.SCISSORS and ochoice == Model.ROCK):
            self._player_score += 1
        elif players_choice != ochoice:
            self._computer_score += 1
        self._round += 1

    def reset(self):
        self._player_score = 0
        self._computer_score = 0
        self._round = 0

def toString(a: int):
    if a == 0: return "Rock"
    elif a == 1: return "Paper"
    elif a == 2: return "Scissors"

if __name__ == "__main__":
    for players_choice in range(3):
        for ochoice in range(3):
            print(f"Player: {toString(players_choice)}, Opponent: {toString(ochoice)}")
            if (players_choice == Model.ROCK and ochoice == Model.SCISSORS) or players_choice > ochoice and not (players_choice == Model.SCISSORS and ochoice == Model.ROCK):
                print("Player wins")
            elif ochoice != players_choice:
                print("Opponent wins")
            else:
                print("Tie")