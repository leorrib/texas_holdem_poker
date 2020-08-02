import unittest

from poker.card import Card
from poker.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        
        self.four_of_diamonds = Card(rank = "4", suit = "Diamonds")
        self.four_of_spades = Card(rank = "4", suit = "Spades")
        self.four_of_hearts = Card(rank = "4", suit = "Hearts")
        self.eight_of_hearts = Card(rank = "8", suit = "Hearts")
        self.eight_of_clubs = Card(rank = "8", suit = "Clubs")
        self.eight_of_spades = Card(rank = "8", suit = "Spades")
        self.ten_of_hearts = Card(rank = "10", suit = "Hearts")


        self.cards = [
            self.four_of_diamonds,
            self.four_of_hearts,
            self.four_of_spades,
            self.eight_of_clubs,
            self.eight_of_hearts,
            self.eight_of_spades,
            self.ten_of_hearts
        ]

    def test_validates_that_cards_have_a_full_house(self):
        validator = FullHouseValidator(cards = self.cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_a_full_house_from_card_collection(self):
        validator = FullHouseValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.four_of_hearts,
                self.four_of_spades,
                self.eight_of_clubs,
                self.eight_of_hearts,
                self.eight_of_spades
            ]
        )