from Shoe import Shoe
from Hand import Hand
from getFunctions import *
from RulesError import RulesError


class Table(object):
    def __init__(self, dealer, numberOfDecks=6):
        self.shoe = Shoe('CardList', numberOfDecks)
        self.dealer = dealer
        self.Players = []
        self.Bets = []

    def shuffle(self):
        """Shuffles the Shoe"""
        self.shoe.shuffle()

    def take_bets(self):
        """Takes all the player bets and adds them to the self.Bets list"""
        self.Bets = []
        removePlayers = []
        for player in self.Players:
            print("""
Name:   {}
Money: ${}""".format(player.name, player.money))
            player.clear_hands()
            bet = player.bet_or_leave()
            if bet == None:
                removePlayers.append(player)
            else:
                self.Bets.append(int(bet))
                player.rake_out(int(bet))
        if len(removePlayers) > 0:
            for player in removePlayers:
                self.Players.remove(player)

    def deal(self):
        """Deals to all active players. Skips players who bet 0"""
        counter = 0
        #
        # The While loop is used as the bets are needed for a hand, but are gotten earlier
        #
        while counter < len(self.Players):
            if self.Bets[counter] == 0:
                pass
            else:
                self.shuffle()
                card = self.shoe.draw()
                cardTwo = self.shoe.draw()
                player = self.Players[counter]
                player.add_hand(Hand(card, cardTwo, self.Bets[counter]))

            counter += 1
        card = self.shoe.draw()
        cardTwo = self.shoe.draw()
        self.dealer.add_hand(Hand(card, cardTwo, 0))


    def play_round(self):
        """Plays the Round. Runs through each player's hands, followed by the next player"""
        #
        # Runs a loop for each player
        #
        for player in self.Players:
            #
            # Skips players who sat out this round
            #
            if len(player.hands) == 0:
                pass
            else:
                #
                # Runs a loop for every hand
                #
                for hand in player.hands:
                    while hand.can_hit():
                            command = player.play(self.dealer.show_card(), hand)
                            if command in ['hit','h']:
                                card = self.shoe.draw()
                                hand.hit(card)
                            elif command in ['stand', 's']:
                                hand.stand()
                            elif command in ['double down', 'd']:
                                addBet = hand.bet
                                while int(addBet) > hand.bet/2:
                                    addBet = get_integer("Please enter your additional bet: ")
                                card = self.shoe.draw()
                                hand.double_down(card, int(addBet))
                            elif command in ['split', 'p']:
                                if not hand.can_split():
                                    raise RulesError("Cannot Split this hand")
                                else:
                                    #
                                    # Runs thru all the stuff needed for a complete split
                                    #
                                    newHand = hand.split()
                                    card = self.shoe.draw()
                                    player.add_hand(Hand(newHand, card, hand.bet))
                                    player.rake_out(hand.bet)
                                    newCard = self.shoe.draw()
                                    hand.hit(newCard)
                            elif command in ['insurance','i']:
                                if not player.is_Insured():
                                    sideBet = hand.bet + 1
                                    while sideBet > hand.bet:
                                        sideBet = get_integer("Please enter your side bet: ")
                                    player.insurance(int(sideBet))
                    if hand.is_busted():
                        print("{} Busted!".format(player.name))
        #
        # This is the dealer's "play" method. It was too basic to be its own thing, at least in my opinion
        #
        while self.dealer.hands.hard < 17:
            card = self.shoe.draw()
            self.dealer.hands.hit(card)
            if self.dealer.hands.is_busted():
                print("Dealer Busts!")
        if not self.dealer.hands.is_busted():
            print("Dealer has {}".format(self.dealer.hands.hard))

    def payout(self):
        """Pays out the bets and earnings"""
        for player in self.Players:
            if len(player.hands) == 0:
                pass
            elif player.is_Insured():
                #
                # Pays out insurance first
                #
                if self.dealer.hands.is_blackjack():
                    player.rake_in(player.InsuranceBet*2)
                    print("{} won {} by Insurance".format(player.name, player.InsuranceBet*2))
            else:
                for hand in player.hands:
                    #
                    # Handles all the math associated with a winning bet,a nd rounds to the nearest int
                    #
                    if hand.is_blackjack():
                        bet = hand.bet * 3
                        bet = bet / 2
                        bet = round(bet, 1)
                        bet = hand.bet + bet
                        player.rake_in(bet)
                        print("{} has Black Jack!".format(player.name))
                        print("{} has won {}!".format(player.name, bet))
                    elif self.dealer.hands.is_busted():
                        bet = hand.bet*2
                        bet = bet + hand.bet
                        player.rake_in(bet)
                    else:
                        if 21 > hand.value() > self.dealer.hands.value():
                            bet = hand.bet*2
                            bet = round(bet, 1)
                            bet = bet + hand.bet
                            player.rake_in(bet)
                            print("{} won {}!".format(player.name, bet))
                        elif hand.value() == self.dealer.hands.value():
                            print("{} Pushed!".format(player.name))
                            player.rake_in(hand.bet)
                        else:
                            print("{} lost ${}".format(player.name, hand.bet))
                            self.dealer.rake_in(hand.bet)

            if player.money <= 0:
                self.Players.remove(player)
                print("{} ran out of money, and blacked out!".format(player.name))
    def introduction(self):
        print("""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
============================================================================""")
        instructions = get_yes_no("Do you want to see instructions? ")
        if instructions == 'yes':
            print("""
--------Instructions-------
In this game you play 
BlackJack, the Card Game.
You keep playing until you 
either run out of money, or
choose to leave. Have Fun!
""")

    def outro(self):
            print("""
Created By: Ian Kollipara
    
Thank you for playing...
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
""")