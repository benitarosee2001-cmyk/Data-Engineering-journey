from Student import Student
from database import save_student, load_student
from utils import generate_id, update_last_id

students = load_student
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
        
    age = int(input("Age: "))
    grade = float(input("Grade: "))

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
                print("Student deleted successfully.")
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
        print("Inavalid ID.")


def average_grade():

    if not students:
        print("No student found.")
        return
    
    average = sum(students.grade for student in students) / len(students)

    print(f"Average Geade: {average:.2f}")


