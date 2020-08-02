class RankAndSuitValidator():

    def _rank_count(self, counter):
        count = 0
        for rank_count in self._card_rank_counts.values():
            if rank_count == counter:
                count += 1

        return count

    def _cards_of_same_suit(self):
        same_suit_hand = [
            card for card in self.cards
            if self._card_suit_counts[card.suit] >= 5
        ]
        
        return same_suit_hand

    def _five_consecutive_cards(self, card_set):
        c_list = []
        for elem in reversed(card_set):
            consecutive_rank = list(range(elem, elem + 5))
            if set(consecutive_rank).issubset(set(card_set)):
                c_list = [elem for elem in consecutive_rank]
                return c_list

        return c_list

    def _five_consecutive_cards_of_same_suit(self, card_set):
        same_suit_hand = [
            card.rank_index for card in card_set
            if self._card_suit_counts[card.suit] >= 5
        ]
        
        return self._five_consecutive_cards(same_suit_hand)

    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts


    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
            
        return card_rank_counts