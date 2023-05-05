class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def get_question_prompt(self, current_question):
        return f"Q.{self.question_number}: {current_question.text} (True/False)?: "

    def check_answer(self, answer, correct_answer):
        is_answer_correct = answer.lower() == correct_answer.lower()

        if not is_answer_correct:
            print('That\'s wrong.')
        else:
            print('You got it right!')
            self.score += 1

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score: {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(self.get_question_prompt(current_question))
        self.check_answer(answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)
