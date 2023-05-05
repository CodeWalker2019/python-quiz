from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def create_question(q):
    return Question(q['text'], q['answer'])


question_bank = list(map(create_question, question_data))
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()
