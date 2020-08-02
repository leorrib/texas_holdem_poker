from poker.validators import RankAndSuitValidator

class FullHouseValidator(RankAndSuitValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Full House"
    
    def is_valid(self):
        if self._rank_count(3) == 2:
            return True
        if self._rank_count(3) == 1 and self._rank_count(2) >= 1:
            return True
        return False

    def valid_cards(self):
        first_three = []
        last_two = []
        copy = self.cards[:]
        
        part1 = [card for card in self.cards \
        if self._card_rank_counts[card.rank] == 3][-3:]

        for card in part1:
            first_three.append(card)
            copy.remove(card)
        for card in copy:
            if self._card_rank_counts[card.rank] >= 2:
                last_two.append(card)
        return last_two[-2:] + first_three