import RandomOpponent
from AbstractOpponent import AbstractOpponent


class RockPaperScissors:
    _ROCK = 0 # TODO hide better
    _PAPER = 1
    _SCISSORS = 2

    def __init__(self, opponent: AbstractOpponent):
        """
        Sets all the values to default
        :param opponent: Which Opponent to use
        """
        self._player_score = 0
        self._computer_score = 0
        self._playerLast = 0
        self._computerLast = 0
        self._round = 0
        self._opponent = opponent

    def play(self, players_choice: int, dchoice=-1) -> tuple:
        """
        Play a new game
        :param players_choice: a number betweeen
        :param dchoice: DO NOT TOUCH only for test purpuses
        :return: tuple with current round, player score, computer score, computer last and player's last pick
        """
        self._playerLast = players_choice
        ochoice = self._opponent.choice() if dchoice == -1 else dchoice
        self._computerLast = ochoice
        if players_choice - 1 == ochoice or (players_choice == self._ROCK and ochoice == self._SCISSORS):
            self._player_score += 1
        elif players_choice != ochoice:
            self._computer_score += 1
        self._round += 1
        return self.stats()

    def reset(self) -> None:
        """
        Resets all the values
        :return: nothing
        """
        self._player_score = 0
        self._computer_score = 0
        self._round = 0

    def stats(self) -> tuple:
        """
        Returns the current stats as a tuple
        :return: tuple with current round, player score, computer score, computer last and player's last pick
        """
        #TODO not so clean i guess
        return (self._round, self._player_score, self._computer_score, self._computerLast, self._playerLast)

    def toString(self, a: int) -> str:
        """
        To map a number to the corresponding string
        :param a: between -1 and 3
        :return: the according String to the number
        """
        return {0: "Rock", 1: "Paper", 2: "Scissors"}[a]


if __name__ == "__main__":
    # Test is kinda shitty
    rps = RockPaperScissors(RandomOpponent.RandomOpponent())
    for players_choice in range(3):
        for ochoice in range(3):
            print(f"Player: {rps.toString(players_choice)}, Opponent: {rps.toString(ochoice)}")
            rps.play(players_choice, ochoice)
            if rps._player_score == 1: print("Player won")
            elif rps._computer_score == 1: print("Opponent won")
            else: print("Tie")
            rps.reset()