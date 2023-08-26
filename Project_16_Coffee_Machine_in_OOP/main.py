from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
turn_off = False

while not turn_off:

    # Ask the user what they'd like
    prompt = input(f"What would you like? ({menu.get_items()}): ")

    if prompt == "report":
        coffee_maker.report()
        money_machine.report()

    elif prompt == "off":
        turn_off = True

    elif prompt in ["espresso", "latte", "cappuccino"]:
        coffee = menu.find_drink(prompt)
        print("coffee = ", coffee)
        print("coffee.name = ", coffee.name)
        print("coffee.cost = ", coffee.cost)
        print("coffee.ingredients = ", coffee.ingredients)

    else:
        print("Please enter a valid option.")
