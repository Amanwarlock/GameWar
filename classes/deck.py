from interfaces.deck_abc import DeckABC
from enums.suits_enum import SuitEnum
from enums.card_enum import CardEnum
from classes.card import Card
from random import shuffle
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

    # Distributes cards randomly between the players (shuffles and distributes) (Builder design pattern)
    def distribute(self, player_one, player_two):
        shuffle(self.deck_of_cards)  # shuffle cards once
        shuffle(self.deck_of_cards)  # shuffle cards twice - Increase random distribution probability and variance
        mid = len(self.deck_of_cards) // 2
        for i in range(mid):
            player_one.add_cards([self.deck_of_cards.pop()])
            player_two.add_cards([self.deck_of_cards.pop()])
        return self

    # Create card instances and adds it to the deck_of_cards array (Builder design pattern)
    def build_deck(self):
        for suit in SuitEnum:
            for card in CardEnum:
                new_card = Card(suit, card)
                self.deck_of_cards.append(new_card)
        return self
