from random import *
from RulesError import RulesError

class Card(object):
    #region Class Values
    hard = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    soft = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    suitUnicode = ['\u2660','\u2663','\u2661','\u2662']
    suits = ['spades','clubs','hearts','diamonds']
    names = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    Unicode = True
    #endregion
    #region Class Dicts
    namesHard = dict(zip(names,hard))
    namesSoft = dict(zip(names,soft))
    suitDict = dict(zip(suits,suitUnicode))
    #endregion
    def __init__(self,rank,suit,showing=True):
        self.__name = rank
        self.__hard = Card.namesHard[rank]
        self.__soft = Card.namesSoft[rank]
        self.__suit = suit
        self.__showing = showing

    def flip(self):
        self.__showing = not self.__showing

    def use_unicode(self):
        Card.Unicode = not Card.Unicode

    def __str__(self):
        cardStr = ''
        if self.__showing:
            if Card.Unicode:
                cardStr = cardStr + self.__name + Card.suitDict[self.__suit.lower()]
            else:
                cardStr = cardStr + self.__name + ' of ' + self.__suit.lower().capitalize()
            return cardStr
        else:
            raise RulesError("Cannot see unflipped Card")

    def get_hard(self):
        return self.__hard

    def get_soft(self):
        return self.__soft

    def get_rank(self):
        return self.__name

    def __eq__(self, other):
        return self.__hard == other.__hard

    hard = property(get_hard)
    soft = property(get_soft)
    rank = property(get_rank)