import unittest

from poker.card import Card
from poker.validators import FlushValidator

class FlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card(rank = "3", suit = "Clubs")
        self.five_of_clubs = Card(rank = "5", suit = "Clubs")
        self.six_of_clubs = Card(rank = "6", suit = "Clubs")
        self.ten_of_clubs = Card(rank = "10", suit = "Clubs")
        self.ace_of_clubs = Card(rank = "Ace", suit = "Clubs")
        self.jack_of_hearts = Card(rank = "Jack", suit = "Hearts")
        self.eight_of_clubs = Card(rank = "8", suit = "Clubs")

        self.cards = [
            self.three_of_clubs,
            self.five_of_clubs,
            self.six_of_clubs,
            self.eight_of_clubs,
            self.ten_of_clubs,
            self.jack_of_hearts,
            self.ace_of_clubs
        ]

    def test_validates_that_cards_have_a_flush(self):
        validator = FlushValidator(cards = self.cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_does_not_figure_a_2_hand_card_as_Flush(self):
        two_cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "3", suit = "Spades")
        ]
        
        validator = FlushValidator(cards = two_cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_returns_a_flush_from_card_collection(self):
        validator = FlushValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.five_of_clubs,
                self.six_of_clubs,
                self.eight_of_clubs,
                self.ten_of_clubs,
                self.ace_of_clubs
            ]
        )