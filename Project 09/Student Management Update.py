import json

students = []


def show_menu():

    print("\n===== Student Management =====\n")
    print("1.Add Student")
    print("2.Show students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Edit Student")
    print("6.Show Average Grade")
    print("7.Show Top Student")
    print("8.Save")
    print("9.Load")
    print("10.Exit\n\n")


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
    print("Student Added Successfully.")


def show_student():

    if len(students) == 0:
        print("Not Found.")

    else:
        print("\n===== Students =====")

        for student in students:

            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Grade: {student['Grade']}")
            print("-" * 50)


def search_student():

    name = input("Name: ")

    found = False

    for student in students:
        if student['Name'].lower() == name.lower():
            print("Student founded.\n")
            print("\n===== Students =====")
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Grade: {student['Grade']}")
            found = True
            break

    if not found:
        print("Student not found.")


def delete_student():

    name = input("Name: ")

    found = False

    for student in students:
        if student['Name'].lower() == name.lower():
            print("Student deleted successfully.")
            students.remove(student)
            found = True
            break

    if not found:
        print("Student not found.")


def edit_student():

    name = input("Name: ")

    found = False

    for student in students:
        if student['Name'].lower() == name.lower():


            student['Name'] = input("New Name: ")
            student['Age'] = int(input("New Age: "))
            student['Grade'] = float(input("New Grade: "))

            print("Student Edit Successfully.")

            found = True

            break

    if not found:
        print("Student not found.")


def show_avarege_grade():

    if len(students) == 0:
        print("No student found.")
        return

    total = 0

    for student in students:

        total += student['Grade']

        average = total / len(students)
        
        print(f"Grade Avarege: {average}")


def top_student():

    if len(students) == 0:
        print("No student found.")
        return
    
    top = students[0]
    
    for student in students:

        if student['Grade'] > top['Grade']:
            top = student

        print("\n===== Top Student =====")
        print(f"Name: {top['Name']}")
        print(f"Grade: {top['Grade']}")


def save_student():

    with open("Students.json", "w", encoding="utf8") as file:
        json.dump(students, file, indent=4)

    print("Student save successfully.")


def load_student():

    global students

    with open("Students.json", "r", encoding="utf8") as file:
        students = json.load(file)

    print("Student load successfully,")


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
            edit_student()

        elif choice == "6":
            show_avarege_grade()

        elif choice == "7":
            top_student()

        elif choice == "8":
            save_student()

        elif choice == "9":
            load_student()

        elif choice == "10":
            print("Good Bye!")
            break

        else:
            print("Invalid choice.")

main()