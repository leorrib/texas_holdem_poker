import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.two_of_clubs = Card(rank = "2", suit = "Clubs")
        self.four_of_diamonds = Card(rank = "4", suit = "Diamonds")
        self.four_of_spades = Card(rank = "4", suit = "Spades")
        self.four_of_hearts = Card(rank = "4", suit = "Hearts")
        self.eight_of_hearts = Card(rank = "8", suit = "Hearts")
        self.ten_of_hearts = Card(rank = "10", suit = "Hearts")
        self.ace_of_clubs = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            self.two_of_clubs,
            self.four_of_diamonds,
            self.four_of_hearts,
            self.four_of_spades,
            self.eight_of_hearts,
            self.ten_of_hearts,
            self.ace_of_clubs
        ]

    def test_validates_that_cards_have_a_three_of_a_kind(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_a_three_of_a_kind_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.ten_of_hearts,
                self.ace_of_clubs,
                self.four_of_diamonds,
                self.four_of_hearts,
                self.four_of_spades
            ]
        )