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
        pass

    # Compare the rank of the current instance with the instance passed as an argument
    def compare(self, card):
        pass

