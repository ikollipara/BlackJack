from Shoe import Shoe
from Card import Card
from RulesError import RulesError


class Hand(object):
    def __init__(self, card, cardTwo, bet):
        self.cards = [card, cardTwo]
        self.hard = card.hard + cardTwo.hard
        self.soft = card.soft + cardTwo.soft
        self.bet = bet
        self.Stand = False
        self.doubleDown = False
        self.Split = False
        self.BlackJack = False

    def hit(self, card):
        self.cards.append(card)
        self.hard = self.hard + card.hard
        self.soft = self.soft + card.soft

    def double_down(self, card, addedBet):
        self.bet = self.bet + addedBet
        self.hit(card)
        self.doubleDown = True

    def show(self,number):
        return self.cards[number]

    def is_blackjack(self):
        blackjack = 0
        if len(self.cards) == 2:
            cardOne = self.cards[0]
            cardTwo = self.cards[1]
            if cardOne.get_rank() in ['10', 'Jack', 'Queen', 'King'] or cardTwo.get_rank() in ['10', 'Jack', 'Queen',
                                                                                               'King']:
                blackjack += 1
            if cardOne.get_rank() == 'Ace' or cardTwo.get_rank() == 'Ace':
                blackjack += 1
            if blackjack == 2:
                self.BlackJack = True
                self.Stand = True
        return self.BlackJack

    def stand(self):
        self.Stand = True

    def split(self):
        newHand = self.cards.pop()
        Hand.Split = True
        self.hard = self.hard - newHand.hard
        self.soft = self.soft - newHand.soft
        return newHand

    def is_21(self):
        if self.hard == 21 or self.soft == 21:
            return True
        else:
            return False

    def is_split(self):
        return self.Split

    def is_double_down(self):
        return self.doubleDown

    def is_busted(self):
        if self.hard > 21:
            bust = True
        else:
            bust = False
        return bust

    def can_hit(self):
        canHit = True
        if self.is_busted() or self.is_double_down() or self.is_blackjack() or self.is_21() or self.Stand:
            canHit = False
        return canHit

    def can_split(self):
        split = False
        counter = 0
        if len(self.cards) < 2:
            return split
        else:
            for card in self.cards:
                if card.hard == 10:
                    counter += 1
            if counter == 2:
                split = True
        return split

    def can_double(self):
        double = False
        if len(self.cards) == 2:
            double = True
        return double

    def value(self):
        if self.soft > 21:
            return self.hard
        else:
            return self.soft

    def __str__(self):
        handStr = ''
        for card in self.cards:
            handStr = handStr + str(card) + '\n'
        handStr = handStr[:-1]
        if self.hard != self.soft:
            handStr = handStr + """
--------------
Total Hard: {}, Total Soft: {}""".format(self.hard, self.soft)
        elif self.soft > 21:
            handStr = handStr + """
--------------
Total Hard: {}""".format(self.hard)
        else:
            handStr = handStr + """
--------------
Total Hard: {}""".format(self.hard)
        return handStr


def hand_test():
    print("Test No. 1: Create a Hand")
    shoe = Shoe('CardList')
    a = shoe.draw()
    b = shoe.draw()
    hand = Hand(a, b, 10)
    print("Passed" + '\n')
    print("Test No. 2: Print Hand")
    print(hand)
    print("Passed" + '\n')
    print("Test No. 3: Check can_split")
    c = hand.can_split()
    print(c)
    print("Passed" + '\n')
    print("Test No. 4: Check can_hit")
    d = hand.can_hit()
    print(d)
    print("Passed" + '\n')
    print("Test No. 5: Check can_double")
    e = hand.can_double()
    print(e)
    print("Passed" + '\n')
    print("Test No. 6: Check is_blackjack")
    f = hand.is_blackjack()
    print(f)
    print("Passed" + '\n')
    print("Test No. 7: Check is_split")
    g = hand.is_split()
    print(g)
    print("Passed" + '\n')
    print("Test No. 8: Check is_double")
    h = hand.is_double_down()
    print(h)
    print("Passed" + '\n')
    print("Test No. 9: Hit the Hand")
    i = shoe.draw()
    hand.hit(i)
    print("Passed" + '\n')
    print("Test No. 10: Print Hand")
    print(hand)
    print("Passed" + '\n')
    print("Test No. 11: Check can_double")
    j = hand.can_double()
    print(j)
    print("Passed" + '\n')
    print("Test No. 12: Hit until Busted")
    while not hand.is_busted():
        k = shoe.draw()
        hand.hit(k)
    print("Passed" + '\n')
    print("Test No. 13: Print Busted Hand")
    print(hand)
    print("Passed" + '\n')
    print("Test No. 14: Create new Hand")
    l = shoe.draw()
    m = shoe.draw()
    hand = Hand(l, m, 10)
    print("Passed" + '\n')
    print("Test No. 15: Split Hand")
    n = hand.split()
    o = shoe.draw()
    p = shoe.draw()
    handTwo = Hand(n, p, 10)
    hand.hit(o)
    print("Passed" + '\n')
    print("Test No. 16: Print Both Hands")
    print(hand)
    print(handTwo)
    print("Passed" + '\n')
    print("Test No. 17: Create Two Hands at the same time")
    hands = []
    for _ in range(2):
        q = shoe.draw()
        r = shoe.draw()
        hands.append(Hand(q, r, 10))
    print("Passed" + '\n')
    print("Test No. 18: Print Both Hands")
    print(hands[0])
    print(hands[1])
    print("Passed")
    print("Test No. 19: test is_blackjack")
    hand = Hand(Card('Ace', 'spades'), Card('Jack', 'spades'), 10)
    s = hand.is_blackjack()
    print(s)
    print("Passed" + '\n')
    print("Test No. 20: Test is_21")
    t = hand.is_21()
    print(t)
    print("Passed")



