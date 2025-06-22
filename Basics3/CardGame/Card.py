import Inputs

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Inputs.values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
