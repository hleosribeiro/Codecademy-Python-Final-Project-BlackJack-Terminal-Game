#defining general tasks to be completed
#how blackjack works
#goal: having a hand that totals higher than the dealers without going over 21
#if a player hand totals higher than 21, he busts and loses his bet
#game flow
#the dealer deals 1 open card to everyone, including himself
#the dealer then deals another open card to everyone but himself, then deals a closed card to himself
#if a player hits a blackjack on opening hand they are awarded 1.5 times their bet(if they bet 1 they get 2.5 in return)
#each player(in the case of this game, only 1), in their turn, going counter-clockwise from the dealer(if there are more than 2 players)
#can decide to do one of each actions:
#hit - the player asks for another card
#stay - the player ends their turn
#double down - doubles their bet, a hit and a stay.

#basic game flow
#players place bets
#dealer deals cards
#players take their turns
#dealer takes their turn
from random import shuffle
from itertools import product as comblista
from os import system
from time import sleep


def print_divider():
    print("------------------------------------------------------------")
    print("♣♤♥♦  ♣♤♥♦  ♣♤♥♦  ♣♤♥♦  ♣♤♥♦  ♣♤♥♦  ♣♤♥♦  ♣♤♥♦  ♣♤♥♦  ♣♤♥♦")
    print("------------------------------------------------------------")

def clear():
    _ = system('cls')
    return _

class Hand:
    def __init__(self):
        self.cards_in_hand = []
    
    #method to get the value of the cards in hand
    def get_hand_value(self):
        possible_values = []
        possible_ace_values = []
        for card in self.cards_in_hand:
            if type(card.value) is not list:
                possible_values.append(card.value)
            else:
                possible_ace_values.append(card.value)
        
        possible_values = sum(possible_values)
        possible_ace_values = list(comblista(*possible_ace_values)) 
        possible_final_values = []
        for each in possible_ace_values:            
            possible_final_values.append(sum(each) + possible_values)
        current_answer = 0
        for each in possible_final_values:
            if each > current_answer and  each <= 21:
                current_answer = each
        if current_answer == 0:            
            return min(possible_final_values)
        else:
            return current_answer 

class Card:
#This class defines values and methods of a card
    def __init__(self, naipe, card_name):
        if card_name in ["Jack", "King", "Queen"]:
            self.value = 10
        elif card_name in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.value = card_name
        else:
            self.value = [1, 11]
        self.card_name = str(card_name) + " of " + naipe
    
    def __repr__(self):
        return self.card_name
         

class Player:
#This class defines values and methods for a player
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.hand = Hand()
    def print_hand(self):        
        print("{}'s hand is: ".format(self.name))
        for card in self.hand.cards_in_hand:
            print(card.card_name)
        print_divider()

class Dealer():
    def __init__(self):
        self.deck = []
        for naipe in ["hearts", "clubs", "spades", "clubs"]:
            for name in ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "King", "Queen"]:
                self.deck.append(Card(naipe, name))
        shuffle(self.deck)
        self.hand = Hand()

    def deal(self, target):
        #remove card from self.deck and put it in target.hand
        target.hand.cards_in_hand.append(self.deck.pop())
    
    #prints the dealers hand before his turn
    def print_hand_stage1(self):        
        print("The Dealer's hand is: \n{}".format(self.hand.cards_in_hand[0].card_name))
        print_divider()
    
    #prints the dealers hand normally
    def print_hand(self):        
        print("The Dealer's Hand is: ")
        for card in self.hand.cards_in_hand:
            print(card.card_name)
        print_divider()


class Wallet:
#This class defines values and methods for a wallet
    def __init__(self, amount):
        self.amount = amount

#header
clear()   
print_divider()
print("BlackJack Terminal Game 1.0")
print_divider()

#Main Game Loop
player_name = input("What is the player's name? \n")
print("{}'s wallet has $100".format(player_name))
player1 = Player(player_name, 100)
current_bet = 0

