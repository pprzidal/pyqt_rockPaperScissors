import AbstractOpponent
from random import randrange


class RandomOpponent(AbstractOpponent.AbstractOpponent):
    def choice(self) -> int:
        return randrange(3)
