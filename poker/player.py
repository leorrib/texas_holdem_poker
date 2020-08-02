class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __eq__(self, other):
        current_player_best_cards = self.best_hand()[2]
        other_player_best_cards = other.best_hand()[2]

        if self.best_hand()[0] == other.best_hand()[0]:
            current_player_cards_rank = [card.rank_index for card in current_player_best_cards]
            other_player_cards_rank = [card.rank_index for card in other_player_best_cards]
            return current_player_cards_rank == other_player_cards_rank


    def __gt__(self, other):
        current_player_best_validator_index = self.best_hand()[0]
        current_player_best_cards = self.best_hand()[2]
        other_player_best_validator_index = other.best_hand()[0]
        other_player_best_cards = other.best_hand()[2]
        card_count = 1

        if current_player_best_validator_index != other_player_best_validator_index:
            return current_player_best_validator_index < other_player_best_validator_index
        else:
            while card_count <= len(current_player_best_cards):
                if current_player_best_cards[-card_count].rank_index != other_player_best_cards[-card_count].rank_index:
                    return current_player_best_cards[-card_count].rank_index >  other_player_best_cards[-card_count].rank_index
                card_count += 1

    def best_hand(self):
        return self.hand.best_rank()

    def add_cards(self, cards):
        self.hand.add_cards(cards)

    def wants_to_fold(self):
        return False
        # player wants to continue o fold?
        # how much they want to wager
        # is the wager smaller than the amount the player has?
        # if self.wager_amount < self.amount_they_have_left:

        