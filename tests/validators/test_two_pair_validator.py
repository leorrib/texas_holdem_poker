import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):

    def setUp(self):
        
        self.seven_of_hearts = Card(rank = "7", suit = "Hearts")
        self.seven_of_spades = Card(rank = "7", suit = "Spades")
        self.ten_of_hearts = Card(rank = "10", suit = "Hearts")
        self.ten_of_spades = Card(rank = "10", suit = "Spades")

        self.cards = [
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "5", suit = "Diamonds"),
            self.seven_of_hearts,
            self.seven_of_spades,
            self.ten_of_hearts,
            self.ten_of_spades,
            Card(rank = "Jack", suit = "Spades")
        ]

    def test_validates_that_cards_have_two_pairs(self):
        validator = TwoPairValidator(cards = self.cards)
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_two_pairs_from_card_collection(self):
        validator = TwoPairValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [         
                Card(rank = "Jack", suit = "Spades"),   
                self.seven_of_hearts,
                self.seven_of_spades,
                self.ten_of_hearts,
                self.ten_of_spades
            ]
        )