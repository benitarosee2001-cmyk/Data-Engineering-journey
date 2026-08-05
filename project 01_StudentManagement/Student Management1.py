import json

students = []

def show_menu():

    print("===== Student Management =====")
    print("\n1.Add Student")
    print("2.Show Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Save to JSON")
    print("6.Load from JSON")
    print("7.Exit")
    print("*" * 50)


def add_student():

    name = input("Name: ")
    age = int(input("Age: "))
    grade = float(input("Grade: "))

    student = {
        "name" : name,
        "age" : age,
        "grade" : grade
    }

    students.append(student)

    print("Student Added!")


def show_students():

    if len(students) == 0:
        print("No students found")

    else:
        print("\n===== Students =====")

        for student in students:
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            print("-" * 50)


def search_student():
    search = input("Student Name: ")

    found = False

    for student in students:

        if student["name"].lower() == search.lower():
            print("\nStudent Found!")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            found = True
            break

        if not found:
            print("\nStudent not found.")


def delete_student():

    delete = input("Student Name: ")

    found = False

    for student in students:
        if student["name"].lower() == delete.lower():
            students.remove(student)
            print("\nStudent Deleted")
            found = True
            break

        if not found:
            print("\nStudent not found.")


def save_students():
    with open("students.json", "w", encoding="utf8") as file:
        json.dump(students, file, indent = 4)

    print("\nStudent saved successfully.")


def load_students():
    global students

    try:
        with open("students.json", "r", encoding = "utf8") as file:
            students = json.load(file)
        
        print("\nStudents loaded successfully.")
    
    except FileNotFoundError:
        print("\nFile not found.")


def main():
    while True:

        show_menu()

        choice = input("Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            save_students()

        elif choice == "6":
            load_students()

        elif choice == "7":
            print("\nGood Bye!")
            break

        else:
            print("Invalid choice.")


main()