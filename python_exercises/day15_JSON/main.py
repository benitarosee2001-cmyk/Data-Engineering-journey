#Exercise 1
import json

students = {
    "name" : "Benita",
    "age" : 24,
    "job" : "Data Engineer"
}

with open("student.json", "w", encoding="utf8") as file:
    json.dump(students, file, indent = 4)