# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 16:21:27 2023

@author: sheet
"""
#Exercise Treasure Map: Write a program which will mark a spot with an X.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("\nWhere do you want to put the treasure? ")

col = int( position[0]) - 1
row = int( position[1]) - 1

map[row][col] = 'X'

print(f"\n{row1}\n{row2}\n{row3}")

