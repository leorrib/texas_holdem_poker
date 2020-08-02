import unittest

from poker.card import Card
from poker.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card(rank = "3", suit = "Clubs")
        self.four_of_diamonds = Card(rank = "4", suit = "Diamonds")
        self.five_of_spades = Card(rank = "5", suit = "Spades")
        self.six_of_hearts = Card(rank = "6", suit = "Hearts")
        self.seven_of_diamonds = Card(rank = "7", suit = "Diamonds")
        self.seven_of_hearts = Card(rank = "7", suit = "Hearts")
        self.eight_of_clubs = Card(rank = "8", suit = "Clubs")
        self.nine_of_clubs = Card(rank = "9", suit = "Clubs")
        self.ace_of_spades = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            self.three_of_clubs,
            self.four_of_diamonds,
            self.five_of_spades,
            self.six_of_hearts,
            self.seven_of_diamonds,
            self.seven_of_hearts,
            self.eight_of_clubs,
            self.nine_of_clubs,
            self.ace_of_spades
        ]

    def test_validates_that_cards_have_a_straight(self):
        validator = StraightValidator(cards = self.cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_a_straight_from_card_collection(self):
        validator = StraightValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.five_of_spades,
                self.six_of_hearts,
                self.seven_of_diamonds,
                self.eight_of_clubs,
                self.nine_of_clubs
            ]
        )

    def test_does_not_figure_a_2_hand_card_as_Straight(self):
        two_cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "3", suit = "Hearts")
        ]
        
        validator = StraightValidator(cards = two_cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )