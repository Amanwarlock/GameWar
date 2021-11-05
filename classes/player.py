from interfaces.player_abc import PlayerABC
from helpers.queue_using_stacks import QueueUsingStacks
"""
    Player class is responsible for maintaining its hand of cards, retrieval and addition of cards to the hand
"""


class Player(PlayerABC):

    hand = None  # Initialize a queue to hold player cards
    name = None

    def __init__(self, player_name):
        self.name = player_name.capitalize()
        self.hand = QueueUsingStacks()

    def get_player_name(self):
        return self.name

    def add_cards(self, card_list):
        pass

    def draw_one(self):
        pass

    def draw_many(self, count=1):
        pass

    def player_cards_count(self):
        pass
