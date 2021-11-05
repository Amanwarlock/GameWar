import unittest
"""
Test file to validate the game play functionality
"""


class MainTest(unittest.TestCase):

    # Test scenario when outcome of the game is a draw i.e., when both the players simultaneously run out of cards
    def test_for_game_draw(self):
        pass

    # When the first player has no cards, the second player should win
    def test_when_player_one_has_zero_cards(self):
        pass

    # When the second player has no cards, the first should win
    def test_when_player_two_has_zero_cards(self):
        pass

    # When player one has obtained all the cards, it should be the winner
    def test_with_player_one_as_winner(self):
        pass

    # When player two acquired all the cards, it should be the sole winner
    def test_with_player_two_as_winner(self):
        pass

    # When both players draw the same card, battle of cards should begin
    def test_for_war(self):
        pass

    # Edge case, during war, the player who runs out of cards first should lose
    def test_for_war_with_player_one_having_five_cards(self):
        pass


if __name__ == '__main__':
    unittest.main()