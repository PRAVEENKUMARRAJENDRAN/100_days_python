class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_no = 0
        self.quiz_list = question_list

    def check_questions_remaining(self):
        return self.question_no < len(self.quiz_list)

    def continue_game(self):
        current_question = self.quiz_list[self.question_no]
        self.question_no += 1
        answer = input(f'Q{self.question_no} {current_question.text} True/False: ')
        self.check_answer(current_question.answer, answer)

    def check_answer(self, quiz_answer, your_answer):
        if quiz_answer == your_answer:
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong.")
            print(f"The correct answer was: {quiz_answer}.")
            print(f"Your current score is: {self.score}/{self.question_no}")
            return

