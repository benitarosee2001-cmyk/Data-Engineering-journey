#Exercise 1
import csv

with open("books.csv", "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Title", "Pages"])
    writer.writerow(["Python", 500])


#Exercise 2
import csv

with open("books.csv", "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Title", "Pages"])
    writer.writerow(["Python", 500])
    writer.writerow(["SQL", 350])


#Exercise 3
import csv

with open("books.csv", "r", newline="", encoding="utf8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


#Exercise 4
import csv

with open("books.csv", "r", newline="", encoding="utf8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[0])


#Exercise 5
import csv

with open("skills.csv", "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file)

    writer.writerow(["Skill", "Level"])
    writer.writerow(["Python", "Advanced"])
    writer.writerow(["SQL", "Intermediate"])
    writer.writerow(["Spark", "Beginner"])


#Exercise 6
import csv

with open("skills.csv", "r", newline="", encoding="utf8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


#Exercise 7
import csv

rows = [
    ["Name", "Age"]
    ["Benita", 24],
    ["Mahi", 30],
    ["Emma", 27],
]

with open("students.csv", "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)


#Exercise 8
#import csv

with open("students.csv", "r", encoding="utf8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


#Exercise 9
#import csv

rows = [
    ["Languages", "Level"],
    ["Python", "Advanced"],
    ["SQL", "Intermediate"],
    ["Spark", "Beginner"],
    ["Airflow", "Beginner"],
]

with open("languages.csv", "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)


#Exercise 10
#import csv

with open("languages.csv", "r", encoding="utf8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[0])


#Exercise 11
#import csv

rows = [
    ["Name", "Job", "Salary"],
    ["Benita", "Data Engineer", 10000],
    ["Mahi", "Data Analyst", 5000],
    ["Emma", "Data Scientist", 8000],
]

with open("employees.csv", "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("employees.csv", "r", newline="utf8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        print(row[1])


#Exercise 12
#import csv

with open("books.csv", "w", newline="", encoding="utf8") as file:

    fields = ["Title", "Pages"]

    writer = csv.DictWriter(file, fieldnames= fields)

    writer.writeheader()

    writer.writerow({
        "Title" :"Python",
        "Pages" : 500
    })

    writer.writerow({
        "Title" : "SQL",
        "Pages" : 360
    })


#Exercise 13
#import csv

with open("books.csv", "r", encoding="utf8") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["Title"])


#Exercise 14
#import csv

with open("employee.csv", "w", newline="", encoding="utf8") as file:

    fields = ["Name", "Job"]

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()

    writer.writerow({
        "Name" :"Benita",
        "Job" : "Data Engineer"
    })

    writer.writerow({
        "Name" :"Emma",
        "Job" : "Data Scientist"
    })

    writer.writerow({
        "Name" : "Mahi",
        "Job" : "Data Analyst"
    })


#Exercise 15
#import csv

with open("employee.csv", "r", encoding="utf8") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["Job"])


#Exercise 16
#import csv

with open("products.csv", "w", newline="", encoding="utf8") as file:

    fields = ["Product", "Price", "Stock"]

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()

    writer.writerows([
        {
        "Product" : "Laptop",
        "Price" : 1200,
        "Stock" : 15
        },
        {
        "Product" : "Mouse",
        "Price" : 25,
        "Stock" : 80
        },
        {
        "Product" : "Keyboard",
        "Price" : 70,
        "Stock" : 40
        }
])

with open("products.csv", "r", encoding="utf8") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["Product"])
        print(row["Price"])


#Exercise 17
#import csv

with open("games.csv", "w", newline="", encoding="utf8") as file:

    fields = ["Game", "Genre", "Year"]

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()

    writer.writerows([
        {
        "Game" : "Minecraft",
        "Genre" : "Sandbox",
        "Year" : 2011
        },
        {
        "Game" : "GTA V",
        "Genre" : "Action",
        "Year" : 2013
        },
        {
        "Game" : "Stardew Valley",
        "Genre" : "Simulation",
        "Year" : 2016
        }
    ])

with open("games.csv", "r", encoding="utf8") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        print(row["Game"])
        print(row["Year"])