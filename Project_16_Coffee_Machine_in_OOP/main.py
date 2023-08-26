from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Ask the user what they'd like
menu = Menu()
prompt = input(f"What would you like? {menu.get_items()}: ")
print(prompt)
