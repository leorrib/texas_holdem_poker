from poker.validators import RankAndSuitValidator

class TwoPairValidator(RankAndSuitValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Two Pair"
    
    def is_valid(self):
        return self._rank_count(2) >= 2

    def valid_cards(self):
        copy = self.cards[:]
        two_pair = [card for card in self.cards \
        if self._card_rank_counts[card.rank] == 2]
        copy_two_pair = two_pair[-4:]
        for card in copy_two_pair:
            copy.remove(card)
        valid_cards = copy + copy_two_pair
        return valid_cards[-5:]