# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:41:46 2023

@author: sheet
"""


print("Welcome to Treasure Island.")
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
      ''')
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


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

def treasure():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')





direction = input("You're at a crossroad. Where do you want to go? \nType \"left\" or \"right\"\n").casefold()

if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n").casefold()
    
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        color = input("Which colour do you choose?\n").casefold()
        
        if color == "yellow":
            print("You found the treasure! You Win!")
            treasure()
        
        elif color == "blue":
            print("You enter a room of beasts. They eat you! \nGame Over.")
            skull()
            
        elif color == "red":
            print("It's a room full of fire. You got burned! \nGame Over.")
            skull()
        
        else:
            print("You chose a door that doesn't exist. Game Over.")
            skull()

        
    elif action == "swim":
        print("You get attacked by an angry trout. Game Over.")
        skull()

    
    else:
        print("Wrong answer! \nGame over.")
        skull()

elif direction == "right":
    print("You fell into a hole. \nGame Over.")
    skull()

else:
    print("Wrong answer! \nGame over.")
    skull()




