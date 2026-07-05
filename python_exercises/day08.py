#Exercise 1
def func(name):
    print(f"Hello, {name}!")

func("benita")


#Exercise 2
def add(x, y):
    return x + y

result = add(4, 12)
print(result)


#Exercise 3
def num(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

num(10)


#Exercise 4
def find_max(li):
    biggest = li[0]
    for i in li:
        if i > biggest:
            biggest = i
    return biggest

print(find_max([1, 23, 45, 3]))


#Exercise 5
def func(name, job = "Data Engineer"):
    print(f"I'm {name} and I'm {job}")

func("benita")



#Exercise 6
def func(name):
    return name

print(func("Jk"))


#Exercise 7
def strr(string):
    for ch in strr[::-1]:
        print(ch)

print(strr("python"))


#Exercise 8
def func():
    print("Welcome")

func()


#Exercise 9
def func():
    print("python")
    print("data")

func()


#Exercise 10
def greet():
    print("Hello!")

greet()
greet()
greet()


#Exercise 11
def prime():
    pass

prime()


#Exercise 12
def num():
    for i in range(1, 6):
        print(i)

num()


#Exercise 13
def hello():
    print("Hello Python")

hello()


#Exercise 14
def stars():
    for i in range(5):
        print("*", end = "")
    print()

stars()
stars()
stars()


#Exercise 15
def numbers():
    for i in range(1, 11):
        print(i)

numbers()


#Exercise 16
def even():
    for i in range(2, 21):
        if i % 2 == 0:
            print(i)

even()


#Exercise 17
def countdown():
    for i in range(5, 0, -1):
        print(i)
        print("go!")

countdown()


#Exercise 18
def greet(name):
    print(f"Hello {name}")

greet("Benita")


#Exercise 19
def square(num):
    print(num ** 2)

square(4)


#Exercise 20
def add(x, y):
    print(x + y)

add(8, 3)


#Exercise 21
def repeat(word):
    for i in range(5):
        print(word)

repeat("Jk")


#Exercise 22
def table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num*i}")

table(4)


#Exercise 23
def square(num):
    return num ** 2

d = square(8)
print(d)


#Exercise 24
def add(a, b):
    return a + b

s = add(3, 9)
print(s)


#Exercise 25
def hello(strr):
    return f"Hello {strr}"

print(hello("Python"))


#Ecercise 26
def is_even(num):
    return num % 2 == 0

print(is_even(12))
print(is_even(71))


#Exercise 27
def max_num(a, b):
    return max(a, b)

d = max_num(2, 9)
print(d)


#Exercise 28
def greet(name = "Guest"):
    return f"Hello {name}"

print(greet())
print(greet("Benita"))


#Exercise 29
def multiply(a, b=2):
    return a * b

print(multiply(5))
print(multiply(1, 8))


#Exercise 30
def country(name = "Korean"):
    return f"country: {name}"

print(country())
print(country("French"))


#Exercise 31
def welcome(name = "Jk"):
    return f"Welcome {name}"

print(welcome())
print(welcome("Json"))


#Exercise 32
def discount(price, percent=10):
    return price - (price * percent / 100)

print(discount(100))
print(discount(100, 20))


#Exercise 33
def add(a, b):
    return a + b

print(add(2, 3))


#Exercise 34
def introduce(name, age):
    return name, age

print(introduce(name="Benita", age= 23))


#Exercise 35
def persone(name, job, country):
    return f"name: {name} country: {country} job: {job}"

print(persone(name="Benita", country="Korea", job="Data Engineer"))


#Exercise 36
def num(*numbers):
    return(numbers)

print(num(1, 2, 3, 4, 5))


#Exercise 37
def person(**info):
    print(info)

person(name="Benita", city="Berlin", age=22)


#Exercise 38
def person(name):
    """print a person's name"""
    print(name)

person("Jk")


#Exercise 39
def add(a, b):
    """The sum of two numbers."""
    return a + b

print(add(2, 8))


#Exercise 40
def square(x:int)->int:
    return x ** 2

print(square(8))


#Exercise 41
def func(name:str)->str:
    return f"Welcom {name}"

print(func("Rose"))

