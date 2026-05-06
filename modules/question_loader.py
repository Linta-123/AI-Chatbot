import json
import random

def load_questions(role):
    if role == "Python Developer":
        file_path = "data/python_questions.json"
    elif role == "Java Developer":
        file_path = "data/java_questions.json"
    else:
        file_path = "data/hr_questions.json"

    with open(file_path, "r") as file:
        questions = json.load(file)

    return random.choice(questions)