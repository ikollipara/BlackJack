from RulesError import RulesError
from Hand import Hand
from Card import Card

class Player(object):
    Surrender = False
    def __init__(self, name, money=1000):
        self.name = name
        self.money = money
        self.table = None
        self. hands = []
        self.Insurance = False
        self.InsuranceBet = 0

    def sit(self, table):
        """Adds player to the Table"""
        self.table = table
        table.Players.append(self)

    def clear_hands(self):
        """Removes all player hands"""
        self.hands = []

    def add_hand(self,hand):
        """Adds a hand to the player"""
        self.hands.append(hand)

    def bet_or_leave(self):
        """asks the user if they want to bet or leave. If they bet 0 they sit the round out"""
        print("""
[B]et
[L]eave""")
        legalInputs = ['bet','leave','b','l']
        command = input()
        if command.lower() not in legalInputs:
            print("Please enter in a real command")
            command = input()
        else:
            if command.lower() in ['bet','b']:
                bet = input("Please enter your bet: ")
            else:
                bet = None
            return bet

    def play(self, card, hand):
        legalCommands = ['h', 's', 'd', 'p', 'i', 'hit', 'stand', 'double down', 'split', 'insurance']
        print("""
Name: {}
Dealer's Card: {}, Not Showing
{}""".format(self.name, card,str(hand)))
        if hand.can_split():
            if card.hard == 10:
                print("""
Menu Options:
[H]it
[S]tand
[D]ouble Down
S[P]lit
""")
            elif card.rank == 'Ace':
                print("""
Menu Options:
[H]it
[S]tand
[D]ouble Down
S[P]lit
[I]nsurance
""")
            else:
                print("""
Menu Options:
[H]it
[S]tand
[D]ouble Down
S[P]lit
""")
        elif hand.can_split() == False:
            if card.hard == 10:
                print("""
Menu Options:
[H]it
[S]tand
[D]ouble Down
""")
            elif card.rank == 'Ace':
                print("""
Menu Options:
[H]it
[S]tand
[D]ouble Down
[I]nsurance
""")
            else:
                print("""
Menu Options:
[H]it
[S]tand
[D]ouble Down
""")
        command = input()
        while command.lower() not in legalCommands:
            print("Please enter in a real command")
            command = input()
        else:
            return command

    def insurance(self, sideBet):
        """Gives player insurance. Checks for multiple insurance from a player"""
        if self.Insurance == True:
            raise RulesError("Cannot have mulitple Insurances per hand")
        else:
            self.Insurance = True
            self.InsuranceBet = sideBet

    def surrender(self, hand):
        bet = hand.bet/2
        self.money = self.money - int(bet)


    def has_surrendered(self):
        return Player.Surrender

    def is_Insured(self):
        """Returns Insurance"""
        return self.Insurance

    def rake_in(self, bet):
        """Adds money to the player's amount"""
        self.money += bet

    def rake_out(self, bet):
        """Removes money from the player. Ran by dealer during the betting phase"""
        self.money = self.money - bet

    def __str__(self):
        handStr = ''
        if len(self.hands) > 0:
            for hand in self.hands:
                handStr = handStr + str(hand) + '\n'
        else:
            handStr = 'None'
        playerStr = """
Name:       {}
Money:      {}
# of Hands: {}
------------------
{}""".format(self.name, self.money, len(self.hands), handStr)
        return playerStr


def test():
    print("Test No. 1: Create Player")
    player = Player('Ian')
    print("Passed" + '\n')
    print("Test No. 2: Print Player")
    print(player)
    print("Passed" + '\n')
    print("Test No. 3: Run player.play base")
    baseHand = Hand(Card('9','spades'),Card('7','hearts'),10)
    a = player.play(Card('6','spades'),baseHand)
    print("Passed" + '\n')
    print("Test No. 4: Print Choice")
    print(a)
    print("Passed" + '\n')
    print("Test No. 5: Run player.play w/ split")
    splitHand = Hand(Card('Jack','spades'),Card('Queen','spades'),10)
    b = player.play(Card('5','spades'),splitHand)
    print("Passed" + '\n')
    print("Test No. 6: Print Choice")
    print(b)
    print("Passed" + '\n')
    print("Test No. 7: Run player.play w/ Insurance + Print Choice")
    c = player.play(Card('10','diamonds'),baseHand)
    print(c)
    print("Passed" + '\n')
    print("Test No. 8: Run player.play w/ Surrender + Print Choice")
    d = player.play(Card('Ace','hearts'),splitHand)
    print(d)
    print("Passed" + '\n')
    print("Test No. 9: Check is_insured")
    e = player.is_Insured()
    print(e)
    print("Passed" + '\n')
    print("Test No. 10: Check has_surrendered")
    f = player.has_surrendered()
    print(f)
    print("Passed" + '\n')
    print("Test No. 11: Run player.insurance")
    player.insurance(15)
    print("Passed" + '\n')
    print("Test No. 12: Print Player.InsuranceBet")
    print(player.InsuranceBet)
    print("Passed" + '\n')
    print("Test No. 13: Run player.add_hand")
    player.add_hand(splitHand)
    player.add_hand(baseHand)
    print("Passed" + '\n')
    print("Test No. 14: Print Player")
    print(player)
    print("Passed")


