# Class for a Question

class Question:
    def __init__(self, question_text, choices, correct_answer):
        self.question_text = question_text
        self.choices = choices
        self.correct = correct_answer
    
    