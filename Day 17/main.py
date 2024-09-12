from data import question_data
from question_model import Question
from quiz_brain import QuizBrain



question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']

    question_list = Question(text, answer)
    question_bank.append(question_list)

quiz = QuizBrain(question_bank)
while quiz.check_questions_remaining:
    quiz.continue_game()
