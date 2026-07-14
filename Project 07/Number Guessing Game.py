import random

attempts = 0

def guessing_game():

    global attempts

    number = random.randint(1, 100)
    
    print("\n===== Number Guessing Game =====")

    while True:

        guess = int(input("Guess a number between 1 and 100: "))

        attempts += 1

        if guess < number:
            print("Too Low!")

        elif guess > number:
            print("Too High!")

        else:
            print("Congratulations!")
            print("You gussed the number!")

            print(f"Attempts: {attempts}")
            break

        
guessing_game()