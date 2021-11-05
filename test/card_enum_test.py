import unittest
from enums.card_enum import CardEnum

"""
> A test file to validate if card enums can be accessed correctly
"""


class CardEnumTest(unittest.TestCase):

    # Test if card enum with value two can be accessed
    def test_for_card_two(self):
        expected_value = 2
        result = CardEnum.TWO.value
        self.assertEqual(result, expected_value)

    # Test if card enum with value ten can be accessed
    def test_for_card_ten(self):
        expected_value = 10
        result = CardEnum.TEN.value
        self.assertEqual(result, expected_value)

    # Test if card enum with value ace can be accessed
    def test_for_card_ace(self):
        expected_value = 14
        result = CardEnum.ACE.value
        self.assertEqual(result, expected_value)


if __name__ == '__main__':
    unittest.main()
