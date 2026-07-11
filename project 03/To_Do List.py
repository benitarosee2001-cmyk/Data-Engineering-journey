import json

tasks = []

def add_task():

    task = input("Task: ")

    new_task ={
        "Task" : task,
        "Completed" : False
    }

    tasks.append(new_task)
    print("Task Added.")


def show_task():

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        if task["Completed"]:
            status = "yes"
        else:
            status = "no"
        
        print("-" * 50)
        print("Task: ", task["Task"])
        print("Completed: ", status)

def mark_task():

    title = input("Task: ")

    found = False

    for task in tasks:

        if task["Task"].lower() == title.lower():

            task["Completed"] = True

            print("Task Completed.")

            found = True

            break

    if not found:
        print("Task not found.")


def delete_task():

    title = input("Task: ")

    for task in tasks:

        if task["Task"].lower() == title.lower():

            tasks.remove(task)

            print("Task deleted.")

            return
        
    print("Task not found")


def save_task():
    
    with open("todo.json", "w", encoding = "utf8") as file:
        json.dump(tasks, file, indent=4)

        print("Saved.")

def load_task():

    global tasks

    with open("todo.json", "r", encoding = "utf8") as file:

        tasks = json.load(file)

    print("Loaded.")

def main():

    while True:

        print("\n===== To Do List =====")
        print("1.Add Task")
        print("2.Show Tasks")
        print("3.Mark Task")
        print("4.Delete Task")
        print("5.Save")
        print("6.Load")
        print("7.Exit")

        choice = input("Choice: ")

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
            print("Invalid Choice")

main()