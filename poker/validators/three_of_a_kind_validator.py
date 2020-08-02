from poker.validators import RankAndSuitValidator

class ThreeOfAKindValidator(RankAndSuitValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Three of a Kind"
    
    def is_valid(self):
        return self._rank_count(3) == 1

    def valid_cards(self):
        copy = self.cards[:]
        three = [card for card in self.cards \
        if self._card_rank_counts[card.rank] == 3]
        for card in three:
            copy.remove(card)
        valid_cards = copy + three
        return valid_cards[-5:]