from abc import ABC, abstractmethod

"""
    An abstract class for card outlining generic functionality
"""


class CardABC(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def compare(self, card):
        pass
