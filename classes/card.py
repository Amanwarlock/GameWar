from interfaces.card_abc import CardABC
"""
 Card class implementing the abstract class CardABC
"""


class Card(CardABC):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Displays the card properties / attributes
    def show(self):
        return f"{self.suit.value} with rank {self.rank.value}"

    # Compare the rank of the current instance with the instance passed as an argument
    def compare(self, card):
        delta = self.rank.value - card.rank.value
        if delta > 0:
            return 1
        elif delta < 0:
            return -1
        else:
            return 0

