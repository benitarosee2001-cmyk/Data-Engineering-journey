from database import load_student, save_student
from Student import Student
from utils import generate_id, update_last_id

students = load_student()
update_last_id(students)


def show_menu():

    print(""" ========== Student Management ========== 
1. Add Student
2. Show Students
3. Search Student
4. Delete Student
5. Edit Student
6. Average Grade
7. Top Student
8. Save Students
9. Load Students
10. Sort Students
11. Count Students
12. Highest Grade
13. Lowest Grade
14. Statistics
15. Exit
=============================""")


def add_student():

    name = input("Name: ")

    for student in students:
        if student.name().lower() == name.lower():
            print("Student already exists.")
            return
    try:    
        age = int(input("Age: "))
        grade = float(input("Grade: "))
    except ValueError:
        print("Invalid input.")

    new_student = Student(
        generate_id(),
        name,
        age,
        grade
    )

    students.append(new_student)

    print(f"Student added successfully. ID= {new_student.id}")


def show_student():

    if not students:
        print("Student not found.")
        return
    
    for student in students:
        student.show_info()


def search_student():

    try:

        search_id = int(input("Student ID: "))

        for student in students:
            if student.id == search_id:
                student.show_info()
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

                print("Student deleted.")
                return

        print("Student not found.")

    except ValueError:

        print("Invalid ID.")


def edit_student():

    try:

        edit_id = int(input("Student ID: "))

        for student in students:

            if student.id == edit_id:

                age = int(input("New Age: "))
                grade = float(input("New Grade: "))

                student.update(age, grade)

                print("Student updated.")
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


def top_student():

    if not students:
        print("No student found.")
        return

    top = max(students, key=lambda student: student.grade)

    print("\n===== Top Student =====")
    top.show_info()


def sort_student():

    if not students:
        print("No student found.")
        return

    sorted_students = sorted(
        students,
        key=lambda student: student.grade,
        reverse=True
    )

    print("\n===== Sorted Students =====")

    for student in sorted_students:
        student.show_info()


def count_student():

    print(f"Total Students: {len(students)}")


def highest_grade():

    if not students:
        print("No student found.")
        return

    highest = max(
        students,
        key=lambda student: student.grade
    )

    print("\n===== Highest Grade =====")
    highest.show_info()


def lowest_grade():

    if not students:
        print("No student found.")
        return

    lowest = min(
        students,
        key=lambda student: student.grade
    )

    print("\n===== Lowest Grade =====")
    lowest.show_info()


def statistics():

    if not students:
        print("No student found.")
        return

    grades = [student.grade for student in students]

    print("\n===== Statistics =====")
    print(f"Total Students : {len(students)}")
    print(f"Average Grade  : {sum(grades) / len(grades):.2f}")
    print(f"Highest Grade  : {max(grades)}")
    print(f"Lowest Grade   : {min(grades)}")


def main():

    global students

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

            top_student()

        elif choice == "8":

            save_student(students)

        elif choice == "9":

            students = load_student()
            update_last_id(students)

        elif choice == "10":

            sort_student()

        elif choice == "11":

            count_student()

        elif choice == "12":

            highest_grade()

        elif choice == "13":

            lowest_grade()

        elif choice == "14":

            statistics()

        elif choice == "15":

            save_student(students)
            print("Good Bye!")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()