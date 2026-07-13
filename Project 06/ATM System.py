balance = 1000


def show_menu():
    print("\n===== ATM =====")
    print()
    print("1.Show Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")


def show_balance():

    print(f"Current Balance: {balance}")


def deposit():

    global balance

    amount = float(input("Enter Amount: "))

    balance += amount

    print("Deposit Successfully.")
    print(f"Current Balance: ${balance}")


def withdraw():

    global balance

    amount = float(input("Enter Amount: "))

    if amount <= balance:
        balance -= amount
        print("Withraw Successfully.")
        print(f"Current Balance: ${balance}")
    else:
        print("Insufficient Balance!")


def main():

    while True:

        show_menu()

        choice = input("Choice: ")

        if choice == "1":
            show_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()
            
        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("Invalid choice.")


main()