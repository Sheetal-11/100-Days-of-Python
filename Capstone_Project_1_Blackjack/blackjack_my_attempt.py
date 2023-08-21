# BlackJack/21 game

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

def pick_card():
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def deal_hands(hand):
    
    hand.append(pick_card())
    return hand
      

def play_game():
    
    print("Do you wanna play?")
    play = input("y/n: ").lower()
    
    if play == "y":
        
        #Intialize player's and dealer's cards and scores
        p_cards = []
        d_cards = []
        
        # Deal hands
        for _ in range(2):
            p_cards = deal_hands(p_cards)
            d_cards = deal_hands(d_cards)
        print(f"Your hand = {p_cards}")
        print(f"Dealer's hand = {d_cards}")        
    
    
    elif play == "n":
        print("Have a good day!")
        
    else:
        print("Please choose either 'y' or 'n'\n")
        play_game()


play_game()

