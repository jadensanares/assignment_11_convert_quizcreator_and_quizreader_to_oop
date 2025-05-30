# Class for handling file for reading and writing

from question import Question

class QuizFileHandler:
    @classmethod
    def save_questions(question_list):
        
        with open("created_quiz_questions.txt", "w", encoding="utf-8") as file:
            for question in question_list:
                file.write(question.question_text + "\n")
                for option_letter, answer_text in question.choices.items():
                    file.write(f"{option_letter}:{answer_text}\n")
                file.write("ANSWER:" + question.correct + "\n\n")
    @classmethod
    def load_questions():
        with open("created_quiz_questions.txt", "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]

        question_list = []
        index = 0
        while index < len(lines):
            question_text = lines[index]
            choices = {}
            for i in range(1, 5):
                letter, answer_text = lines[index + i].split(":", 1)
                choices[letter] = answer_text
            correct_answer = lines[index + 5].split(":")[1]
            question = Question(question_text, choices, correct_answer)
            question_list.append(question)
            index += 6

        return question_list
