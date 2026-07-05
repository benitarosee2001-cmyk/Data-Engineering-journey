#Exercise 1
s = input("sentence: ")
print(s.split()[2])


#Exercise 2
s = input("sentence: ")
print(len(s.split()))


#Exercise 3
date = int(input("date: "))
parts = date.split("-")
print(parts[0])
print(parts[1])
print(parts[2])


#Exercise 4
s = input("sentence: ")
words = s.split()
print(words[::-1])


#Exercise 5
s = input("sentence: ")
print("data" in s.split())

#Exercise 6
s = input("sentence: ")
words = s.split()
print(words[-2])


#Exercise 7
jib = input("jib: ")
parts = jib.split("/")
print(parts[0])
print(parts[1])
print(parts[2])


#Exercise 8
s = input("sentence: ")
words = s.split()
print(words[::-1])


#Exercise 9
s = input("sentence: ")
print("python" in s.split())


#Exercise 10
s = input("sentence: ")
words = s.split()[0]
word = s.split()[-1]
print(" | ".join([words , word]))


#Exercise 11
s = input("sentence: ")
words = s.split()
print(words[-3])


#Exercise 12
ip = (input("IP: "))
parts = ip.split(".")
print(parts[0])
print(parts[1])
print(parts[2])


#Exercise 13
s = input("sentence: ")
print(s.replace("error", "succeses"))



#Exercise 14
date = int(input("date: "))
parts = s.split("/")
p = parts[0]
pa = parts[1]
print("-".join([p, pa]))


#Exercise 15
s = input("sentence: ")
words = s.split()
print(" | ".join([words[0], words[-1]]))


#Exercise 16
s = input("sentence: ")
words = s.split(" ")
print(len(words))


#Exercise 17
path = input("path: ")
parts = path.split("/")
print(parts[-1])


#Exercise 18
tag1 = input("tag1: ")
tag2 = input("tag2: ")
tag3 = input("tag3: ")
print(" , ".join([tag1, tag2, tag3]))


#Exercise 19
s = input("sentence: ")
print("data" in s.split())


#Exercise 20
s = input("sentence: ")
words = s.split(" ")
w = words[::-1]
print(" ".join(w))


#Exercise 21
email = input("email: ")
s = email.split("@")
print(s[1])


#Exercise 22
s = input("sentence: ")
words = s.split(" ")
print(words[1].upper())


#Exercise 23
s = input("sentence: ")
print(len(s.replace(" ", "")))


#Exercise 24
s = input("sentence: ")
print(s.endswith("python"))


#Exercise 25
s = input("sentence: ")
words = s.split(" ")
del words[0]
print(" ".join(words))


#Exercise 26
url = input("URL: ")
s = url.split("/")
print(s[0])


#Exercise 27
date = input("date: ")
p = date.split("-")
print(p[0])
print(p[1])
print(p[2])


#Exercise 28
s = input("sentence: ")
words = s.split(" ")
w = words[::-1]
print(" ".join(w))


#Exercise 29
email = input("email: ")
print(email.split("@")[1])


#Exercise 30
path = input("path: ")
words = path.split(" / ")
w = words[0]
wo = words[-1]
print(" | ".join([w, wo]))


#Exercise 31
n = float(input("n: "))
print(int(n))


#Exercise 32
x = int(input("x: "))
y = int(input("y: "))

print(sum([x, y]))


#Exercise 33
x = int(input("x: "))
print(abs(x))


#Exercise 34
n = float(input("n: "))
print(round(n, 2))


#Exercise 35
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

print(max(x, y, z))


#Exercise 36
li = ["Python", "SQL", "Pandas", "ETL", "Numpy"]
print(li[0])
print(li[-1])


#Exercise 37
li = ["Python", "SQL", "Pandas", "ETL", "Numpy"]
li.append("Spark")
print(li)


#Exercise 38
name1 = input("name1: ")
name2 = input("name2: ")
name3 = input("name3: ")
li = [name1, name2, name3]
li.sort()
print(li)


#Exercise 39
n = [1, 2, 3, 4, 5]

print(min(n))
print(max(n))
print(sum(n))


#Exercise 40
skills = ["Python", "SQL", "Pandas", "ETL", "Numpy"]
skill = input("skill: ")

print(skill in skills)


#Exercise 41
li = [1, 2, 3, 4, 5]
print(li[2])


#Exercise 42
skills = ["Python", "SQL", "Pandas", "ETL", "Numpy"]
skills.pop(0)
print(skills)


#Exercise 43
li = [12, 98, 23, 45, 64, 32]
li.reverse()
print(li)


#Exercise 44
city1 = input("city1: ")
city2 = input("city2: ")
city3 = input("city3: ")
city4 = input("city4: ")
li = [city1, city2, city3, city4]
li[1] = "Berlin"

print(li)


#Exercise 45
li = [1, 2, 3, 4, 5]
print(len(li))
li.append(6)
print(len(li))


#Exercise 46
li = [1, 2, 3, 4, 5]

for i in li:
    print(i)


#Exercise 47
li = [4, 5, 6, 7, 8, 10]

for i in li:
    if i % 2 == 0:
        print(i)


#Exercise 48
li = []

for i in range(5):
    n = int(input(f"number {i+1}: "))
    li.append(n)
sum_ = sum(li)
ave = sum_ / len(li)

print(sum_)
print(ave)


#Exercise 49
skills = ["Python", "SQL", "Pandas", "ETL", "Numpy"]

for i in skills:
    print("skills: ", i)


#Exercise 50
li1 = [1, 3, 5, 7]
li2 = [2, 4, 6, 8]
li = li1 + li2

print(li)