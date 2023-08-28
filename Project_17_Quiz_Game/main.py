from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for entry in question_data:
    # Add all the entries in question_data to a list question_bank as an instance of Question class
    question = entry["text"]
    answer = entry["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
