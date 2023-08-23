#Exercise: Write a program that automatically prints the solution to the FizzBuzz game.


for i in range(1, 101):
    
    if i % 15 == 0:
        print("FizzBuzz")
        
    elif i % 3 == 0:
        print("Fizz")
        
    elif i % 5 == 0:
        print("Buzz")
        
    else:
        print(i)

