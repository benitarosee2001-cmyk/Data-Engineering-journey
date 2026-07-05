#Exercise 1
li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2:6])
print(li[::2])


#Exercise 2
skills = ["Python", "SQL", "ETL", "Pandas"]
print(skills.index("SQL"))


#Exercise 3
li = [1, 2, 3, 4, 3, 5, 3, 6, 3, 6, 3]
print(li.count(3))


#Exercise 4
li = [12, 43, 65, 23, 87]
print(li[:2])
print(li[2:6])


#Exercise 5
li1 = [1, 2, 3, 4]
li2 = [4, 5, 6, 7]

for i in li1:
    for i in li2:
        print(i)


#Exercise 6
li = []

for i in range(1, 100):
    if i > 50:
        print(i)


#Exercise 7
name = ["Jin", "Suga", "Ania", "Anisa"]

for i in name:
    if i.startswith("A"):
        print(i)

#Exercise 8
li = [1, 2, 3, 4, 5, 6]

for i in li:
    print(i ** 2)


#Exercise 9
skills = ["Python", "SQL", "ETL", "Pandas"]

for i, skill in enumerate(skills, 1):
    print(f"{i}. {skill}")


#Exercise 10
li = [1, 2, 3, 4, 5]
total = 0

for i in li:
    total += i

print(f"sum: {total}")


#Exercise 11
li = [2, 3, 4, 5, 6]
biggest = li[0]

for i in li:
    if i > biggest:
        biggest = i

print(biggest)


#Exercise 12
names = ["Alish", "Neda", "Jessi","Barbod"]

for i in names:
    if len(i) > 4:
        print(i)


#Exercise 13
li = [1, 2, 3, 4, 5, 6, 7]
odds = []

for i in li:
    if i % 2 != 0:
        odds.append(i)
print(odds)


#Exercise 14
skills = ["Python", "SQL", "ETL", "Pandas"]

for i in skills:
    print(i.upper())


#Exercise 15
li1 = [1, 2, 3, 4, 5]
li2 = [6, 7, 8, 9, 10]
li = []

for i in li1:
    li.append(i)
for i in li2:
    li.append(i)
print(li)


#Exercise 16
data_engineer = {
    "name" : "Benita",
    "age" : 24,
    "city" : "Tehran",
    "skill" : "Python"
}

print(data_engineer["name"])
print(data_engineer.get("age"))
print(data_engineer.get("city"))
print(data_engineer["skill"])


#Exercise 17
data_engineer = {
    "name" : "Benita",
    "age" : 24,
    "city" : "Tehran",
    "skill" : "Python"
}

data_engineer["age"] = 25
data_engineer["salary"] = 100000

print(data_engineer)


#Exercise 18
data_engineer = {
    "name" : "Benita",
    "age" : 24,
    "city" : "Tehran",
    "skill" : "Python"
}

for keys, values in data_engineer.items():
    print(f"{keys} : {values}")


#Exercise 19
data_engineer = {
    "name" : "Benita",
    "age" : 24,
    "city" : "Tehran",
    "skill" : "Python"
}
key = input("key: ")

if key in data_engineer:
    print(data_engineer[key])
else:
    print("not found")


#Exercise 20
skills = {
    "Python" : "Advanced",
    "SQL" : "Intermediate",
    "ETL" : "Advanced"
}

for skill, level in skills.items():
    if level == "Advanced":
        print(skill)


#Exercise 21
city = {
    "Tehran" : 200000,
    "Sari" : 10000,
    "Kerman" : 5000
}
biggest = max(city.values())

for name, pop in city.items():
    if pop == biggest:
        print(name, pop)

#Exercise 22
d1 = {"a" : 1, "b" : 2}
d2 = {"c" : 3, "d" : 4}
d1.update(d2)

print(d1)

#Exercise 23
d = {
    "Sahel" : 19,
    "Bahar" : 20,
    "Roza" : 18
}
s = sum(d.values())
ave = s / len(d)

print(ave)


#Exercise 24
d = {"a" : 1, "b" : 2, "c" : 3}
del d["b"]

print(d)


#Exercise 25
skills = {
    "Python" : 1,
    "Pandas" : 2,
    "SQL" : 3
}

for skill, year in skills.items():
    if year > 2:
        print(skill)


#Exercise 26
d = {
    "korea" : "Seoul",
    "France" : "Paris",
    "Japan" : "Tokyo"
}
country = input("country: ")

if country in d:
    print(d[country])
else:
    print("not found")

#Exercise 27
d = {
    "lipbalm" : 20,
    "mascara" : 100,
    "lipoil" : 51
}

for pro, pri in d.items():
    if pri > 50:
        print(pro)


#Exercise 28
di = {"a" : 1, "b" : 2, "c" : 3}
print(len(di.keys()))

di["d"] = 4
print(len(di.keys()))


#Exercise 29
d = {
    "Ann" : 92,
    "Lima" : 60,
    "Kevin" : 75
}
best = max(d.values())

for name, mark in d.items():
    if mark == best:
        print(name)


#Exercise 30
d = {"a" : 1, "b" : 2, "c" : 3}
li = []

for key, value in d.items():
    li.append(value)
print(li)