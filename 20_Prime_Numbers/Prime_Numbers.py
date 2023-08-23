#Exercise: Check whether a given number is prime or not.

def prime_checker(number):
    
    if number == 1:
        print(f"{number} is neither a prime nor a composite number.")
    
    else:
        divisible = False
        for i in range(2, number):
            if number % i == 0:
                divisible = True
                break
        
        if divisible:
            print(f"{number} is not a prime number.")
        else:
            print(f"{number} is a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
    
    