import unittest
from classes.card import Card
from enums.suits_enum import SuitEnum
from enums.card_enum import CardEnum
"""
    Test file that test the scenarios for the card class
"""


class CardTest(unittest.TestCase):

    # Should create a card with given attributes
    def test_creating_card(self):
        card = Card(SuitEnum.SPADES, CardEnum.TWO)
        self.assertEqual(card.suit.value, SuitEnum.SPADES.value)
        self.assertEqual(card.rank.value, CardEnum.TWO.value)

    # Should perform comparison between two instances of the card
    def test_card_compare(self):
        card_with_rank_two = Card(SuitEnum.SPADES, CardEnum.TWO)
        card_with_rank_five = Card(SuitEnum.SPADES, CardEnum.FIVE)
        result_a = card_with_rank_two.compare(card_with_rank_five)
        self.assertEqual(result_a, -1)
        result_b = card_with_rank_two.compare(card_with_rank_two)
        self.assertEqual(result_b, 0)
        result_c = card_with_rank_five.compare(card_with_rank_two)
        self.assertEqual(result_c, 1)


if __name__ == '__main__':
    unittest.main()
