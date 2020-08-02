import unittest
from poker.card import Card


class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suite(self):
        card = Card(rank = "2", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_knows_its_rank_index(self):
        card = Card(rank = "Jack", suit = "Hearts")
        self.assertEqual(card.rank_index, 9)

    def test_has_string_representation(self):
        card = Card(rank = "5", suit = "Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")

    def test_has_technical_representation(self):
        card = Card(rank = "King", suit = "Spades")
        self.assertEqual(repr(card), "Card('King', 'Spades')")

    def test_card_has_four_suite_options(self):
        self.assertEqual(
            Card.SUITS,
            ("Hearts", "Clubs", "Spades", "Diamonds")
        )

    def test_card_has_13_rank_options(self):
        self.assertEqual(
            Card.RANKS,
            ("2", "3", "4", "5", "6", "7", "8", "9", "10", \
            "Jack", "Queen", "King", "Ace")
        )

    def test_card_w_invalid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Spades")

    def test_card_w_invalid_suite(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit = "Spade")

    def test_create_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)
        self.assertEqual(
            cards[0],
            Card(rank = '2', suit = 'Hearts')
        )
        self.assertEqual(
            cards[-1],
            Card(rank = 'Ace', suit = 'Diamonds')
        )

    def test_figures_if_two_cards_are_equal(self):
        self.assertEqual(
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "2", suit = "Hearts")
        )

    def test_card_can_sort_itself_with_another_one(self):
        queen_of_spades = Card(rank = "Queen", suit = "Spades")
        king_of_hearts = Card(rank = "King", suit = "Hearts")
        self.assertTrue(
            queen_of_spades < king_of_hearts,
            "The sort algorithm is not working properly"
            )

    def test_sorts_cards(self):
        two_of_spades = Card(rank = "2", suit = "Spades")
        five_of_diamonds = Card(rank = "5", suit = "Diamonds")
        five_of_hearts = Card(rank = "5", suit = "Hearts")
        eight_of_hearts = Card(rank = "8", suit = "Hearts")
        ace_of_clubs = Card(rank = "Ace", suit = "Clubs")

        unsorted_cards = [
            five_of_hearts,
            two_of_spades,
            five_of_diamonds,
            ace_of_clubs,
            eight_of_hearts
        ]

        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                five_of_diamonds,
                five_of_hearts,
                eight_of_hearts,
                ace_of_clubs
            ]
        )

