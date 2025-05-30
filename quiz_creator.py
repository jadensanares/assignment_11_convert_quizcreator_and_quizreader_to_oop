# This is the main controller for making the quiz

# All of the questions, choices, and the correct answer shall be saved to a separate file (.txt)
     # Define a function save_to_file()
        # A text file will open in appen mode.
        # Write the question.
        # Write each option with its respective label (a, b, c, d).
        # Write the correct answer.
        # Format the txt file by adding a space between entries for better readability to the user.
def save_to_file(question, choices, correct_answer, filename="created_quiz_questions.txt"):
    with open(filename, "a") as file:
        file.write(question + "\n")
        for choice, answer in choices.items():
            file.write(choice + ": " + answer + "\n")
        file.write("Correct Answer: " + correct_answer + "\n\n")

# Make a welcome message to the user.
def main():
    print("Hello User, welcome to this Quiz Creator!")

# Create the loop in able for the user to input as many quiz questions that they want.
    # Asking the user to input a quiz question and then store it.
    while True:
        question = input("Enter the question: ")
 
    # Make a dictionary where it stores the 4 possible answers (a, b, c, d).
        # For each letter choices (a, b, c, d), the user will enter the answer and store it to the dictionary.
        choices = {}
        for choice in ['a', 'b', 'c', 'd']:
            answer = input("Enter the answer for " + choice + ": ")
            choices[choice] = answer

    # Asking the user to input the correct answer that is found in one of the following letter choices: (a, b, c, d)
    # For consistency, the letter input should be lowercased, we will be converting them.
        while True:   
            correct_answer = input("Enter the correct answer (a, b, c, or d): ").lower()
            if correct_answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Invalid choice. Enter only the letters a, b, c, or d.")

        save_to_file(question, choices, correct_answer) # to run seperate txt file function inside the main() 

    # Make a visual display feedback for the questions entered (for more convenience visually in letting the user know what answer options are correct or not)
        # Make a loop for each answer option
        # If the option is the correct answer, print it with a green square emoji text (🟩).
        # If the option is not the correct answer, print it with a red square emoji text (🟥).
        print("Question feedback:")
        for choice, answer in choices.items():
            if choice == correct_answer:
                print(choice + ": " + answer + " 🟩")
            else:
                print(choice + ": " + answer + " 🟥")

    # Ask the user if they want to put in another question.
        # If the response is "yes" then the loop continues, if "no" then the loop breaks
        another_question = input("Would you like to add another question? Type either (yes) or (no): ").lower()
        if another_question != "yes":
            break

# If the user wants to exit the program, put in a thank message to the user 
    print("\nThank you for making the quiz! ^-^")

if __name__ == "__main__":
    main()
