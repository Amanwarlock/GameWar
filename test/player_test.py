import unittest
from classes.player import Player
from classes.card import Card
from enums.suits_enum import SuitEnum
from enums.card_enum import CardEnum


class PlayerTest(unittest.TestCase):

    def test_player_name(self):
        player = Player('mike')
        expect = 'Mike'
        result = player.get_player_name()
        self.assertEqual(result, expect)

    def test_adding_cards_to_player(self):
        player = Player('mike')
        card = Card(SuitEnum.SPADES, CardEnum.FIVE)
        player.add_cards([card])
        self.assertEqual(player.player_cards_count(), 1)

    def test_drawing_one_card_from_player(self):
        player = Player('mike')
        card_with_rank_five = Card(SuitEnum.SPADES, CardEnum.FIVE)
        player.add_cards([card_with_rank_five])
        card_drawn = player.draw_one()
        self.assertEqual(card_with_rank_five, card_drawn)
        self.assertEqual(card_drawn.rank.value, CardEnum.FIVE.value)

    def test_drawing_multiple_cards_from_player(self):
        player = Player('mike')
        card_with_rank_five = Card(SuitEnum.SPADES, CardEnum.FIVE)
        card_with_rank_two = Card(SuitEnum.SPADES, CardEnum.TWO)
        card_with_rank_ten = Card(SuitEnum.SPADES, CardEnum.TEN)
        player.add_cards([card_with_rank_five, card_with_rank_two, card_with_rank_ten])
        self.assertEqual(player.player_cards_count(), 3)
        drawn_cards = player.draw_many(2)
        self.assertEqual(len(drawn_cards), 2)
        self.assertEqual(player.player_cards_count(), 1)
        self.assertEqual(drawn_cards[0].rank.value, CardEnum.FIVE.value)


if __name__ == '__main__':
    unittest.main()
