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
        print()
        score