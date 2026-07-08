#Exercise 1
class Student:

    school = "MIT"

    @classmethod
    def school_name(cls):
        print(cls.school)

Student.school_name()


#Exercise 2
class Calculator:

    @staticmethod
    def subtract(a, b):
        return a - b

print(Calculator.subtract(10, 6))


#Exercise 3
class Company:

    name = "OpenAI"

    @classmethod
    def company_name(cls):
        print(cls.company)

Company.company_name()


#Exercise 4
class Converter:

    @staticmethod
    def km_to_meter(a):
        print(1000 * a)


Converter.km_to_meter(5)


#Exercise 5
class Person:

    def __init__(self):
        self._age = 0
    
    @property
    def age(self):
        return self._age

p = Person()

print(p.age)


#Exercise 6
class Person:

    def __init__(self):
        self._age = 0
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value

p = Person()

p.age = 24

print(p.age)


#Exercise 7
class Product:

    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value

p = Product()

p.price = 100

print(p.price)


#Exercise 8
class Student:

    def __init__(self):
        self._score = 0
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value

s = Student()

s.score = 99

print(s.score)


#Exercise 9
class Battery:

    def charge(self):
        print("Charging...")
    
class Phone:

    def __init__(self):
        self.battery = Battery()

phone = Phone()

phone.battery.charge()


#Exercise 10
class Book:

    def __init__(self, title):
        self.title = title
    
class Library:

    def __init__(self, obj):
        self.obj = obj

b = Book("Python")

library = Library(b)

print(library.obj.title)


#Exercise 11
#from dataclasses import dataclass

#@dataclass
class Book:
    title: str
    page: int

s = Book("Python", 350)

print(s)
print(s.title)
print(s.page)


#Exercise 12
#from dataclasses import dataclass

#@dataclass
class Person:
    name: str
    age: int

p = Person("Benta", 24)

print(p)


#Exercise 13
nums = [100, 200, 300]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))


#Exercise 14
text = "Data"

it = iter(text)

print(next(it))
print(next(it))
print(next(it))
print(next(it))