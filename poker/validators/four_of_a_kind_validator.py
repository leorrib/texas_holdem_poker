from poker.validators import RankAndSuitValidator

class FourOfAKindValidator(RankAndSuitValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Four of a Kind"
    
    def is_valid(self):
        return self._rank_count(4) == 1

    def valid_cards(self):
        copy = self.cards[:]
        four = [card for card in self.cards \
        if self._card_rank_counts[card.rank] == 4]
        for card in four:
            copy.remove(card)
        valid_cards = copy + four
        return valid_cards[-5:]