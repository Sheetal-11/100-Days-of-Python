# Rock Paper Scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
names = ['Rock', 'Paper', 'Scissors']

def main():

    def trophy():
        print('''
                ___________
               '._==_==_=_.'
               .-\:      /-.
              | (|:.     |) |
               '-|:.     |-'
                 \::.    /
                  '::. .'
                    ) (
                  _.' '._
                 `"""""""`
              ''')
    
    def skull():
        
        print('''
         _.--""--._
        /  _    _  \\
     _  ( (_\  /_) )  _
    { \._\   /\   /_./ }
    /_"=-.}______{.-="_\\
     _  _.=("""")=._  _
    (_'"_.-"`~~`"-._"'_)
     {_"            "_}
          ''')

    
    def pick():
        
        print("What do you choose? Type:")
        player = int( input("0 for Rock, \n1 for Paper \n2 for Scissors\n"))
        comp = random.randrange(len(options))
        return player, comp
        
    player, comp = pick()
    
    if player in [0, 1, 2]:   
        
        print(f'You: {names[player]} {options[player]}')
        print(f'Computer: {names[comp]} {options[comp]}')
        
        if player == comp:
            print("Oops! it's a tie! please try again.\n")
            main()
        
        elif (player==0 and comp==1) or (player==1 and comp==2) or (player==2 and comp==0):
            print("You lose")
            skull()
            
        else:
            print("Yay! You win!")
            trophy()
    
    else:
        
        print("Please enter a valid choice.")

main()