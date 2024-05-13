from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []
for Q in question_data:
    question_bank.append(Question(Q["question"], Q["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()


print("\n"+"-"*40)
print("you've completed the quiz")
print(f"you final score was {quiz.score}/{quiz.question_number}")

