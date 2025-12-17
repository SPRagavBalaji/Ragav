import csv 

def create_question(filename):
    questions = []
    for i in range(0, 3):
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        questions.append((question, answer))
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for question, answer in questions:
            writer.writerow([question, answer])

create_question('questions.csv')