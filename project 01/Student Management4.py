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
    print("10.Sort Student")
    print("11.Count Student")
    print("12.Highest Grade")
    print("13.Lowest Grade")
    print("14.Exit\n\n")


def add_student():

    name = input("Name: ")

    for student in students:
        if student['Name'].lower() == name.lower():
            print("Student already exists.")
            return

        try:
            age = int(input("Age: "))
            grade = float(input("Grade: "))

        except ValueError:
            print('Please enter valid numbers.')
            return

        if grade < 0 or grade > 20:
            print("Grade must be between 0 and 20.")
            return

        student = {
            "Name" : name,
            "Age" : age,
            "Grade" : grade
        }

        students.append(student)
        print("Student added successfully.")


def show_student():
    
    if len(students) == 0:
        print("No student found.")
        return
    
    print("===== Student =====")
    
    for student in students:

        print(f"Name: {student['Name']}")
        print(f"Age: {student['Age']}")
        print(f"Grade: {student['Grade']}")
        print("-" * 50)


def search_student():
    
    name = input("Name: ")

    found = False

    for student in students:
        if student["Name"].lower() == name.lower():
            print("Student found successfully.\n")
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
            students.remove(student)
            print("Student removed successfully.")
            found = True
            break

    if not found:
        print("Student not found.")


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


def edit_student():

    name = input("Name: ")

    for student in students:
        if student['Name'].lower() == name.lower():

            student['Name'] = input("Name: ")

            try:
                student['Age'] = int(input("Age: "))
                student['Grade'] = float(input("Grade: "))

            except ValueError:
                print("Please enter valid nimber.")
                return
            
            print("Student edit successfully.")
            return

        print("Student not found.")


def average_grade():

    if len(students) == 0:
        print("No student found.")
        return

    total = 0

    for student in students:
        total += student['Grade']

    average = total / len(students)

    print(f"Average Grade: {average}")


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
    print(f"Grade {top['Grade']}")


def sort_student():

    if len(students) == 0:
        print("No student found.")
        return

    sorted_students = sorted(students, key=lambda student: students['Grade'], reverse=True)

    for student in sorted_students:

        print("\n===== Student sorted by Grade =====")
        print(f"Name: {student['Name']}")
        print(f"Grade: {student['Grade']}")
        print("*" * 50)


def count_student():

    print(f"Total Students: {len(students)}")


def highest_grade():

    if len(students) == 0:
        print("No student found.")
        return

    high = students[0]

    for student in students:
        if student['Grade'] > high['Grade']:
            high = student
    
    print("\n===== Highest Grade =====")
    print(f"Name: {high['Name']}")
    print(f"Grade: {high['Grade']}")


def lowest_grade():

    if len(students) == 0:
        print("No student found.")
        return
    
    low = students[0]

    for student in students:
        if student['Grade'] < low['Grade']:
            low = student

    print("\n===== Lowest Grade =====")
    print(f"Name: {low['Name']}")
    print(f"Grade: {low['Grade']}")


def statistics():

    if len(students) == 0:
        print("No student found.")
        return
    
    grades = []

    for student in students:
        grades.append(student['Grade'])

        print("\n==== Statistics ====")
        print(f"Toatal Student: {len(students)}")
        print(f"Average Grade: {sum(grades)/len(grades)}")
        print(f"Highest Grade: {max(grades)}")
        print(f"Lowest: {min(grades)}")


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
            average_grade()

        elif choice == "7":
            edit_student()

        elif choice == "8":
            save_students()

        elif choice == "9":
            load_students()

        elif choice == "10":
            sort_student()

        elif choice == "11":
            count_student()

        elif choice == "12":
            highest_grade()

        elif choice == "13":
            lowest_grade()

        elif choice == "14":
            print("Good Bye!")
            break

        else:
            print("Invalid choice.")

main()