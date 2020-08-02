from poker.validators import RankAndSuitValidator

class RoyalStraightFlushValidator(RankAndSuitValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Royal Straight Flush"
    
    def is_valid(self):
        if len(self.valid_cards()) < 2:
            return False
        
        if self.valid_cards()[-1].rank == "Ace":
            return len(self._five_consecutive_cards_of_same_suit(self.cards)) > 4 
        return False

    def valid_cards(self):
        consec_cards = [
            card for card in self.cards
            if card.rank_index in self._five_consecutive_cards_of_same_suit(self.cards)
        ]
        return consec_cards