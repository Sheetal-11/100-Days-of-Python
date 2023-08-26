from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off = False

while not turn_off:

    # Ask the user what they'd like
    menu = Menu()
    prompt = input(f"What would you like? {menu.get_items()}: ")
    print(prompt)

    if prompt == "off":
        turn_off = True
