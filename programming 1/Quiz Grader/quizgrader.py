import csv
import random

def load_questions(filename):
    questions = []

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("Error: questions file not found.")
        return questions

    reader = csv.reader(file)

    for line in reader:
        if len(line) < 2:
            print("Skipping row: not enough columns.")
            continue

        question_text = line[0].strip()
        correct_letter = line[1].strip().lower()

        if not question_text or not correct_letter:
            print("Skipping row: missing question or answer.")
            continue

        questions.append([question_text, correct_letter])

    file.close()
    return questions


def ask_question(q):
    question_text = q[0]
    correct_letter = q[1]

    print()
    print(question_text)
    answer = input("Enter your answer (a/b/c/d): ").strip().lower()

    if answer == correct_letter:
        print("Correct!")
        return True
    else:
        print("Wrong. The correct answer is", correct_letter)
        return False


def run_quiz(questions):
    if len(questions) == 0:
        print("No questions to ask.")
        return 0, 0, 0.0

    print("There are", len(questions), "questions in the quiz.")
    print("How many questions do you want to answer? (0 or too big = all)")

    while True:
        user_input = input("Number of questions: ")
        try:
            n = int(user_input)
            break
        except ValueError:
            print("Please enter a valid integer.")

    if n <= 0 or n > len(questions):
        n = len(questions)

    # Shuffle for random order
    random.shuffle(questions)
    selected = questions[:n]

    correct_count = 0

    for q in selected:
        if ask_question(q):
            correct_count += 1

    total = len(selected)
    if total > 0:
        percentage = (correct_count / total) * 100
    else:
        percentage = 0.0

    print()
    print("=== Quiz summary ===")
    print("Questions answered:", total)
    print("Correct answers   :", correct_count)
    print("Score             :", round(percentage, 1), "%")

    return total, correct_count, percentage


def main():
    print("=== Quiz & Grader ===")
    questions = load_questions("Questions.csv")
    run_quiz(questions)


main()
