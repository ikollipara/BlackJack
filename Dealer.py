from Player import Player

class Dealer(Player):
    def __init__(self):
        super(Dealer, self).__init__(name='Dealer', money=9999)
        self.table = None

    def sit(self, table):
        self.table = table

    def add_hand(self, hand):
        self.hands = hand

    def show_card(self):
        return self.hands.show(0)

    def restock(self):
        self.money = 9999
