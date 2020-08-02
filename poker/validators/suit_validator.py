class SuitValidator():

    def _more_than_five_of_a_suit_in_deck(self):
        suit_gt_five = [
            True for n in range(5, len(self.cards) + 1)
            if n in self._card_suit_counts.values()
        ]

        return len(suit_gt_five) > 0

    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts