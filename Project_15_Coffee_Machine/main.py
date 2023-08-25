MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """
    Prints the current status of resources
    """
    for resource in resources:
        print(f"{resource.title()} : {resources[resource]}ml")
    print(f"Money : ${'{:.2f}'.format(money)}")


def suitable_format(letter):
    """
    If a user inputs the initial letter of coffee, it returns the full word that is the suitable format
    """
    if letter == "e":
        return "espresso"
    elif letter == "l":
        return "latte"
    else:
        return "cappuccino"


def check_resources(coffee_type):
    """
    Takes coffee type as input and returns a boolean based on the availability of the resources
    :param coffee_type: str
    :return: bool
    """
    for resource in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
        else:
            return True


def insert_coins():
    """
    Lets the user insert coins and returns the total money inserted
    :return: total
    """
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total


def is_success(coffee, price):
    if price < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if price > MENU[coffee]["cost"]:
            change = price - MENU[coffee]["cost"]
            print(f"Here is ${'{:.2f}'.format(change)} dollars in change.")
            return True


def update_stock(stock, coffee):
    """
    Takes in resources (dict) and coffee (str) and based on the coffee type,
    it deducts the ingredient quantities and returns the updated resources
    :param stock: dict : current resources
    :param coffee: str : coffee type
    :return: dict : updated resources
    """
    for element in stock:
        if element in MENU[coffee]["ingredients"]:
            stock[element] -= MENU[coffee]["ingredients"][element]
    return stock


money = 0
turn_off = False

while not turn_off:

    # Take user input
    print("\nWhat would you like? (espresso/latte/cappuccino)")
    print("You can optionally type \n'E' for Espresso,\n'L' for Latte,\n'C' for Cappuccino")
    prompt = input("Please enter: ").lower()

    if prompt in ["espresso", "latte", "cappuccino", "e", "l", "c"]:

        # if the user input only the initial letter, convert it into a suitable format
        if prompt in ["e", "l", "c"]:
            prompt = suitable_format(prompt)

        # checks whether the resources are sufficient
        is_sufficient = check_resources(prompt)
        if is_sufficient:
            amount = round(insert_coins(), 2)
            # Check whether the transaction was successful
            tr_pass = is_success(prompt, amount)
            if tr_pass:
                resources = update_stock(resources, prompt)
                money += MENU[prompt]["cost"]
                report()

        else:
            print("If you'd like please select something else")

    elif prompt == "report":
        report()
    elif prompt == "off":
        turn_off = True
    else:
        print("Please enter a valid input.")


# todo 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the user selected,
# then the ingredients to make the drink should be deducted from the coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
# If latte was their choice of drink.
