import unittest

from poker.card import Card
from poker.validators import PairValidator

class PairValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_a_pair(self):
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Hearts")
        ]

        validator = PairValidator(cards = cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_a_winning_hand_with_pair_from_card_collection(self):
        seven_of_diamonds = Card(rank = "7", suit = "Diamonds")
        seven_of_spades = Card(rank = "7", suit = "Spades")

        cards = [       
            Card(rank = "2", suit = "Spades"),
            Card(rank = "5", suit = "Spades"),
            seven_of_diamonds,
            seven_of_spades,
            Card(rank = "8", suit = "Diamonds"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs")
        ]

        validator = PairValidator(cards = cards)
        self.assertEqual(
            validator.valid_cards(),
            [   
                Card(rank = "8", suit = "Diamonds"),
                Card(rank = "10", suit = "Clubs"),
                Card(rank = "Queen", suit = "Clubs"),
                seven_of_diamonds, 
                seven_of_spades
            ]
        )