questions = [
    {
    "question" : "What is the capital of France?",
    "answer"  : "Paris"
    },
    {
    "question" : "How many days are in a week?",
    "answer" : "7"
    },
    {
    "question" : "What is 10 + 8?",
    "answer" : "18"
    }
]


def quiz_game():

    score = 0

    print("===== Quize Game =====\n")
    for i,question in enumerate(questions, start = 1):
        print(f"Question {i}")
        print(question['question'])

        user_answer = input("Your answer: ")

        if user_answer.lower() == question['answer'].lower():
            score += 1
        else:
            print("Wrong!")
            print(f"Correct Answer: {question['answer']}\n")

    total_question = len(questions)
    wrong_answer = total_question - score
    percentage = (score / total_question) * 100

    print("=" * 50)
    print("\tResult\t")
    print("=" * 50)
    print(f"Correct answer: {score}")
    print(f"Wrong answer: {wrong_answer}")
    print(f"Score: {percentage:.0f}")
    print("*" * 50)


quiz_game()