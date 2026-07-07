#Exercise 1
class Car:
    pass

car1 = Car()

car1.name = "BMW"

print(car1.name)


#Exercise 2
class Cat:
    
    def sound(self):
        print("Meow")

cat = Cat()

cat.sound()


#Exercise 3
class Person:
    pass

p1 = Person()

p1.name = "Benita"
p1.country = "Germany"

print(p1.name)
print(p1.country)


#Exercise 4
class Book:

    def read(self):
        print("Reading...")

book = Book()
book.read()


#Exercise 5
class Laptop:
    pass

lap = Laptop()

lap.brand = "Lenovo"
lap.ram = 32
lap.cpu = "Intel"

print(lap.brand)
print(lap.ram)
print(lap.cpu)


#Exercise 6
class Person:

    def __init__(self, name):
        self.name = name

p1 = Person("Benita")

print(p1.name)


#Exercise 7
class Car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car = Car("BMW", 2026)

print(car.brand)
print(car.year)


#Exercise 8
class Student:

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

std = Student("Benita", 24, "Germany")

print(std.name)
print(std.age)
print(std.country)


#Exercise 9
class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Rocky")

dog.bark()


#Exercise 10
class Employee:

    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary
    
    def info(self):
        print(f"Name: {self.name} \nJob: {self.job} \nSalary: {self.salary}")

emp = Employee("Benita", "Data Engineer", 10000)

emp.info()


#Exercise 11
class Student:

    school = "MIT"

    def __init__(self, name):
        self.name = name

std = Student("Bahar")

print(std.school)
print(std.name)


#Exercise 12
class Car:

    company = "BMW"

    def __init__(self, model):
        self.model = model

c1 = Car("X5")
c2 = Car("M3")

print(c1.company)
print(c1.model)
print(c2.model)


#Exercise 13
class Book:

    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return self.title

b = Book("Romance")

print(b)


#Exercise 14
class Employee:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Employee ({self.name})"

emp = Employee("Benita")

print(emp)


##Exercisde 15
class Animal:

    def __init__(self, name):
        self.name = name
    
class Cat(Animal):
    pass

cat = Cat("Luna")

print(cat.name)


#Exercise 16
class Person:

    def hello(self):
        print("Hello!")

class Student(Person):
    pass

s = Student()

s.hello()


#Exercise 17
class Vehicle:

    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):

    def __init__(self,brand, model):
        super().__init__(brand)
        self.model = model

car = Car("BMW", "X5")

print(car.brand)
print(car.model)


#Exercise 18
class Animal:

    def sound(self):
        print("some sound")

class Dog(Animal):

    def sound(self):
        print("Woof!")

dog = Dog()

dog.sound()


#Exercise 19
class Animal:

    def eat(self):
        print("Eating...")

class Bird(Animal):
    pass

b = Bird()

b.eat()


#Exercise 20
class Person:

    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

t = Teacher("Emma")

print(t.name)


#Exercise 21
class Device:

    def __init__(self, brand):
        self.brand = brand

class Laptop(Device):

    def __init__(self, brand, ram):
        super().__init__(brand)
        self.ram = ram

lap = Laptop("Lenovo", 32)

print(lap.brand)
print(lap.ram)


#Exercise 22
class Vehicle:

    def move(self):
        print("Moving...")

class Bike(Vehicle):

    def move(self):
        print("Bike is moving.")

b = Bike()

b.move()


#Exercise 23
class Employee:

    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f"Employee: {self.name}")

class Manager(Employee):

    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

m = Manager("Benita", "Data")

m.info()

print(m.department)


#Exercise 24
class Dog:

    def sound(self):
        print("Woof!")

class Cat:

    def sound(self):
        print("Meow!")

d = Dog()
c = Cat()

d.sound()
c.sound()


#Exercise 25
class Car:

    def move(self):
        print("Driving...")

class Plane:

    def move(self):
        print("Flying...")

c = Car()
p = Plane()

c.move()
p.move()


#Exercise 26
class CSVFile:

    def open(self):
        print("Opening CSV...")

class JSONFile:

    def open(self):
        print("Opening JSON...")

s = [CSVFile(), JSONFile()]

for file in s:
    file.open()


#Exercise 27
class PythonCourse:

    def study(self):
        print("Studying Python")


class SQLCourse:

    def study(self):
        print("Studying SQL")


class SparkCourse:

    def study(self):
        print("Studying Spark")


courses = [
    PythonCourse(),
    SQLCourse(),
    SparkCourse()
]

for course in courses:
    course.study()