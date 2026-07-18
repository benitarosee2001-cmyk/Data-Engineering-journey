import json

FILE_NAME = "Students.json"

students = []

student_id = 1000

class Student:

    def __init__(self, student_id, name, age, grade):

        self.id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):

        print(f"""
            ID : {self.id}
            Name : {self.name}
            Age : {self.age}
            Grade : {self.grade}
            =====================
            """)

    def update(self, age, grade):

        self.age = age
        self.grade = grade

    def to_dict(self):

        return{
            "ID" : self.id,
            "Name" : self.name,
            "Age" : self.age,
            "Grade" : self.grade
        }


def generate_id():

    global student_id

    student_id += 1

    return student_id



def show_menu():

    print("""
========== Student Management ==========
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
========================================
""")


def add_student():

    name = input("Name: ")

    for student in students:
        if student.name.lower() == name.lower():

            print("Student already exists.")
            return
        
        age = input("Age: ")
        grade = input("Grade: ")

        new_student = student(
        generate_id(),
            name,
            age,
            grade
            )
        
        students.append(new_student)
        print(f"Student added successfully. ID{new_student.id}")


def show_student():

    if not students:
        print("No student found.")
        return
    
    for student in students:
        student.show_info()


def search_student():

    try:

        search_id = int(input("Search ID: "))

        for student in students:
            if student_id == search_id:
                student.show_info()
                return
        
        print("Student not found.")

    except ValueError:

        print("Invalid ID.")


def delete_student():

    try:
        
        delete_id = int(input("Student ID: "))

        for student in students:
            if student_id == delete_id:
                students.remove(student)
                print("Student deleted succcessfully.")
                return
        print("Student not found.")

    except ValueError:
        print("Invalid ID.")


def edit_student():

    try:

        edit_id = int(input("Student ID: "))

        for student in students:
            if student_id == edit_id:

                age = int(input("Age: "))
                grade = float(input("Grade: "))

                student.update(age, grade)

                print("Student updated.")
                return
        print("No student found.")

    except ValueError:
        print("Invalid ID.")


def average_student():

    if not students:
        print("No student found.")
        return
    
    total = 0

    for student in students:
        total += student.grade

    print(f"Average Grade: {total / len(students):.2f}")


def top_student():

    if not students:
        print("No student found.")
        return

    top = max(students,  key=lambda student:student.grade)

    print("======== Top Student ========")

    top.show_info()


def save_student():

    data = []

    for student in students:
        data.append(student.to_dict())

    with open(FILE_NAME, "w", encoding= "utf8") as file:

        json.dump(data, file, indent=4)

        print("Student saved successfully.")


def load_student():

    global students
    global student_id

    try:

        with open(FILE_NAME, "r", encoding="utf8") as file:
            data = json.load(file)

            students = []

            for item in data:

                student = Student(
                    item["ID"],
                    item["Name"],
                    item["Age"],
                    item["Grade"]
                )

                students.append(student)
                if item["ID"] > student_id:
                    student_id = item["ID"]

                print("Students load successfully.")
        
    except FileNotFoundError:
        print("File not found.")


def sort_student():

    if not students:
        print("No student found.")
        return
    
    sorted_students = sorted(students, key=lambda student:student.grade, reverse=True)

    print("====== Sorted Student ======")

    for student in sorted_students:
        student.show_info()


def count_student():

    print(f"Total Students: {len(students)}")


def highest_grade():

    if not students:
        print("No student found.")
        return
    
    highest = max(students, key=lambda student:student.grade)
    print("======= Highest Grade =======")

    highest.show_info()


def lowest_grade():

    if not students:
        print("No student found.")
        return
    
    lowest = min(students, key=lambda student:student.grade)
    print("======== Lowest Grade ========")
    lowest.show_info()


def statistics():

    if not students:
        print("No student found.")
        return

    grades = []

    for student in students:
        grades.append(student.grade)

    print("======== STATISTICE =======")
    print(f"Total Student: {len(students)}")
    print(f"Average Grade: {sum(grades)/len(grades)}")
    print(f"Highest Grade: {max(grades)}")
    print(f"lowet Grade: {min(grades)}")


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
            average_student()

        elif choice == "7":
            top_student()

        elif choice == "8":
            save_student()

        elif choice == "9":
            load_student()

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
            print("Good Bye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()