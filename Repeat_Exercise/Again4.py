questions = [
    {
    "question" : "What is the capital of South Korea?",
    "answer" : "Seoul"
    },
    {
    "question" : "What do bees make?",
    "answer" : "Honey"
    }
]

def quiz_game():

    score = 0

    for i,question in enumerate(questions, start=1):
        print(f"Question {i}")
        print(question['question'])

        user_answer = input("Your Answer: ")

        if user_answer.lower() == question['answer'].lower():
            print("Correct")
            score += 1
        else:
            print("Wrong")
            print(f"Correct answer: {question['answer']}")

            total_question = len(questions)
            wrong_answer = total_question - score
            percentage = (score / total_question) * 100

            print("===== Result =====")
            print(f"Correct answer: {score}")
            print(f"Wrong answer: {wrong_answer}")
            print(f"Score: {percentage}%")


quiz_game()