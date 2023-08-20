# Calculator

import calculator_art

#Addition
def add(n1, n2):
    return n1 + n2

#Subtraction
def subtract(n1, n2):
    return n1 - n2

#Multiplication
def multiply(n1, n2):
    return n1 * n2

#Division
def division(n1, n2):
    return n1 / n2


operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : division,
        }


def calculator():
    
    num1 = int( input("What's the first number?: "))
    
    end_calculation = False
    
    while not end_calculation:
        
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num_2 = int( input("What's the next number?: "))
            
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num_2)
    
        print(f"{num1} {operation_symbol} {num_2} = {answer}")
            
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        
        if should_continue == 'y':
            num1 = answer
            
        if should_continue == 'n':
            end_calculation = True
            calculator()

calculator()





