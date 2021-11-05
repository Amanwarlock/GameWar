from abc import ABC, abstractmethod

"""
    An abstract class for deck of cards class outlining generic functionality
"""


class DeckABC(ABC):
    @abstractmethod
    def build_deck(self):
        pass

    @abstractmethod
    def distribute(self, player_one, player_two):
        pass

    @abstractmethod
    def inc_round(self):
        pass
