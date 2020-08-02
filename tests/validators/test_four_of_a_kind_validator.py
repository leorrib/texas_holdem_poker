import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        
        self.four_of_diamonds = Card(rank = "4", suit = "Diamonds")
        self.four_of_spades = Card(rank = "4", suit = "Spades")
        self.four_of_hearts = Card(rank = "4", suit = "Hearts")
        self.four_of_clubs = Card(rank = "4", suit = "Clubs")
        self.eight_of_clubs = Card(rank = "8", suit = "Clubs")
        self.ten_of_hearts = Card(rank = "10", suit = "Hearts")


        self.cards = [
            self.four_of_clubs,
            self.four_of_diamonds,
            self.four_of_hearts,
            self.four_of_spades,
            self.eight_of_clubs,
            self.ten_of_hearts
        ]

    def test_validates_that_cards_have_a_4_of_a_kind(self):
        validator = FourOfAKindValidator(cards = self.cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_a_4_of_a_kind_from_card_collection(self):
        validator = FourOfAKindValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.ten_of_hearts,
                self.four_of_clubs,
                self.four_of_diamonds,
                self.four_of_hearts,
                self.four_of_spades
            ]
        )