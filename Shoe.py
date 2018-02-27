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
            card = self.pop()
            self.__used += 1
            return card
        else:
            print("Passed Cut Card")
            card = self.pop(0)
            self.__used += 1
            return card

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
    print("1. Create a New Shoe")
    shoe = Shoe('CardList')
    print()
    print("2. Print the Shoe")
    print(shoe)
    print()
    print("3. Shuffle the Shoe")
    shoe.shuffle()
    print()
    print("4. Print the Shoe")
    print(shoe)
    print()
    print("5. Create a shoe with 2 Decks")
    shoe = Shoe('CardList',2)
    print()
    print("6. Create a shoe with 1 Deck")
    shoe = Shoe('CardList',1)
    print()
    print("7. Fail Gracefully to create a deck with 0.5 Decks")
    try:
        shoe = Shoe('CardList',0.5)
    except:
        print("successfully failed to create deck with 0.5 decks")
    cutCard = 2
    print()
    print("8. Create a shoe with 1 Deck")
    shoe = Shoe('CardList',1)
    print()
    print("9. Print the Shoe")
    print(shoe)
    shoe.insert_card(cutCard)
    print()
    print("10. Draw a card from the Shoe")
    s = shoe.draw()
    print()
    print("11. Print the Drawn Card")
    print(s)
    print()
    print("12. Draw 10 Cards")
    for placeholder in range(1,10):
        s = shoe.draw()
        print(s)
    print()
    print("13. Print the Shoe")
    print(shoe)
    print()
    print("14. Draw until past the Cut Card")
    for placeholder in range(0,cutCard):
        shoe.draw()
    print("successfully went past the cut card")
    print()
    print("15. Shuffle the Shoe")
    shoe.shuffle()
    print()
    print("16. Print the Shoe")
    print(shoe)
    print()
    print("17. Draw 40 Cards from the Shoe")
    for placeholder in range(1,40):
        s = shoe.draw()
        print(s)
    print()
    print("18. Print the Shoe")
    print(shoe)


