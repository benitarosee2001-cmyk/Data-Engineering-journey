# Exercise 1
name = "benita"
age = 24
city = "Tehran"

print(f" My name is {name} and I'm {age} I live in {city}")


#Exercise 2
a = 17
b = 5
print(a // b)
print(a % b)
print(a ** b)


#Exercise 3
price = 1500000
discount = price * 20 / 100
final = price - discount
print(final)


#Exercise 4
number = 365
units = number % 10
tens = number // 10 % 10
hundreds = number // 100
print(units)
print(tens)
print(hundreds)


#Exercise 5
x = int(input("x: "))
y = int(input("y: "))
total = x + y
print(total)


#Exercise 6
s = "stray kids"
print(len(s))
print(s.upper())


#Exercise 7
price = float(input("price: "))
discount = price * 9 / 100
final = price - discount
print(final)


#Exercise 8
a = 120
b = 12.5
c = True
print(type(a))
print(type(b))
print(type(c))


#Exercise 9
x = int(input("x: "))

if x % 2 == 0:
    print("even number")
else:
    print("odd number")


#Excersice 10
age = int(input("What's your age? "))

if age > 18:
    print("can work remotely")
else:
    print("too young")


#Exercise 11
a = int(input("a: "))
b = int(input("b: "))

if a > b:
    print(a)
else:
    print(b)


#Exercise 12
mark = float(input("mark: "))

if mark > 90:
    print("A")
elif mark > 70:
    print("B")
elif mark > 50:
    print("c")
else:
    print("F")


#Exercise 13
monthly_salary = float(input("monthly salary: "))

if monthly_salary > 50:
    print("above average")
elif 20 < monthly_salary < 50:
    print("average")
else:
    print("below average")


#Exercise 14
i = 1
while i <= 10:
    print(i)
    i += 1


#Exercise 15
x = int(input("x: "))
while x != 0:
    print(x)
    x = int(input("x: "))
print("finished")


#Exercise 16
n = int(input("n: "))
i = 1
while i <= 10:
    print(n,"*",i,"=",n*i)
    i += 1

#Exercise 17
i = 1
while i <= 50:
    if i % 3 == 0:
        print(i)
    i += 1


#Exersice 18
password = input("password: ")

while password != "benita123":
    print("Try again")
    password = input("password: ")
print("Welcome")


#Exercise 19
r = float(input("r: "))
area = 3.14 * r ** 2
print(f"Area: {area:.2f}")


#Excersise 20
seconds = int(input("seconds: "))
hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{hours} hour")
print(f"{minutes} minute")
print(f"{seconds} second")


#Exercise 21
price = float(input("price: "))
discount = price * 15 / 100
final_price = price - discount
print(final_price)


#Exercise 22
x = "Benita"
print(len(x))
print(x.upper())
print(x.lower())


name = input("name: ")   #benita


#Exercise 23
if len(name) > 5:
    print("long name")
else:
    print("short name")



#Exercise 24
s = input("sentence: ")   #Hi i'm benita

print(len(s.replace(" ","")))


#Exercise 25
w = input("words: ")   #alishah

if w[0] == "a":
    print("start with a")
else:
    print("doesn't start with a")


#Exercise 26
s = input("sentence: ")
print(s.split(" "))


#Exercise 27
text = input("text: ")
print(text.count("a"))


#Exercise 28
name = input("name: ")

print(name.strip())
print(name.capitalize())


#Exercise 29
s = input("sentence: ")

print(s.replace("bad", "good"))


#Exercise 30
email = input("email: ")

print('@' in email)


#Exercise 31
s = input("sentence: ")
print(s.startswith("data"))


#Exercise 32
str = input("string: ")

print(len(str.split(" ")))



#Exercise 33
s = input("sentence: ")
print("2024" in s)


#Exercise 34
w = input("word: ")
print(w.split()[0])


#Exercise 35
skills = ["Python" , "SQL", "Pandas"]

print(" | ".join(skills))


#Exercise 36
s = input("sentence: ")

print(s.split()[-1])


#Exercise 37
text = input("text: ")

print(text.isnumeric())


#Exercise 38
email = input("email: ")

print(email.split("@")[0])


#Exercise 39
s = input("sentence: ")
words = s.split()

print(len(s.split(" ")))
print(len(s.replace(" ", "")))
print(words[0])
print(words[-1])


#Exercise 40
x = 54637
print(x.isnumeric())