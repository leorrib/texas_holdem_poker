import unittest
from unittest.mock import MagicMock, call
from poker.game import Game
from poker.card import Card

class GameTest(unittest.TestCase):

    def setUp(self):
        self.first_two_cards = [
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "6", suit = "Clubs")
        ]
        
        self.next_two_cards = [
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "4", suit = "Spades")
        ]

        self.flop_cards = [
            Card(rank = "2", suit = "Diamonds"),
            Card(rank = "4", suit = "Hearts"),
            Card(rank = "10", suit = "Spades")
        ]

        self.turn_card = [Card(rank = "9", suit = "Hearts")]
        self.river_card = [Card(rank = "Queen", suit = "Clubs")]

    def test_stores_deck_and_players(self):
        deck = MagicMock()
        players = [
            MagicMock(),
            MagicMock()
        ]
        
        game = Game(
            deck = deck,
            players = players
        )

        self.assertEqual(
            game.deck,
            deck
        )

        self.assertEqual(
            game.players,
            players
        )    

    def test_game_play_shuffles_deck(self):
        mock_deck = MagicMock()
        players = [
            MagicMock(),
            MagicMock()
        ]
        
        game = Game(
            deck = mock_deck,
            players = players
        )

        game.play()
        mock_deck.shuffle.assert_called_once() 

    def test_deals_two_initial_cards_to_each_player(self):

        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards, 
            self.next_two_cards, 
            MagicMock(),
            MagicMock(),
            MagicMock()
        ]

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        mock_players = [mock_player1, mock_player2]

        game = Game(
            deck = mock_deck,
            players = mock_players
        )

        game.play()
        mock_deck.remove_cards.assert_has_calls([
            call(2), call(2) #since each player receives 2 cards
        ])

        mock_player1.add_cards.assert_has_calls(
            [call(self.first_two_cards)]
        )
        mock_player2.add_cards.assert_has_calls(
            [call(self.next_two_cards)]
        )

    def test_removes_player_if_not_willing_to_bet(self):
        deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()

        player1.wants_to_fold.return_value = True
        player2.wants_to_fold.return_value = False
        players = [player1, player2]

        game = Game(deck = deck, players = players)
        game.play()

        self.assertEqual(
            game.players,
            [player2]
        )

    def test_deals_each_player_3_flop_1_turn_1_river_cards(self):
        mock_player1 = MagicMock()
        mock_player1.wants_to_fold.return_value = False
        mock_player2 = MagicMock()
        mock_player2.wants_to_fold.return_value = False
        players = [mock_player1, mock_player2]

        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
        ]

        game = Game(deck = mock_deck, players = players)
        game.play()

        mock_deck.remove_cards.assert_has_calls([
            call(3), call(1), call(1)
        ])
        
        calls = [
            call(self.flop_cards),
            call(self.turn_card),
            call(self.river_card)
        ]

        for player in players:
            player.add_cards.assert_has_calls(calls)