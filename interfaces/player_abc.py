from abc import ABC, abstractmethod
"""
    An abstract class for player class outlining necessary functionality
"""


class PlayerABC(ABC):

    @abstractmethod
    def get_player_name(self):
        pass

    @abstractmethod
    def add_cards(self, card_list):
        pass

    @abstractmethod
    def draw_one(self):
        pass

    @abstractmethod
    def draw_many(self, count=1):
        pass
