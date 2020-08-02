import random

class Deck():
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def add_cards(self, cards):
        self.cards.extend(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_cards(self, num):
        cards_to_remove = self.cards[:num]
        del self.cards[:num] #deletes first 'num' cards from self.cards permanently
        return cards_to_remove