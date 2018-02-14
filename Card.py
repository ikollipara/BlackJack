from random import *

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
    def __init__(self,rank,suit):
        self.__name = rank
        self.__hard = Card.namesHard[rank]
        self.__soft = Card.namesSoft[rank]
        self.__suit = suit

    def use_unicode(self):
        Card.Unicode = not Card.Unicode

    def __str__(self):
        cardStr = ''
        if Card.Unicode:
            cardStr = cardStr + self.__name + ' of ' + Card.suitDict[self.__suit.lower()]
        else:
            cardStr = cardStr + self.__name + ' of ' + self.__suit.lower().capitalize()
        if self.__hard != self.__soft:
            cardStr = cardStr + ': Hard {}, Soft {}'.format(self.__hard,self.__soft)
        else:
            cardStr = cardStr + ': Hard {}'.format(self.__hard)
        return cardStr

    def get_name(self):
        return self.__name

    def __eq__(self, other):
        return self.__name == other.__name
