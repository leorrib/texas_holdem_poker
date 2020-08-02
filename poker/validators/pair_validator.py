from poker.validators import RankAndSuitValidator

class PairValidator(RankAndSuitValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Pair"
    
    def is_valid(self):
        return self._rank_count(2) == 1

    def valid_cards(self):
        # valid_cards = [card for card in self.cards \
        # if self._card_rank_counts[card.rank] == 2]
        
        # return valid_cards
        copy = self.cards[:]
        pair = [card for card in self.cards \
        if self._card_rank_counts[card.rank] == 2]
        for card in pair:
            copy.remove(card)
        valid_cards = copy + pair
        return valid_cards[-5:]