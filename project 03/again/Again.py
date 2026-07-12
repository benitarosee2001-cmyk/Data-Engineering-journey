import json

students = []

def show_menu():
    print("===== Student Management =====")
    print("1.Add Student")
    print("2.Show Students")
    print("3.Search Student")
    print("4.Delete student")
    print("5.Save")
    print("6.Load")
    print("7.Exit")


def add_student():

    name = input("Name: ")
    age = int(input("Age: "))
    grade = float(input("Grade: "))

    student = {
        "Name" : name,
        "Age" : age,
        "Grade" : grade
    }

    students.append(student)
    print("\nStudent Added Successfully.")


def show_student():

    if len(students) == 0:
        print("No students found.")
    else:
        print("===== Students =====")

        for student in students:
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Grade: {student['Grade']}")
            print("*" * 50)


def search_student():

    search = input("Student Name: ")

    found = False

    for student in students:

        if student["Name"].lower() == search.lower():
            print("\nStudent found successfully.")
            print("==== Students ====")
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Grade: {student['Grade']}")
            found = True
            break
    
    if not found:
        print("Student not found.")


def delete_student():

    delete = input("Student Name: ")

    found = False

    for student in students:
        if student["Name"].lower() == delete.lower():
            students.remove(student)
            print("\nStudent deleted successfully.")
            found = True
            break

    if not found:
        print("Student not found.")


def save_student():

    with open("students.json", "w", encoding="utf8") as file:
        json.dump(students, file, indent=4)

    print("Student saved.")


def load_student():
    
    global students
    
    with open("students.json", "r", encoding="utf8") as file:
        students = json.load(file)

    print("Student loaded")


def main():
    
    while True:
        
        show_menu()
        
        choice = input("Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            save_student()

        elif choice == "6":
            load_student()

        elif choice == "7":
            print("Good Bye")
            break
        
        else:
            print("Invalid choice.")

main()