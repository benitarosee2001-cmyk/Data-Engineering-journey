#Exercise 1
import json

students = {
    "name" : "Benita",
    "age" : 24,
    "job" : "Data Engineer"
}

with open("person.json", "w", encoding="utf8") as file:
    json.dump(students, file, indent = 4)


#Exercise 2
#import json

with open("person.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data)


#Exercise 3
#import json

with open("person.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data["name"])


#Exercise 4
#import json

skills = {
    "Python" : 1,
    "SQL" : 2,
    "Spark" : 3
}

data = json.dumps(skills)

print(data)


#Exercise 5
#import json

person = '{"city" : "Berlin", "country" : "Germany"}'

data = json.loads(person)

print(data)


#Exercise 6
#import json

profile = {
    "name" : "Benita",
    "skills" : ["Python", "SQL", "Spark"],
    "experience" : 1
}

with open("profile.json", "w", encoding="utf8") as file:
    json.dump(profile, file, indent = 4)


#Exercise 7
#import json

with open("profile.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data["skills"])


#Exercise 8
#import json

book = {
    "title" : "Python",
    "pages" : 500
}

with open("book.json", "w", encoding="utf8") as file:
    json.dump(book, file)


#Exercise 9
#import json

car = {
    "brand" : "BMW",
    "year" : 2026
}

with open("car.json", "w", encoding="utf8") as file:
    json.dump(car, file, indent = 4)


#Exercise 10
#import json

with open("book.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data)


#Exercise 11
#import json

with open("car.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data["brand"])


#Exercise 12
#import json

person = {
    "city" : "Berlin",
    "country" : "Germany"
}

data = json.dumps(person)

print(data)


#Exercise 13 
#import json

d = {
    "language" : "Python",
    "level" : "Beginner"
}

data = json.dumps(d)

print(data)


#Exercise 14
#import json

text = '{"name" : "Sali", "age" : 23}'

data = json.loads(text)

print(data)


#Exercise 15
#import json

d = '{"job" : "Data Engineer", "country" : "Canada"}'

data = json.loads(d)

print(data["job"])


#Exercise 16
#import json

profile2 = {
    "name" : "Benita",
    "skills" : ["Python", "SQL", "Spark"],
    "country" : "Germany"
}

with open("profile2.json", "w", encoding="utf8") as file:
    json.dump(profile2, file, indent=4)

with open("profile2.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data)
print(data["skills"])
print(data["country"])


#Exercise 17
#import json

person = {
    "name" : "Alex",
    "age" : 30
}

with open("user.json", "w", encoding="utf8") as file:
    json.dump(person, file)


#Exercise 18
#import json

with open("user.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data)


#Exercise 19
#import json

with open("user.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data["age"])


#Exercise 20
#import json

d = {
    "language" : "Python",
    "version" : 3.13
}

data = json.dumps(d)

print(data)


#Exercise 21
#import json

text = '{"city" : "Seoul", "country" : "Korea"}'

data = json.loads(text)

print(data)


#Exercise 22
#import json

text = '{"city" : "Seoul", "country" : "Korea"}'

data = json.loads(text)

print(data)
print(data["country"])


#Exercise 23
#import json

user = {
    "name" : "Benita",
    "country" : "Germany",
    "job" : "Data Engineer"
}

with open("info.json", "w", encoding="utf8") as file:
    json.dump(user, file, indent = 4)


#Exercise 24
#import json

with open("info.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data)
print(data["job"])


#Exercise 25
#import json

movie = {
    "name" : "Life",
    "year" : 1998
}

with open("movie.json", "w", encoding="utf8") as file:
    json.dump(movie, file)

with open("movie.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data)
print(data["name"])


#Exercise 26
#import json

person = {
    "name" : "Benita",
    "department" : "Data",
    "salary" : 10000
}

with open("employee.json", "w", encoding="utf8") as file:
    json.dump(person, file, indent=4)


#Exercise 27
#import json

with open("employee.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data)
print(data["department"])


#Exercise 28
#import json

d = {
    "framework" : "Spark",
    "language" : "Python"
}

data = json.dumps(d)

print(data)


#Exercise 29
#import json

text = '{"framework" : "Airflow", "version" : 3}'

data = json.loads(text)

print(data)
print(data["framework"])

#Exercise 30
#import json

info = {
    "company" : "Open AI",
    "employees" : 1000,
    "tools" : ["Python", "SQL", "Spark"]
}

with open("company.json", "w", encoding="utf8") as file:
    json.dump(info, file, indent=4)

with open("company.json", "r", encoding="utf8") as file:
    data = json.load(file)

print(data)
print(data["company"])
print(data["tools"])