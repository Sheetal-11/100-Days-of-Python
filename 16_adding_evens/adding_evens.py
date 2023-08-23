#Exercise: Write a program that calculates the sum of all the even numbers from 1 to 100.

sum = 0

for i in range(2, 101, 2):
    sum += i
    
print(f"Sum of all even numbers from 1 to 100 is {sum}.")

