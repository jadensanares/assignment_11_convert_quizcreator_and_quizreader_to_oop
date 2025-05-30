# This is the main controller for making the quiz

# Import the Question Class
# Import the file handler Class
from question import Question
from quiz_file_handler import QuizFileHandler

class QuizCreator:
    def __init__(self):
        # Initializing an empty list in able to styore the question objects
        self.questions = []

    def create_question(self):
        # Asking the user for the quiz question
        question_text = input("Enter the question: ")

        # Create a dictionary to hold the 4 answer choices (a, b, c, d)
        choices = {}
        for letter in ["a", "b", "c", "d"]:
            answer = input(f"Enter the answer for {letter}: ")
            choices[letter] = answer

        # Validating the correct answer input (needs to be from a-d)
        while True:
            correct_answer = input("Enter the correct answer ( a, b ,c , or d): ").lower()
            if correct_answer in ["a", "b", "c", "d"]:
                break
            else:
                print("Invalid choice. Enter only the letters a, b, c, or d.")
            
        # Returning a question object using gathered input
        return Question(question_text, choices, correct_answer)