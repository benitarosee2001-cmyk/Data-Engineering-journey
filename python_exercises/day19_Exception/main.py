#Exercise 1
try:
    print(10/0)

except ZeroDivisionError:
    print("Division Error")


#Exercise 2
try:
    print(int("hello"))

except ValueError:
    print("Invalid Number")


#Exercise 3
try:
    numbers = [1, 2, 3]

    print(numbers[10])

except IndexError:
    print("Index Error")


#Exercise 4
try:
    print(5/0)

except ZeroDivisionError:
    print("Can't divide")


#Exercise 5
try:
    print(20/4)

except ZeroDivisionError:
    print("Error")

else:
    print("Success")


#Exercise 6
try:
    print(10/0)

except ZeroDivisionError:
    print("Error")

finally:
    print("Done")


#Exercise 7
try:
    print(int("50"))

except ValueError:
    print("Error")

else:
    print("Valid Number")

finally:
    print("Finished")


#Exercise 8
number = -5

if number < 0:
    raise ValueError("Number is Invalid")


#Exercise 9
class AgeError(Exception):
    pass

age = -4

if age < 0:
    raise AgeError("Invalid")


#Exercise 10
score = 90

assert score >= 0


#Exercise 11
password = "12345"

assert len(password) >= 8, "is too short"