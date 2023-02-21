from abc import ABC, abstractmethod


class AbstractOpponent(ABC):
    @abstractmethod
    def choice(self):
        pass


    @abstractmethod
    def addToHistory(self, lastChoice: dict):
        pass
