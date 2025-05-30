# This is the main controller for playing the quiz game

# Adding a simple creative upgrade: colored text and timed messages
import random
import time
from colorama import Fore, Style, init
init(autoreset=True) # So that it auto resets the color after each print

# INITIALIZE the QUIZ Game

# DISPLAY the welcome message to the players
print(Fore.CYAN + "🧐 Welcome to this short Math Quiz Game! Let's test your problem solving skills!")
time.sleep(1)
print(Fore.CYAN + "Let's test your math solving skills!\n")
time.sleep(1)

# ASK the user to inpute filename of quiz (its default is set to "created_quiz_questions.txt")
filename = input("Enter the filename of the quiz (press Enter to user 'created_quiz_questions.txt'): ")
if filename.strip() == "":
    filename = "created_quiz_questions.txt"

# CALL function to load up the questions form the created text file
#      OPEN file in read mode 
#      READ all lines
#      INITIALIZE an empty list to store each question set
#      FOR each line group (question + choices + correct answer)
#           break down the text and extract:
#             Question, Choices (a, b , c, d), Correct Answer
#           ADD each question set to the list
#      RETURN list of break downed txt questions

def load_questions_from_file(filename):
    questions = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        line_index = 0
        while line_index < len(lines):
            line = lines[line_index].strip()
            if line == "":
                line_index += 1
                continue
            question = line
            choices = {}
            for choice_number in range (1, 5):
                key, value = lines[line_index + choice_number].strip().split(": ")
                choices[key] = value
            correct_answer_line = lines[line_index + 5].strip()
            correct_answer = correct_answer_line.split(": ")[1]
            questions.append({"question": question, "choices": choices, "answer": correct_answer})
            line_index += 7
    except FileNotFoundError:
        print(Fore.RED + " ⚠️ CAUTION⚠️ Cannot locate the file. Please type in an existing filename and check if it is correct.")
        return []
    return questions

# IF no questions were found
#   DISPLAY an error message
#   END program
quiz_data = load_questions_from_file(filename)
if not quiz_data:
    print(Fore.RED +"No questions were found. Exiting the quiz game.")
    exit()

# SHUFFLE the list of questions (so that the user will answer the questions in a randomized way)
random.shuffle(quiz_data)

# SET score to 0
# SET total to number of questions
score = 0
total = len(quiz_data)

# FOR each questions in the list
#       DISPLAY questions and choices (a to d)  
#       ASK user for their answer (a, b, c, or d)
#       IF user's answer is equal to the correct answer
#           DISPLAY "Correct Answer!" message text
#           INCREMENT score 
#       ELSE    
#           DISPLAY "Incorrect Answer." message text
for item in quiz_data:
    print("\n" + Fore.BLUE + "📃 " + item["question"])
    for key in sorted(item["choices"].keys()):
        print(f" {key}: {item['choices'][key]}")
    while True:
        user_answer = input("Your answer (a, b, c, or d): ").lower()
        if user_answer in ['a', 'b', 'c', 'd']:
            break
        else:
            print(Fore.YELLOW + "Invalid input. Enter only a, b, c, or d.")
    if user_answer == item["answer"]:
        print(Fore.GREEN + "🟩 Your Answer is Correct!\n")
        score += 1
    else:
        correct_letter = item["answer"]
        correct_text = item["choices"][correct_letter]
        print(Fore.RED + f"🟥 The Answer is Incorrect. The correct answer was {correct_letter}: {correct_text}\n")

# after all of the questions were displayed
#       DISPLAY final score out of how many questions were provided
print(Fore.MAGENTA + f"You've completed the Quiz! You scored: {score} out of {total}")

# DISPLAY a thank you message in the end
print(Fore.MAGENTA +"Thank you for playing this short Math Quiz Game! 🙋‍♂️")

# END the Quiz Game