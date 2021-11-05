import unittest
from enums.suits_enum import SuitEnum

"""
> A test file to verify suits enum class
"""


class SuitEnumTest(unittest.TestCase):

    def test_for_spade(self):
        expected = 'spades'
        result = SuitEnum.SPADES.value
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
