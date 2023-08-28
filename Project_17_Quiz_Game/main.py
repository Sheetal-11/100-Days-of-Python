from question_model import Question
from data import question_data

question_bank = []

for entry in question_data:
    question = entry["text"]
    answer = entry["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)
