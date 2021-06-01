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
#split - if the player has two cards of the same value, they can split it in two hands, doubling their bet and playing two hands
#surrender - the player gives up the hand and pays half his bet
#insurance - if the dealer open card is an ace the player can take half of his bet off the table
#if dealer hand totals to less than 17 he has to hit

#basic game flow
#players place bets
#dealer deals cards
#players take their turns
#dealer takes their turn
from random import shuffle

class Dollars(float):
#This class returns a $ with a float
    def __repr__(self):
        return "$ " + super().__repr__()

class Card:
#This class defines values and methods of a card
    def __init__(self, naipe, card_name):
        if card_name in ["Jack", "King", "Queen"]:
            self.value = 10
        elif card_name in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.value = card_name
        else:
            self.value = [1, 11]
        self.card_name = card_name + " of " + naipe
         

class Player:
#This class defines values and methods for a player
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.hand = []
    def print_hand(self):
        print("{}'s hand is: ".format(self.name))
        for card in self.hand:
            print(card.card_name)


class Dealer:
    def __init__(self):
        self.deck = []
        for naipe in ["hearts", "clubs", "spades", "clubs"]:
            for name in ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "King", "Queen"]:
                self.deck.append(Card(naipe, name))
        shuffle(self.deck)

        self.hand = []

    def deal(self, target):
        #remove card from self.deck and put it in target.hand
        target.hand.append(self.deck.pop())
    
    def print_hand_stage1(self):
        print("The Dealer's hand is {}".format(self.hand[0].card_name))
    
    def print_hand_stage2(self):
        print("The Dealer's Hand is: ")
        for card in self.hand:
            print(card.card_name)


class Wallet:
#This class defines values and methods for a wallet
    def __init__(self, amount):
        self.amount = amount

class Table:
    def __init__(self, dealer, players):
        self.players = players
        self.dealer = dealer
    def show_table(self):
        print("Dealer's Hand: " + dealer.hand[0] + )

    


print("BlackJack Terminal Game 1.0")
#Main Game Loop
player1 = Player("John", 100)
dealer = Dealer()

#possible multiple players later
#players = [player1]

finish_game = False
while not finish_game:
    #does player want to continue the game?
    while True:
        wants_to_play = input("Do you want to play a hand of blackjack? (y,n)\n")
        if wants_to_play not in ["y", "n", "Y", "N"]:
            print("Please answer \"y\" or \"n\"")
        elif wants_to_play in ["n", "N"]:
            finish_game = True
            break
        else:
            break
    
    if finish_game == True:
        break
    #dealer deals initial hands on
    for counter in range(2):
        #for player in players:
        dealer.deal(player1)
        dealer.deal(dealer)
    #each player takes their turn    
    dealer.print_hand_stage1()    
    end_turn = False
    while not end_turn:
        player1.print_hand()
        input("What do you want to do? (1: Hit) (2: Stay) (3: Double Down)")

        
    #continue
    