finish_game = False
while not finish_game:
    #does player want to continue the game?
    while True:

        wants_to_play = input("Do you want to play a hand of blackjack? (y,n)\n")
        clear()
        if wants_to_play not in ["y", "n", "Y", "N"]:
            print("Please answer \"y\" or \"n\"")
        elif wants_to_play in ["n", "N"]:
            finish_game = True
            break
        else:
            
            player1.hand = Hand()
            player1.wallet += current_bet
            current_bet = 0
            dealer = Dealer()

            while True:
                clear()
                pot = float(input("Enter bet (current funds: {}): \n".format(player1.wallet)))
                if pot <= player1.wallet:
                    player1.wallet -= pot
                    break                    

            print_divider()
            break
    
    if finish_game == True:
        break

    #dealer deals initial hands on
    for counter in range(2):        
        dealer.deal(player1)
        dealer.deal(dealer)
    
    #each player takes their turn 
    dealer.print_hand_stage1()
    busted = False
    blackjack = False
    end_turn = False
    while not end_turn:
        #check for blackjack
        if player1.hand.get_hand_value() == 21:
            print("BlackJack!")
            print_divider()
            blackjack = True
            end_turn = True
        #check for bust
        elif player1.hand.get_hand_value() > 21:            
            player1.print_hand()
            busted = True
            print("Busted!")
            print_divider()
            end_turn = True
        #continue playing
        else:
            player1.print_hand()                  
            decision = input("What do you want to do? (1: Hit) (2: Stay) (3: Double Down)\n")
            clear()
            if decision == "1":
                print("{} hits".format(player1.name))
                dealer.deal(player1)
                print("{} drew the {}".format(player1.name, player1.hand.cards_in_hand[-1]))
                sleep(1)            
            elif decision == "2":
                print("{} stays".format(player1.name))
                sleep(1)
                end_turn = True
            elif decision == "3":
                if player1.wallet < pot:
                    print("You can't double down(insufficient funds)")
                else:
                    player1.wallet -= pot
                    pot *= 2
                    print("Remaining Funds: {} \n New bet: {}".format(player1.wallet, pot))
                    input("")                
            # elif decision == "4":
            #     print("Not implemented yet")
            # elif decision == "5":
            #     print("Not Implemented Yet")
            # elif decision == "6":
            #     print("Not Implemented yet")
            else:
                print("Try again")
    
    
    
    while dealer.hand.get_hand_value() < 17 and not busted and not blackjack:
        print("The dealer will now draw")
        sleep(1)
        dealer.deal(dealer)
        print("The dealer drew the {}".format(dealer.hand.cards_in_hand[-1]))
        sleep(1)
        
    dealer_hand_value = dealer.hand.get_hand_value()
    player1_hand_value = player1.hand.get_hand_value()

    if busted:        
        print("Dealer wins")
        input("Press Any Key to Continue")
    elif blackjack:
        current_bet = pot * 2.5
        print("{} wins!".format(player1.name))
        
    elif dealer_hand_value > 21 or dealer_hand_value < player1_hand_value:
        current_bet = pot * 2        
        print("Dealer hand value is {} \n {} hand value is {}".format(dealer.hand.get_hand_value(), player1.name, player1.hand.get_hand_value()))
        print("{} wins the hand!".format(player1.name))        
        input("Press Any Key to Continue")  

    elif dealer_hand_value == player1_hand_value:
        current_bet = pot        
        print("Dealer hand value is {} \n {} hand value is {}".format(dealer.hand.get_hand_value(), player1.name, player1.hand.get_hand_value()))
        print("It's a draw!")
        input("Press Any Key to Continue")
        
    elif dealer_hand_value > player1_hand_value:        
        print("Dealer hand value is {} \n {} hand value is {}".format(dealer.hand.get_hand_value(), player1.name, player1.hand.get_hand_value()))
        print("Dealer wins")
        input("Press Any Key to Continue")
        
    