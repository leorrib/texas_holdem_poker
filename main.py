from poker.card import Card
from poker.deck import Deck
from poker.game import Game
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()
hand3 = Hand()

player1 = Player(name = "Leo", hand = hand1)
player2 = Player(name = "Rodrigo", hand = hand2)
player3 = Player(name = "Diego", hand = hand3)
players = [player1, player2, player3]

game = Game(deck = deck, players = players)
game.play()

for player in players:
    index, hand_name, hand_cards = player.best_hand()
    hand_cards_strings = [str(card) for card in hand_cards]
    hand_cards_string = " and ".join(hand_cards_strings)
    print(f"{player.name} has a {hand_name} with the following hand: {hand_cards_string}.")

winners_list_name = [max(players).name]
copy = players[:]
copy.remove(max(players))
for player in copy:
    if player == max(players):
        winners_list_name.append(player.name)
if len(winners_list_name) > 1:
    winning_players_string = " and ".join(winners_list_name)
    print(f"The winners are {winning_players_string}")
elif len(winners_list_name) == 1:
    print(f"The winning player is {winners_list_name[0]}")
    