#Exercise 1
def square(x):
    return x ** 2

print(square(8))


#Exercise 2
def greet(name="Jk"):
    return f"Hello {name}"

print(greet())
print(greet("Benita"))


#Exercise 3
def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3, 4, 5))


#Exercise 4
def user_info(**info):
    print(info)

user_info(name="Alicia", age=24, city="Berlin")


#Exercise 5
numbers = [1, 2, 3, 4]
multiply = list(map(lambda x: x * 2, numbers))

print(multiply)
