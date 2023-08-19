#Exercise: write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights: ").split()

for i in range( len(student_heights)):
    student_heights[i] = int( student_heights[i])

sum = 0
n = 0

for element in student_heights:
    sum += element
    n += 1

average = sum / n
average = round(average)

print(f"The average student height = {average}")


