from quiz_creator import QuizCreator
from quiz_game import QuizGame

def main():
    print("Welcome to this simple Quiz Program!")
    print("1. Create a Quiz")
    print("2. Play the Quiz")

    choice = input("Choose a number option (1 or 2): ")

    if choice == "1":
        creator = QuizCreator()
        creator.run()
    elif choice == "2":
        game = QuizGame()
        game.start_quiz()
    else:
        print("Invalid choice. Please run the program again and specifically select 1 or 2.")
    
if __name__ == "__main__":
    main()