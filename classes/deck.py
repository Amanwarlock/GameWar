from interfaces.deck_abc import DeckABC
"""
Deck class implementing the abstract class DeckABC
"""


class Deck(DeckABC):

    round = None
    deck_of_cards = None

    def __init__(self):
        self.round = 0
        self.deck_of_cards = []

    # keep track of rounds being played in the game
    def inc_round(self):
        self.round += 1

    # Distributes cards randomly between the players (shuffles and distributes)
    def distribute(self, player_one, player_two):
        pass

    # Create card instances and adds it to the deck_of_cards array
    def build_deck(self):
        pass
