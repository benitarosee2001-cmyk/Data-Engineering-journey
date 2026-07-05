#Exercise 1
mark = float(input("mark: "))

if mark >= 90:
    print("A")
elif mark >= 80:
    print("B")
elif mark >= 70:
    print("C")
elif mark >= 60:
    print("D")
else:
    print("E")


#Exercise 2
age = int(input("age: "))
salary = float(input("salary: "))

if age > 20 and salary > 2000:
    print("eligible for remote work")


#Exercise 3
x = int(input("x: "))
result = "even" if x % 2 == 0 else "odd"
print(result)

#Exercise 4
skills = {"python", "sql", "pandas", "numpy"}

if "sql" in skills:
    print("ready for DE")
else:
    print("learn SQL firs")


#Exercise 5
de = {"skill" : "python", "age" : 24}

if "salary" not in de:
    print("salary not set")


#Exercise 6
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x >= y and x >= z:
    biggest = x
elif y >= x and y >= z:
    biggest = y
else:
    biggest = z

print(f"The largest number: {biggest}")


#Exercise 7
year = int(input("year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} isn't leap year")


#Exercise 8
username = input("username: ")
password = input("password: ")

if username == "benita" and password == "1234":
    print("loggin successful")
else:
    print("failed")


#Exercise 9
x = int(input("x: "))

if x > 0:
    print("positive number")
elif x < 0:
    print("negetive number")
else:
    print("0")


#Exercise 10
d = {
    "python" : "advanced",
    "sql" : "intermediate",
    "pandas" : "advanced"
}

if d["python"] == "advanced":
    print("ready to freelance")
else:
    print("keep practicing")


#Exercise 11
n = int(input("n: "))

if 1 <= n <= 10:
    print("between 1 and 10")
elif 11 <= n <= 100:
    print("between 11 and 100")
else:
    print("greater than 100")


#Exercise 12
s1 = input("s1: ")
s2 = input("s2: ")

if len(s1) > len(s2):
    print("s1 is longer")
elif len(s2) > len(s1):
    print("s2 is longer")
else:
    print("equal")


#Exercise 13
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
all_even = True

for i in li:
    if i % 2 != 0:
        all_even = False
        break
if all_even:
    print("all even")
else:
    print("mixed")



#Exercise 14
month = int(input("month: "))

if 1 <= month <= 3:
    print("winter")
elif 4 <= month <= 6:
    print("spring")
elif 7 <= month <= 9:
    print("summer")
else:
    print("fall")


#Exercise 15
de_skills = ["python", "sql", "pandas"]

skill1 = input("skill1: ")
skill2= input("skill2: ")
skill3 = input("skill3: ")

if skill1 in de_skills and skill2 in de_skills and skill3 in de_skills :
    print("qualified")
else:
    for skill in [skill1, skill2, skill3]:
        if skill not in  de_skills:
            print(f"missing: {skill}")


# Exercise 16

d = {
    "a": 1,
    "b": 2,
    "c": "e",
    "d": 3.5,
    "e": True
}

for value in d.values():
    if type(value) is int:
        print(value)


#Exercise 17
li = [1, 2, 3, 4, 5]

count = 0

for i in li:
    if i % 2 == 0:
        count += 1

print(count)


#Exercise 18
d = {"p" : "111", "o" : 3, "g" : "u"}

d.update({"w" : 222})

print(d)


#Exercise 19
li = [-22, -3, 0, 10, 78]
all_pos = True

for i in li:
    if i <= 0:
        all_pos = False

if all_pos:
    print("all possitive")
else:
    print("mixed")


#Exercise 20
n = int(input("n: "))

result = "greater than 100" if n > 100 else "not greater than 100"

print(result)