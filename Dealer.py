from Player import Player

class Dealer(Player):
    def __init__(self):
        super(Dealer, self).__init__(name='Dealer', money=9999)
        self.table = None

    def sit(self, table):
        """Adds the dealer to the table"""
        self.table = table

    def add_hand(self, hand):
        """gives the dealer their hand"""
        self.hands = hand

    def show_card(self):
        """Displays the Dealer's first card"""
        return self.hands.show(0)

    def restock(self):
        """Restocks the Dealer's money to allow continuous play"""
        self.money = 9999
