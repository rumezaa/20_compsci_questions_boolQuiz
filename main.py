import json
from gui import*
from quiz_methods import*
import requests

r = requests.get("https://opentdb.com/api.php?amount=20&category=18&type=boolean")
r = r.json()

with open("data.json", "w") as file:
    json.dump(r,file,indent=4)
with open('data.json') as file:
    data=json.load(file)
    data = data["results"]


#format questions
q_list = []
for q in data:
    q_question = [q["question"] for i in data]
    q_answer = [q["correct_answer"] for i in data]
    q_dict = dict(zip(q_question,q_answer))
    q_list.append(q_dict)



quiz = Quizsetup(q_list)
quiz_interface = QuizGUI(quiz)









