from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

i = 0

question_bank = []
while i < 12: 
    question = Question(question_data[i]["text"], question_data[i]["answer"]) 
    question_bank.append(question)
    i += 1

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question() 

print(f"your final score is: {quiz_brain.score}/{quiz_brain.question_number}")    
      








