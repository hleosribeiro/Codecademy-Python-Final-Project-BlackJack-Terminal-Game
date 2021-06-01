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


class Dollars(float):
#This class returns a $ with a float
    def __repr__(self):
        return "$ " + super().__repr__()

print("BlackJack Terminal Game 1.0")
#Main Game Loop
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
                
    #continue
    #stop
        finish_game = True