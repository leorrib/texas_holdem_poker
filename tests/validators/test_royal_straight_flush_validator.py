import unittest

from poker.card import Card
from poker.validators import RoyalStraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.eight_of_spades = Card(rank = "8", suit = "Spades")
        self.nine_of_spades = Card(rank = "9", suit = "Spades")
        self.ten_of_spades = Card(rank = "10", suit = "Spades")
        self.jack_of_spades = Card(rank = "Jack", suit = "Spades")
        self.queen_of_spades = Card(rank = "Queen", suit = "Spades")
        self.king_of_spades = Card(rank = "King", suit = "Spades")
        self.ace_of_spades = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            self.eight_of_spades,
            self.nine_of_spades,
            self.ten_of_spades,
            self.jack_of_spades,
            self.queen_of_spades,
            self.king_of_spades,
            self.ace_of_spades
        ]

    def test_validates_that_cards_have_a_royal_straight_flush(self):
        validator = RoyalStraightFlushValidator(cards = self.cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_a_royal_straight_flush_from_card_collection(self):
        validator = RoyalStraightFlushValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.ten_of_spades,
                self.jack_of_spades,
                self.queen_of_spades,
                self.king_of_spades,
                self.ace_of_spades
            ]
        )
