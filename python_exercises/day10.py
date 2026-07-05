#Exercise 1
numbers = [1, 12, 32, 4, 5, 6]
n = list(map(lambda x: x * 2, numbers))
result = list(filter(lambda x: x > 10, n))

print(result)


#Exercise 2
names = ["Alicia", "Laris", "Rm"]
print(sorted(names, key= lambda x: len(x)))


#Exercise 3
people = [("Suga", 32), ("Jimin", 29), ("JK", 28), ("V", 30)]

print(sorted(people, key= lambda x: x[1]))


#Exercise 4
numbers = [21, 22, 23, 24]
r = list(filter(lambda x: x % 2 != 0, numbers))
result = list(map(lambda x : x ** 2, r))

print(result)


#Exercise 5
person = {
    "Mahi" : 85,
    "Nadi" : 62,
    "Ann" : 70
}

print(sorted(person.items(), lambda x: x[1]))


#Exercise 6
numbers = [10, 20, 30]
numbers.append(40)

print(numbers)


#Exercise 7
numbers = [10, 20, 30]
numbers.extend([50, 60])

print(numbers)


#Exercise 8
numbers = [10, 20, 30]
numbers.insert(1, 15)

print(numbers)


#Exercise 9
numbers = [10, 20, 30]
numbers.remove(20)

print(numbers)


#Exercise 10
numbers = [10, 20, 30]
numbers.pop()

print(numbers)


#Exercise 11
numbers = [5, 2, 5, 8, 5]

print(numbers.count(5))


#Exercise 12
n = [8, 1, 6, 3]
n.sort()

print(n)


#Exercise 13
n = [8, 1, 6, 3]
n.sort(reverse= True)

print(n)


#Exercise 14
n = [8, 1, 6, 3]
n.reverse()

print(n)


#Exercise 15
numbers = (1, 5, 3, 5, 8, 5)

print(numbers.count(5))


#Exercise 16
numbers = (10, 20, 30)

print(numbers.index(30))


#Exercise 17
n = {2, 32, 76, 98}
n.add(10)

print(n)


#Exercise 18
n = {2, 32, 76, 98}
n.remove(2)

print(n)


#Exercise 19
s1 = {1, 2, 3, 4}
s2 = {2, 4, 6, 7}

print(s1.union(s2))


#Exercise 20
s1 = {1, 2, 3, 4}
s2 = {2, 4, 6, 7}

print(s1.intersection(s2))


#Exercise 21
person = {
    "name" : "Jk",
    "age" : 28
}

print(person.get("name"))


#Exercise 22
person = {
    "name" : "Jk",
    "age" : 28
}

print(person.items())


#Exercise 23
person = {
    "name" : "Jk",
    "age" : 28
}

person.update({"city" : "Seoul"})

print(person)


#Exercise 24
person = {
    "name" : "Jk",
    "age" : 28
}

person.pop("age")

print(person)


#Exercise 25
numbers = [1, 2, 3, 4]
result = [i*2 for i in numbers]

print(result)


#Exercise 26
numbers = [1, 2, 3, 4]
square = [i**2 for i in numbers]

print(square)


#Exercise 27
name = ["jk", "jimin", "suga"]
upper = [i.upper() for i in name]

print(upper)


#Exercise 28
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = [i for i in numbers if i % 2 == 0]

print(even)


#Exercise 29
numbers = [5, 12, 20, 3, 18]
result = [i for i in numbers if i > 10]

print(result)


#Exercise 30
names = ["Alicia", "Raya", "Ann", "Kevin"]
result = [i for i in names if i.startswith("A")]

print(result)


#Exercise 31
names = ["SQL", "PANDAS", "PYTHON"]
result = [i.lower() for i in names]

print(result)


#Exercise 32
numbers = [1, 2, 3, 4, 5, 6, 7]
result = [i**2 for i in numbers if i % 2 != 0]

print(result)


#Exercise 33
name = "Python"

print(name.encode())


#Exercise 34
text = b'Hello'

print(text.decode())


#Exercise 35
text = "Data"

print(text.encode())


#Exercise 36
name = "PYTHON"

print(name.lower())


#Exercise 37
skill = "data engineer"

print(skill.title())


#Exercise 38
name = "  SQL  "

print(name.strip())


#Exercise 39
s = "I Love Python"

print(s.replace("Python", "SQL"))


#Exercise 40
s = "Python SQL SPARK"

print(s.split())


#Exercise 41
s = ['Python', 'SQL', 'SPARK']

print(" ".join(s))


#Exercise 42
text = "Notebook"

print(text.find("o"))


#Exercise 43
f = "banana"

print(f.count("a"))


#Exercise 44
s = "python"

print(s.startswith("py"))


#Exercise 45
s = "database.csv"

print(s.endswith("csv"))


#Exercise 46
text = "  pandas  "
t = text.strip()

print(t.upper())


#Exercise 47
sen = "python sql spark"
s = sen.split()

print("-".join(s))