#Exercise: Write a program that calculates the highest score from a List of scores.

students_scores = input("Enter the scores of the students separated by space:\n").split()

for i in range( len(students_scores)):
    students_scores[i] = int(students_scores[i])

highest_score = 0

for score in students_scores:
    if highest_score < score:
        highest_score = score
        
print(f"The highest score in the class is {highest_score}")
    
    