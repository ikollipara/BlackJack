from Table import Table
from Player import Player
from Dealer import Dealer
from getFunctions import *

def main():
    dealer = Dealer()
    table = Table(dealer)
    table.introduction()
    numberOfPlayers = get_integer("Please enter the number of Players: ")
    for _ in range(1, int(numberOfPlayers)+1):
        name = input("Please input Player {}'s Name: ".format(_))
        player = Player(name)
        player.sit(table)
    dealer.sit(table)
    while len(table.Players) > 0:
        table.take_bets()
        table.deal()
        table.play_round()
        table.payout()
        dealer.restock()
    table.outro()

main()