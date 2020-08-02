from poker.validators import RankAndSuitValidator

class StraightFlushValidator(RankAndSuitValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"
    
    def is_valid(self):
        return len(self._five_consecutive_cards_of_same_suit(self.cards)) > 4 

    def valid_cards(self):
        consec_cards = [
            card for card in self.cards
            if card.rank_index in self._five_consecutive_cards_of_same_suit(self.cards)
            ]
        return consec_cards