import json

tasks = []

def show_menu():

    print("==== Tasks ====")
    print("1.Add Task")
    print("2.Show Tasks")
    print("3.Mark Task as Completed")
    print("4.Delete Task")
    print("5.Save")
    print("6.Load")
    print("7.Exit")
    print("-" * 50)


def add_task():

    task = input("Task: ")

    task = {
        "Task" : task,
        "Completed" : False
    }

    tasks.append(task)
    print("Task add successfully.")


def show_task():

    if len(tasks) == 0:
        print("No task found.")
    else:
        print("==== Tasks ====")

        for task in tasks:
            if task["Completed"]:
                print("completed: Ok")
            else:
                print("Completed: No")


def mark_task():

    title = input("Task: ")

    found = False

    for task in tasks:
        if task["Task"].lower() == title.lower():
            task["Completed"] = True
            print("Task completed.")
            found = True
            break
    
    if not found:
        print("Task not found.")



def delete_task():

    title = input("Task: ")

    found = False

    for task in tasks:

        if task["Task"].lower() == title.lower():
            tasks.remove(task)
            print("Task deleted successfully.")
            found = True
            break

    if not found:
        print("Task not found.")


def save_task():

    with open("Todo.json", "w", encoding = "utf8") as file:
        json.dump(tasks, file, indent=4)
    

    print("Task save successfully.")


def load_task():
    
    global tasks
    
    with open("Todo.json", "r", encoding="utf8") as file:
        tasks = json.load(file)

    
    print("Task load successfully.")


def main():
    
    while True:

        show_menu()
        
        choice = input("choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_task()

        elif choice == "3":
            mark_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            save_task()

        elif choice == "6":
            load_task()

        elif choice == "7":
            print("Good Bye!")
            break

        else:
            print("Invalid choice.")

main()