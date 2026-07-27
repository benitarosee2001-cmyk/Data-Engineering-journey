from database import load_student, save_student
from student import Student
from utils import generat_id, update_last_id

students = load_student
update_last_id(students)


def show_menu():

    print("""
========== Student Management ==========
1. Add Student
2. Show Students
3. Search Student
4. Delete Student
5. Edit Student
6. Average Grade
7. Highest Grade
8. Lowest Grade
9. Save Students
10. Load Students
11. Statistics
12. Exit
========================================
""")


def add_student():

    name = input("Name: ")

    for student in students:
        if student.name.lower() == name.lower():
            print("Student already exists.")
            return

        try:
            age = int(input("Age: "))
            grade = float(input("Grade: "))

        except ValueError:
            print("Invalid input.")

            new_student = Student(
                generat_id,
                name,
                age,
                grade
            )

            students.append(new_student)

            print(f"Student added successfully. ID = {new_student.id}")

def show_student():

    if not students:
        print("No student found.")
        return

    for student in students:
        student.show_info()


def search_student():

    search_id = int(input("Student ID: "))

    try:

        for student in students:
            if student.id == search_id:
                student.show_info()
                print("Student found.")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid ID.")


def edit_student():

    try:

        edit_id = int(input("Student ID: "))

        for student in students:
            if student.id == edit_id:

                age = int(input("Age: "))
                grade = float(input("Grade: "))

                student.update(age, grade)

                print("Student updated.")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid ID.")


def delete_student():

    try:

        delete_id = int(input("Student ID: "))

        for student in students:
            if student.id == delete_id:

                students.remove(student)

                print("Student delete successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid ID.")


def average_grade():

    if not students:
        print("No student found.")
        return

    average = sum(student.grade for student in students) / len(students)

    print(f"Average Grade: {average:.2f}")


def highest_grade():

    if not students:
        print("No student found.")
        return

    highest = max(students, key=lambda student: student.grade)

    print("\n======= Highest Grade =======")

    highest.show_info()


def lowest_grade():

    if not students:
        print("No student found.")
        return

    lowest = min(students, key=lambda student:student.grade)

    print("\n======== Lowest Grade =========")

    lowest.show_info()


def student_count():

    print(f"Total students: {len(students)}")


def statistics():

    if not students:
            print("No student found.")
            return

    grades = [student.grade for student in students]

    print("\n======== Statistics =========")
    print(f"Average Grade: {sum(grades) / len(grades):.2f}")
    print(f"Highest Grade: {max(grades)}")
    print(f"lowest Grade: {min(grades)}")
    print(f"Student Count: {len(students)}")


def  main():

    global students

    while True:

        show_menu()

        choice = input("Choose: ")

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
            highest_grade()

        elif choice == "8":
            lowest_grade()

        elif choice == "9":

            save_student(students)

        elif choice == "10":

            students = load_student()
            update_last_id(students)

        elif choice == "11":
            statistics()

        elif choice == "12":
            print("Good Bye.")
            break

        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()