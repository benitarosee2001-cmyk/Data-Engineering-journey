import json

FILE_NAME = "students.json"

students = []

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):

        print(f"""
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
            "Name" : self.name,
            "Age" : self.age,
            "Grade" : self.grade
        }


def show_menu():

    print("""======== Student Management =========\n
1.Add Student
2.Show Students
3.Search Student
4.Delete Student
5.Edit Student
6.Average Grade
7.Top Student
8.Save Students
9.Load Students
10.Sort Students
11.Count Students
12.Highest Grade
13.Lowest Grade
14.Statistics
15.Exit
===========================================
""")


def add_student():

    name = input("Name: ")

    for student in students:
        if student.name.lower() == name.lower():
            print("Student already exists.")
            return

    age = int(input("Age: "))
    grade = float(input("Grade: "))

    new_student = student(name,age,grade)

    students.append(new_student)
    print("Student added successfully.")


def show_students():

    if not students:
        print("No student found.")
        return
    
    for student in students:
        student.show_info()


def search_student():

    name = input("Name: ")

    for student in students:
        if student.name.lower() == name.lower():
            student.show_info()
            return


    print("Student not found.")


def delete_student():

    name = input("Name: ")

    for student in students:
        if student.name.lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def edit_student():

    name = input("Name: ")

    for student in students:
        if student.name.lower() == name.lower():
            age = int(input("Age: "))
            grade = float(input("Grade: "))
            student.update(age, grade)

            print("Student updated.")
            return

    print("Student not found.")


def average_student():

    total = 0

    for student in students:
        total += student.grade

    average = total / len(students)

    print(f"Average Grade: {average}")


def top_student():

    top = students[0]

    for student in students:
        if student.grade > top.grade:
            top = student

    print("====== Top Student ======")
    top.show_info()


def save_student():

    data = []

    for student in students:
        data.append(student.to_dict())

    with open(FILE_NAME, "w", encoding = "utf8") as file:
        json.dump(data, file, indent=4)

    print("Student saved successfully.")

