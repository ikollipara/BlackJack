from Card import Card
from RulesError import RulesError
from random import *

class Shoe(list):
    def __init__(self, filename, numberOfDecks=6):
        super(Shoe, self).__init__()
        if type(numberOfDecks) == type(2):
            for placeholder in range(numberOfDecks):
                with open(filename) as cardList:
                    for c in cardList:
                        if c[-1] == '\n':
                            cardParts = c[:-1].split(',')
                        else:
                            cardParts = c.split(',')
                        card = Card(cardParts[0],cardParts[1])
                        self.append(card)
        else:
            raise TypeError("numberOfDecks needs to be an int, not {}".format(type(numberOfDecks)))
        self.__stopper = len(self)
        self.__used = 0

    def draw(self):
        if self.__used != self.__stopper:
            card = self.pop(0)
            self.__used += 1
            return card
        else:
            raise RulesError('Not Enough Cards in Deck')

    def insert_card(self, number):
        if int(number) > len(self) or int(number) < 1:
            raise RulesError("Plastic Card not in Deck Length. Default Used")
        else: self.__stopper = int(number)

    def shuffle(self):
        for placeholder in range(1,10001):
            index = randint(0,len(self)-1)
            c = self.pop(index)
            self.append(c)

    def __str__(self):
        shoeStr = []
        for card in self:
            shoeStr.append(str(card))
        return str(shoeStr)


def test():
    shoe = Shoe('CardList')
    print(shoe)
    shoe.shuffle()
    print(shoe)
    shoe = Shoe('CardList',2)
    shoe = Shoe('CardList',1)
    try:
        shoe = Shoe('CardList',0.5)
    except:
        print("successfully failed to create deck with 0.5 decks")
    shoe = Shoe('CardList',1)
    print(shoe)
    shoe.insert_card(10)
    s = shoe.draw()
    print(s)
    for placeholder in range(1,10):
        s = shoe.draw()
        print(s)
    print(shoe)
    try:
        while True:
            shoe.draw()
    except:
        print("successfully failed to go past cut card")
    shoe.shuffle()
    print(shoe)
    shoe = Shoe('CardList')
    for placeholder in range(1,40):
        s = shoe.draw()
        print(s)
    print(shoe)

test()

