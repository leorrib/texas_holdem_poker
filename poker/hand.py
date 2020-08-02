from poker.validators import (
    RoyalStraightFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardsValidator
)

class Hand():
    VALIDATORS = (
        RoyalStraightFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator
    )

    def __init__(self):
        self.cards = []

    def __repr__(self):
        cars_as_strings = [str(card) for card in self.cards]
        return ", ".join(cars_as_strings)

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def best_rank(self):
        for index, validator_class in enumerate(self.VALIDATORS):
            validator = validator_class(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())