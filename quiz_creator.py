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
        
    def display_feedback(self, question): 
        # Show visual feedback with green/red emojies for the correct/incorrect options
        print("Question Feedback:")
        for choice, answer in question.choices.items():
            if choice == question.correct_answer:
                print(choice + ": " + answer + " 🟩")
            else:
                print(choice + ": " + answer + " 🟥")
    
    def run(self):
        # Wwelcome message to the user
        print("Hello User, welcome to this Quiz Creator!")

        while True:
            questions = self.creat_question()
            self.questions.append(question)

            # Display of emoji-based answer feedback
            self.display_feedback(question)

            # Ask if the user wants to create another questions
            another = input("Would you like to add another question? Type either (yes) or (no): ").lower()
            if another != "yes":
                break
    
        # Save all created quesitons to file using the helper class
        QuizFileHandler.save_questions(self.questions)

        # Thank you message to end the program
        print("\nThank you for making the quiz! ^-^")

# Entry Point
if __name__ == "__main__":
    creator = QuizCreator()
    creator.run
    