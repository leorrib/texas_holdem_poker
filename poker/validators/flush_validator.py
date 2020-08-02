from poker.validators import RankAndSuitValidator

class FlushValidator(RankAndSuitValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Flush"
    
    def is_valid(self):

        return len(self._cards_of_same_suit()) > 4

    def valid_cards(self):
        valid_cards = self._cards_of_same_suit()
        if len(valid_cards) > 5:
            i = len(valid_cards) - 5
            return valid_cards[i:]
        return valid_cards