import unittest
from classes.deck import Deck
from classes.player import Player
"""
    Test file validating the functionality of the Deck class
"""


class DeckTest(unittest.TestCase):
    # Should build a deck of cards instance
    def test_build_deck(self):
        deck = Deck()
        deck.build_deck()
        self.assertEqual(len(deck.deck_of_cards), 52)

    # Should distribute cards randomly among two players
    def test_distribute(self):
        player_one = Player('mike')
        player_two = Player('matt')
        deck = Deck()
        deck.build_deck().distribute(player_one, player_two)
        self.assertEqual(len(deck.deck_of_cards), 0)
        self.assertEqual(player_one.player_cards_count(), 26)
        self.assertEqual(player_two.player_cards_count(), 26)


if __name__ == '__main__':
    unittest.main()