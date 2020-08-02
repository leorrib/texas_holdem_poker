import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.seven_of_spades = Card(rank = "7", suit = "Spades")
        self.eight_of_spades = Card(rank = "8", suit = "Spades")
        self.nine_of_spades = Card(rank = "9", suit = "Spades")
        self.ten_of_spades = Card(rank = "10", suit = "Spades")
        self.jack_of_spades = Card(rank = "Jack", suit = "Spades")
        self.queen_of_spades = Card(rank = "Queen", suit = "Spades")
        self.king_of_clubs = Card(rank = "King", suit = "Clubs")

        self.cards = [
            self.seven_of_spades,
            self.eight_of_spades,
            self.nine_of_spades,
            self.ten_of_spades,
            self.jack_of_spades,
            self.queen_of_spades,
            self.king_of_clubs
        ]

    def test_validates_that_cards_have_a_straight_flush(self):
        validator = StraightFlushValidator(cards = self.cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_a_straight_flush_from_card_collection(self):
        validator = StraightFlushValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.eight_of_spades,
                self.nine_of_spades,
                self.ten_of_spades,
                self.jack_of_spades,
                self.queen_of_spades,
            ]
        )
