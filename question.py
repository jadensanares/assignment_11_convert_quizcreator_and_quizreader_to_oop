# Class for a Question

class Question:
    def __init__(self, question_text, choices_dictionary, correct_letter_answer):
        self.question_text = question_text
        self.choices = choices_dictionary
        self.correct = correct_letter_answer
    
    def display(self):
        print("\n" + self.question_text)
        for key in sorted(self.choices):
            print(f"{key}: {self.choices[key]}")

    def check_answer(self, user_answer):
        return user_answer == self.correct