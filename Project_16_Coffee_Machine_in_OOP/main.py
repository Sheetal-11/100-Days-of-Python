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
        # Searches the menu for a particular drink by name.
        # Returns a MenuItem object if it exists, otherwise returns None.
        coffee = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(coffee):
            print(money_machine.make_payment(coffee.cost))
            print("meaning payment is successful")

    else:
        print("Please enter a valid option.")
