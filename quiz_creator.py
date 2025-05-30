# Import the Question class to create quiz question objects
# Import QuizFileHandler to handle saving to file
from question import Question
from quiz_file_handler import QuizFileHandler


# Handles user interaction for creating quiz questions
class QuizCreator:
    def __init__(self):
        # Initialize an empty list to store all created Question objects
        self.question_list = []

    def create_question(self):
        # Ask user for the quiz question text
        question_text = input("Enter the question: ")

        # Create a dictionary to store letter choices (A, B, C, D) and their corresponding answers
        choices_dictionary = {}
        for letter in ['a', 'b', 'c', 'd']:
            answer_text = input(f"Enter the answer for {letter}: ")
            choices_dictionary[letter] = answer_text

        # Ask the user to input the correct letter answer, validate input
        while True:
            correct_answer = input("Enter the correct answer (a, b, c, or d): ").lower()
            if correct_answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Invalid choice. Enter only the letters a, b, c, or d.")

        # Display feedback with color green and red emojis
        print("Question feedback:")
        for letter, answer_text in choices_dictionary.items():
            if letter == correct_answer:
                print(letter + ": " + answer_text + " 🟩")
            else:
                print(letter + ": " + answer_text + " 🟥")

        # Return a Question object created from the user inputs
        return Question(question_text, choices_dictionary, correct_answer)

    def run(self):
        # Display welcome message
        print("Hello User, welcome to this Quiz Creator!")

        while True:
            # Call method to create a new question
            new_question = self.create_question()
            # Add the newly created question to the list
            self.question_list.append(new_question)

            # Ask user if they want to add another question
            another_question = input("Would you like to add another question? Type either (yes) or (no): ").lower()
            if another_question != "yes":
                break

        # Save all collected questions to a file using the file handler class
        QuizFileHandler.save_questions(self.question_list)
        print("\nThank you for making the quiz! ^-^")


# Run the program only if this file is executed directly
if __name__ == "__main__":
    quiz_creator_instance = QuizCreator()
    quiz_creator_instance.run()
