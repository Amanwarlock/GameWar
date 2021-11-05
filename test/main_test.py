import unittest
from main import Main
from classes.deck import Deck
from classes.card import Card
from enums.suits_enum import SuitEnum
from enums.card_enum import CardEnum
"""
Test file to validate the game play functionality
"""


class MainTest(unittest.TestCase):

    # Test scenario when outcome of the game is a draw i.e., when both the players simultaneously run out of cards
    def test_for_game_draw(self):
        game = Main()
        game.create_players('Mike', 'Blake')
        game.deck = Deck()
        game.start_game()
        self.assertEqual(game.is_draw, True)
        self.assertEqual(game.is_game_on, False)

    # When the first player has no cards, the second player should win
    def test_when_player_one_has_zero_cards(self):
        game = Main()
        game.create_players('Mike', 'Blake')
        game.deck = Deck()
        card_two = Card(SuitEnum.SPADES, CardEnum.TWO)
        game.player_two.add_cards([card_two])
        self.assertEqual(game.player_one.player_cards_count(), 0)
        self.assertEqual(game.player_two.player_cards_count(), 1)
        game.start_game()
        self.assertEqual(game.winner.get_player_name(), 'Blake')

    # When the second player has no cards, the first should win
    def test_when_player_two_has_zero_cards(self):
        game = Main()
        game.create_players('Mike', 'Blake')
        game.deck = Deck()
        card_two = Card(SuitEnum.SPADES, CardEnum.TWO)
        game.player_one.add_cards([card_two])
        self.assertEqual(game.player_two.player_cards_count(), 0)
        self.assertEqual(game.player_one.player_cards_count(), 1)
        game.start_game()
        self.assertEqual(game.winner.get_player_name(), 'Mike')

    # When player one has obtained all the cards, it should be the winner
    def test_with_player_one_as_winner(self):
        game = Main()
        game.create_players('Mike', 'Blake')
        game.deck = Deck()
        card_ace = Card(SuitEnum.SPADES, CardEnum.ACE)
        card_two = Card(SuitEnum.SPADES, CardEnum.TWO)
        game.player_one.add_cards([card_ace])
        game.player_two.add_cards([card_two])
        self.assertEqual(game.player_two.player_cards_count(), 1)
        self.assertEqual(game.player_one.player_cards_count(), 1)
        game.start_game()
        self.assertEqual(game.winner.get_player_name(), 'Mike')

    # When player two acquired all the cards, it should be the sole winner
    def test_with_player_two_as_winner(self):
        game = Main()
        game.create_players('Mike', 'Blake')
        game.deck = Deck()
        card_ace = Card(SuitEnum.SPADES, CardEnum.ACE)
        card_two = Card(SuitEnum.SPADES, CardEnum.TWO)
        game.player_one.add_cards([card_two])
        game.player_two.add_cards([card_ace])
        self.assertEqual(game.player_two.player_cards_count(), 1)
        self.assertEqual(game.player_one.player_cards_count(), 1)
        game.start_game()
        self.assertEqual(game.winner.get_player_name(), 'Blake')

    # When both players draw the same card, battle of cards should begin
    def test_for_war(self):
        game = Main()
        game.create_players('Mike', 'Blake')
        game.deck = Deck()
        card_two = Card(SuitEnum.SPADES, CardEnum.TWO)
        card_four = Card(SuitEnum.SPADES, CardEnum.FOUR)
        card_ten = Card(SuitEnum.SPADES, CardEnum.TEN)
        card_ace = Card(SuitEnum.SPADES, CardEnum.ACE)
        card_jack = Card(SuitEnum.SPADES, CardEnum.JACK)
        game.player_one.add_cards([card_two, card_ace, card_four, card_jack, card_ten])
        game.player_two.add_cards([card_two, card_four, card_ten, card_ace, card_jack])
        self.assertEqual(game.player_two.player_cards_count(), 5)
        self.assertEqual(game.player_one.player_cards_count(), 5)
        game.start_game()
        self.assertEqual(game.winner.get_player_name(), 'Blake')
        self.assertEqual(game.winner.player_cards_count(), 10)
        self.assertEqual(game.player_one.player_cards_count(), 0)

    # Edge case, during war, the player who runs out of cards first should lose
    def test_for_war_with_player_one_having_five_cards(self):
        game = Main()
        game.create_players('Mike', 'Blake')
        game.deck = Deck()
        card_two = Card(SuitEnum.SPADES, CardEnum.TWO)
        card_four = Card(SuitEnum.SPADES, CardEnum.FOUR)
        card_ten = Card(SuitEnum.SPADES, CardEnum.TEN)
        card_ace = Card(SuitEnum.SPADES, CardEnum.ACE)
        card_jack = Card(SuitEnum.SPADES, CardEnum.JACK)
        game.player_one.add_cards([card_two, card_ace, card_four, card_jack, card_ten])
        game.player_two.add_cards([card_two, card_four, card_ten])
        self.assertEqual(game.player_one.player_cards_count(), 5)
        self.assertEqual(game.player_two.player_cards_count(), 3)
        game.start_game()
        self.assertEqual(game.winner.get_player_name(), 'Mike')


if __name__ == '__main__':
    unittest.main()