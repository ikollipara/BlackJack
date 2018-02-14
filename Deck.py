from Card import Card
from random import *

class Deck(list):
    def __init__(self, filename):
        super(Deck, self).__init__()
        with (filename, 'r') as cardList:
            for c in cardList:
                cardParts = c[:-1].split(',')
                card = Card(cardParts[0],cardParts[1],True)
                self.append(card)

    def __str__(self):
        deckString = ''
        for card in self:
            deckString += str(card) + ', '
        deckString = deckString[:-2] + ']'
        return deckString

    def draw(self):
        if len(self) > 0:
            card = self.pop()
        else:
            raise ValueError("Not enough cards in Deck")
        return card

