from poker.validators import RankAndSuitValidator

class StraightValidator(RankAndSuitValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"
        self.list_rank_indexes = [card.rank_index for card in self.cards]
    
    def is_valid(self):
        if len(self.cards) < 5:
            return False
            
        return len(self._five_consecutive_cards(self.list_rank_indexes)) > 0 

    def valid_cards(self):
        consec_cards = [
            card for card in self.cards
            if card.rank_index in self._five_consecutive_cards(self.list_rank_indexes)
            ]
        valid_cards = [consec_cards[-1]]
        for card in consec_cards:
            if card.rank != valid_cards[-1].rank:
                valid_cards.append(card)
        return valid_cards[-5:]