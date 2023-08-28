class QuizBrain:

    def __init__(self, q_list):
        """
        Takes a list of questions as an argument
        :param q_list: list
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """
        Checks if there are more questions to be asked
        :return: boolean
        """
        total_questions = len(self.question_list)
        return self.question_number < total_questions

    def next_question(self):
        """
        Asks the next question from the list of questions
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_string = f"Q{self.question_number}. {current_question.text} "
        user_answer = input(question_string + "(True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
