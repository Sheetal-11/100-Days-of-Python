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


def score(hand):
    '''
    returns the sum of all the values in a given hand
    
    '''
    sum = 0
    for element in hand:
        sum += element
    return sum


def case_11(given_hand):
    
    # print("caee_11")
    # print(f"Before : {given_hand}")
    
    if 11 in given_hand:
        total = score(given_hand)
        if total > 21:
            for i in range(len(given_hand)):
                if given_hand[i] == 11:
                    given_hand[i] = 1
                    break
    # print(f"After : {given_hand}")
    return given_hand

        
def deal_hands(hand):
    
    hand.append(pick_card())
    hand = case_11(hand)
    sum = score(hand)
    return hand, sum


def should_continue():
    '''
    Ask the user to hit or to stand
    '''
    prompt = input("Do you want to 'hit' or 'stand'?: ").lower()
    print('____________________________________________')
    
    if prompt == "hit":
        choice = False
    elif prompt == "stand":
        choice = True
    else:
        print("Please type either 'hit' or 'stand'\n")
        choice = should_continue()
    return choice


def declare_winner(player_total, dealer_total, dealer_cards):
    
    dealer_cards, dealer_total = deal_hands(dealer_cards)
    print(f"\nDealer's hand = {dealer_cards} \t Dealer's score = {dealer_total}")
    
    if player_total > 21:
        print("You lose!")
    elif player_total == 21 and dealer_total < 21:
        print("Yay! You win!")
          
    else:
        while dealer_total < 17:
            print("Dealer is taking another card..")
            dealer_cards, dealer_total = deal_hands(dealer_cards)
            print(f"Dealer's hand = {dealer_cards} \t Dealer's score = {dealer_total}")
        
        print('____________________________________________')
        print(f"\nYour score: {player_total} \t Dealer's score: {dealer_total}\n")
        if dealer_total > 21:
            print("Yay! You win!")
        else:
            if player_total > dealer_total:
                print("Yay! You win!")
            elif player_total == dealer_total:
                print("Draw")
            else:
                print("You lose!")
            
    

def game_start():
    
    print("\n\n")
    print("Welcome to the Blackjack game!")
        
    #Intialize player's and dealer's cards
    p_cards = []
    d_cards = []
    
    # Deal hands and calculate scores
    for _ in range(2):
        p_cards, p_score = deal_hands(p_cards)
    d_cards, d_score = deal_hands(d_cards)
    print(f"\nYour hand = {p_cards} \t Your score = {p_score}")
    print(f"Dealer's hand = {d_cards} \t Dealer's score = {d_score}\n")
    
    #If player scores a natural
    if p_score == 21:
        declare_winner(p_score, d_score, d_cards)
    
    #A flag that tells if the player wants to stand or not
    stand = should_continue()
    
    while not stand:
        #while the player selects hit
        p_cards, p_score = deal_hands(p_cards)
        print(f"\n\nYour hand = {p_cards} \t Your score = {p_score}")
        print(f"Dealer's hand = {d_cards} \t Dealer's score = {d_score}\n")
        if p_score >= 21:
            declare_winner(p_score, d_score, d_cards)
            return
        else:
            stand = should_continue()
    
    declare_winner(p_score, d_score, d_cards)


def play_game():
    
    end_of_game = False
    
    while not end_of_game:
        print("\nDo you want to play Blackjack?")
        play = input("y/n: ").lower()
        
        if play == "y":
            game_start()
        elif play == "n":
            end_of_game = True
            print("Have a good day!")
        else:
            print("Please type either 'y' or 'n'\n")

play_game()
            

