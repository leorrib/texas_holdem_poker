import unittest

from unittest.mock import patch
from poker.card import Card
from poker.deck import Deck

class DeckTest(unittest.TestCase):
    
    def test_has_len_equal_to_cards_count(self):
        deck = Deck()
        self.assertEqual(
            len(deck),
            0
        )

    def test_empty_at_start(self):
        deck = Deck()
        self.assertAlmostEqual(
            deck.cards,
            []
        )
    
    def test_adds_cards_to_collection(self):
        card = Card(rank = "Ace", suit = "Spades")
        deck = Deck()
        deck.add_cards([card])
        self.assertEqual(
            deck.cards,
            [card]
        )

    @patch('random.shuffle') # random.shuffled= will be mocked by the second arg of the function below
    def test_shuffles_cards_in_random_order(self, mock_shuffle):
        deck = Deck()

        cards = [ 
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "8", suit = "Diamonds"),
        ]

        deck.add_cards(cards)
        deck.shuffle()
        mock_shuffle.assert_called_once_with(cards)
        # line above can be translated as
        # random.shuffle.assert_called_once_with(cards)

    def test_remove_specified_number_of_cards_from_the_deck(self):
        ace = Card(rank = "Ace", suit = "Spades"),
        eight = Card(rank = "8", suit = "Diamonds"),
        
        cards = [ace, eight]
        deck = Deck()
        deck.add_cards(cards)

        self.assertEqual(
            deck.remove_cards(1),# removes first card from deck
            [ace]
        )

        self.assertEqual(
            deck.cards,
            [eight]
        )
