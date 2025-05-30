import random
import time
from colorama import Fore, Style, init
from question import Question

init(autoreset=True)  # Automatically reset color after each print

class QuizGame:
    def __init__(self, filename="created_quiz_questions.txt"):
        self.filename = filename
        self.questions = []
        self.score = 0

    def load_questions(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            line_index = 0
            while line_index < len(lines):
                line = lines[line_index].strip()
                if line == "":
                    line_index += 1
                    continue
                question_text = line
                choices = {}
                for i in range(1, 5):
                    key, value = lines[line_index + i].strip().split(": ")
                    choices[key.lower()] = value
                correct_line = lines[line_index + 5].strip()
                correct_answer = correct_line.split(": ")[1].lower()
                question = Question(question_text, choices, correct_answer)
                self.questions.append(question)
                line_index += 7
        except FileNotFoundError:
            print(Fore.RED + " ⚠️ CAUTION⚠️ Cannot locate the file. Please type in an existing filename and check if it is correct.")
        except Exception as e:
            print(Fore.RED + f"Error loading questions: {e}")

    def start_quiz(self):
        print(Fore.CYAN + "🧐 Welcome to this short Math Quiz Game! Let's test your problem solving skills!")
        time.sleep(1)
        print(Fore.CYAN + "Let's test your math solving skills!\n")
        time.sleep(1)

        filename = input("Enter the filename of the quiz (press Enter to use 'created_quiz_questions.txt'): ").strip()
        if filename:
            self.filename = filename

        self.load_questions()

        if not self.questions:
            print(Fore.RED + "No questions were found. Exiting the quiz game.")
            return

        random.shuffle(self.questions)

        for question in self.questions:
            question.display()
            answer = self.get_valid_answer()
            if question.check_answer(answer):
                print(Fore.GREEN + "🟩 Your Answer is Correct!\n")
                self.score += 1
            else:
                correct_letter = question.correct
                correct_text = question.choices[correct_letter]
                print(Fore.RED + f"🟥 The Answer is Incorrect. The correct answer was {correct_letter}: {correct_text}\n")

        print(Fore.MAGENTA + f"You've completed the Quiz! You scored: {self.score} out of {len(self.questions)}")
        print(Fore.MAGENTA + "Thank you for playing this short Math Quiz Game!")

    def get_valid_answer(self):
        while True:
            answer = input("Your answer (a, b, c, or d): ").lower()
            if answer in ['a', 'b', 'c', 'd']:
                return answer
            print(Fore.YELLOW + "Invalid input. Enter only a, b, c, or d.")
