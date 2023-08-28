class QuizBrain:

    def __init__(self, q_list):
        """
        Takes a list of questions as an argument
        :param q_list: list
        """
        self.question_number = 0
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
        input(question_string + "(True/False)?: ")
