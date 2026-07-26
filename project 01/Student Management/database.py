import json
from Student import Student

FILE_NAME = "Students.json"

def save_student(students):

    data = []

    for student in students:
        data.append(student.to_dict())

    with open(FILE_NAME, "w", encoding="utf8") as file:
        json.dump(data, file, indent=4)

    print("Student saved successfully.")


def load_student():

    students = []

    try:

        with open(FILE_NAME, "r", encoding="utf8") as file:
            data = json.load(file)

        for item in data:

            student = Student(
                item["ID"],
                item["Name"],
                item["Age"],
                item["Grade"]
            )

            students.append(student)

    except FileNotFoundError:
        print("File not found.")

    return students