#Exercise 1
country = "Korean"

def func():
    print(country)

func()


#Exercise 2
def person():
    age = 22
    print(age)

person()


#Exercise 3
score = 50

def change():
    score = 100
    print(score)

change()
print(score)


#Exercise 4
score = 50

def change():
    global score
    score = 100

change()
print(score)


#Exercise 5
def add(x):
    x += 10
    print(x)

num = 124

add(num)
print(num)


#Exercise 6
def add_x(x):
    x.append(3)

li = [1, 2]

add_x(li)

print(li)


#Exercise 7
def add_s(s):
    s += "Python"
    print(s)

st = "SQL"

add_s(st)
print(st)


#Exercise 8
def add_d(d):
    d["age"] = 23
    print(d)

student = {"name" : "Jk"}

add_d(student)
print(student)


#Exercise 9
x = 10

def sun():
    print(x)

sun()
print(x)


#Exercise 10
size = 120

def person():
    global size
    size = 140

person()
print(size)


#Exercise 11
x = 105

def x_1():
    x = 10
    print(x)

def x_2():
    x = 25
    print(x)

x_1()
x_2()
print(x)


#Exercise 12
def ret():
    a = 20
    return a

print(ret())


#Exercise 13
counter = 120

def func():
    global counter
    counter += 1

func()
print(counter)


#Exercise 14
numbers = [2, 3, 4, 5]
square = list(map(lambda x: x ** 4, numbers))

print(square)


#Exercise 15
numbers = [2, 3, 4, 5, 6]
cube = list(map(lambda x: x ** 3, numbers))

print(cube)


#Exercise 16
numbers = [11, 3, 43, 6]
s = list(filter(lambda x: x > 10, numbers))

print(s)


##Exercise 17
name = ["jk", "v", "jimin"]
upper = list(map(lambda x: x.upper(), name))

print(upper)


#Exercise 18
names = ["Ajin", "Yuna", "Mingi"]

result = list(filter(lambda x: x.startswith("A"), name))

print(result)


#Exercise 19
num = [2, 3, 4, 5, 6]
result = list(map(lambda x: x * 2, num))
re = list(filter(lambda x: x > 3, num))

print(re)


#Exercise 20
numbers = [2, 3, 4, 5, 6]
cube = list(map(lambda x: x ** 3, numbers))

print(cube)


#Exercise 21
numbers = [21, 32, 2, 12, 87]
result = list(filter(lambda x: x > 10, numbers))

print(result)


#Exercise 22
names = ["jin", "suga", "rm", "jimin"]
result = list(map(lambda x: x.upper(), names))

print(result)


#Exercise 23
name = ["Mahi", "Asemon", "Roya", "Aramesh"]
result = list(filter(lambda x: x.startswith("A"), name))

print(result)
