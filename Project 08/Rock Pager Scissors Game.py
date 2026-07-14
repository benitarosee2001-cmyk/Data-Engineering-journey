import random


def rock_pager_scissors():

    while True:

        choices = ["Rock", "Pager", "Scissors"]

        print("\n===== Rock Pager Scissors =====")
        print()
        print("Choose:")
        print("1.Rock")
        print("2.Pager")
        print("3.Scissors\n\n")

        choice = input("Choice (1_3): ")

        if choice == "1":
            user_choice = "Rock"

        elif choice == "2":
            user_choice == "Pager"

        elif user_choice == "3":
            user_choice = "Scissors"

        else:
            print("Invalid choice.")
            return

        computer_choice = random.choice(choices)

        print(f"Your choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")

        if user_choice == computer_choice:
            print("\nDraw!")

        elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):

            print("\n\tYou win!")
        
        else:
            print("\n\tComputer wins!")



rock_pager_scissors()