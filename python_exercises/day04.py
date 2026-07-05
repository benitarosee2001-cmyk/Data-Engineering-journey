#Exercise 1
city = ("Paris", "Tokyo", "Seoul", "Tehran", "Sari")
print(city[0])
print(city[-1])


#Exercise 2
t = (1, 2, 3, 4, 5, 6)

for i in t:
    print(i)


#Exercise 3
t = (2, 4, 7, 5)
print(7 in t)


#Exercise 4
t = (1, 3, 4, 3, 2, 3)
print(t.count(3))


#Exercise 5
t = (10, 20, 30, 40)
li = list(t)
li.append(50)
nt = tuple(li)
print(nt)


#Exercise 6
skills = {"Python", "SQL", "Pandas"}
skills.add("ETL")
print(skills)


#Exercise 7
li = [1, 2, 3, 4, 3, 5, 3, 3]
s = set(li)
print(s)


#Exercise 8
s1 = {1, 2, 5, 6}
s2 = {5, 6, 7, 8}

print(s1 & s2)
print(s1 | s2)


#Exercise 9
skills = {"Python", "SQL", "Pandas"}
print("Python" in skills)


#Exercise 10
s1 = {1, 2, 5, 6}
s2 = {5, 6, 7, 8}

print(s1 - s2)


#Exercise 11
s = {"a", "b", "c", "d"}
s.remove("a")
s.discard("b")
s.discard("f")
print(s)

#Exercise 12
email = {"benita@gmail.com", "edvin@gmail.com", "sahel@gmail.com", "benita@gmail.com"}
print(email)


#Exercise 13
p1 = {"Python", "HTML", "Pandas"}
p2 = {"Numpy", "Pandas", "HTML"}
print(p1 & p2)


#Exercise 14
s = {1, 2, 3, 4, 5}

for i in s:
    print(i)


#Exercise 15
d = {
    "Sahel" : [20, 19, 18],
    "Edvin" : [20, 20, 20],
    "Rosa" : [18, 17, 16]
}

for name, marks in d.items():
    ave = sum(marks) / len(marks)
    print(f"{name}: {ave}")


#Exercise 16
skills = {
    "python" : "easy",
    "SQL" : "itermediate",
    "ETL" : "advanced"
}

for name, level in skills.items():
    if level == "advanced":
        print(level)


#Exercise 17
name = ["mahi", "aftab", "laleh", "mahi"]
n = set(name)
print(n)
print(sorted(n))


#Exercise 18
city = ("Paris", "Tokyo", "Seoul", "Tehran", "Sari")
c = set(city)
c.add("Istanbol")
print(c)


#Exercise 19
d1 = {"mahi" : 18, "kevin" : 20, "jack" : 22}
d2 = {"mahi" : " Tehran", "kevin" : "paris", "aftab" : "seoul"}

for key in d1:
    if key in d2:
        print(key)

#Exercise 20
d = {
    "python" : 1,
    "SQL" : 2,
    "pandas" : 3
}

for skill, year in sorted(d.items(), key = lambda x: x[1]):
    print(skill, year)


#Exercise 21
li = [1, 2, 3, 4, 5, 6]
t = []
s = set()

for i in li:
    if i % 2 == 0:
        t.append(i)
    else:
        s.add(i)
print(tuple(t))
print(s)


#Exercise 22
cosmetic = {
    "lip balm" : 20,
    "lip oil" : 40,
    "lip gloss" : 80
}
expensive = max(cosmetic.values())
cheap = min(cosmetic.values())

for pro, pri in cosmetic.items():
    if pri == expensive:
        print(f"expensive: {pro}")
    elif pri == cheap:
        print(f"cheap: {pro}")
    else:
        print("average")


#Exercise 23
li = [{"jin" : 24}, {"jk" : 29}, {"v" : 25}]

for person in li:
    for name, age in person.items():
        if age > 25:
            print(age)


#Exercise 24
de = {"python", "sql", "pandas", "numpy"}
mde = {"python"}

print(de - mde)