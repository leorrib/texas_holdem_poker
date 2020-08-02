import unittest
from unittest.mock import MagicMock
from poker.card import Card
from poker.hand import Hand
from poker.player import Player

class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        player = Player(name = "Boris", hand = hand)
        self.assertEqual(player.name, "Boris")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name = "Boris", hand = mock_hand)
        
        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        
        mock_hand.best_rank.assert_called()

    def test_passes_new_cars_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Kimberly", hand = mock_hand)
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Queen", suit = "Diamonds")
        ]
        player.add_cards(cards)
        mock_hand.add_cards.assert_called_once_with(cards)

    def test_decides_to_continue_or_drop_out(self):
        player = Player(name = "Sharon", hand = Hand())
        self.assertEqual(
            player.wants_to_fold(),
            False
        )

    def test_sort_players_by_best_hand(self):
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (0, "Royal Flush", [])

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (2, "Four of a Kind", [])

        player1 = Player(name = "Kimberly", hand = mock_hand1)
        player2 = Player(name = "Debbie", hand = mock_hand2)

        players = [player1, player2]

        self.assertEqual(
            max(players),
            player1
        )

    def test_sort_players_with_High_Card_in_correct_order(self):
        two_of_clubs = Card(rank = "2", suit = "Clubs")
        queen_of_diamonds = Card(rank = "Queen", suit = "Diamonds")
        
        cards1 = [two_of_clubs]
        cards2 = [queen_of_diamonds]

        mock_hand1 = MagicMock()
        mock_hand2 = MagicMock()

        mock_hand1.best_rank.return_value = (9, "High Card", cards1)
        mock_hand2.best_rank.return_value = (9, "High Card", cards2)

        player1 = Player(name = "Kimberly", hand = mock_hand1)
        player2 = Player(name = "Debbie", hand = mock_hand2)
        players = [player1, player2]

        self.assertEqual(
            max(players),
            player2
        )

    def test_sort_players_with_Pair_in_correct_order(self):
        two_of_clubs = Card(rank = "2", suit = "Clubs")
        two_of_hearts = Card(rank = "2", suit = "Hearts")
        king_of_clubs = Card(rank = "King", suit = "Clubs")
        
        ten_of_clubs = Card(rank = "10", suit = "Clubs")
        queen_of_diamonds = Card(rank = "Queen", suit = "Diamonds")
        queen_of_hearts = Card(rank = "Queen", suit = "Hearts")
        
        cards1 = [king_of_clubs, two_of_clubs, two_of_hearts]
        cards2 = [ten_of_clubs, queen_of_diamonds, queen_of_hearts]

        mock_hand1 = MagicMock()
        mock_hand2 = MagicMock()

        mock_hand1.best_rank.return_value = (8, "Pair", cards1)
        mock_hand2.best_rank.return_value = (8, "Pair", cards2)

        player1 = Player(name = "Kimberly", hand = mock_hand1)
        player2 = Player(name = "Debbie", hand = mock_hand2)
        players = [player1, player2]

        self.assertEqual(
            max(players),
            player2
        )

    def test_points_a_draw_between_two_out_of_three_players(self):
        two_of_clubs = Card(rank = "2", suit = "Clubs")
        two_of_hearts = Card(rank = "2", suit = "Hearts")
        two_of_diamonds = Card(rank = "2", suit = "Diamonds")
        two_of_spades = Card(rank = "2", suit = "Spades")
        seven_of_hearts = Card(rank = "7", suit = "Hearts")
        eight_of_clubs = Card(rank = "8", suit = "Clubs")

        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (9, "Pair", [two_of_clubs, two_of_diamonds])

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (9, "Pair", [two_of_hearts, two_of_spades])

        mock_hand3 = MagicMock()
        mock_hand3.best_rank.return_value = (10, "High Card", [seven_of_hearts, eight_of_clubs])

        player1 = Player(name = "Kimberly", hand = mock_hand1)
        player2 = Player(name = "Debbie", hand = mock_hand2)
        player3 = Player(name = "Amanda", hand = mock_hand3)

        players = [player1, player2, player3]

        self.assertEqual(
            player1,
            player2
        )

        self.assertGreater(
            player1,
            player3
        )

        self.assertGreater(
            player2,
            player3
        )