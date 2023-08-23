#Blind Auction

# from replit import clear
import art_blind_auction
from os import system as sys

def greet_and_take_inputs():
    # print("\x1B[2J")  # An alternate way to clear screen
    sys('cls')
    print(art_blind_auction.logo)
    print("Welcome to the secret auction program.")
    person_name = input("What is your name? ")
    bid_price = int(input("What's your bid? $"))
    return person_name, bid_price

def declare_winner(auction_data):
    # print("\x1B[2J")
    sys('cls')
    highest_bid = 0
    for winner in auction_data:
        if auction_data[winner] > highest_bid:
            winner_name = winner
            highest_bid = auction_data[winner]
    print(f"The winner is {winner_name} with a bid of ${highest_bid}")
    

def to_continue():
    repeat = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if repeat == "no":
        end = True
    elif repeat == "yes":
        end = False
    else:
        print("Please choose a valid answer.")
        end = to_continue()
    return end
        

auction = {}

end_auction = False

while not end_auction:
    name, bid = greet_and_take_inputs()
    auction[name] = bid
    
    repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    end_auction = to_continue()

for entry in auction:
    print(f"{entry} : {auction[entry]}")
    
declare_winner(acution)