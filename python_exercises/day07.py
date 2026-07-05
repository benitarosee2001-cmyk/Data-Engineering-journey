#Exercise 1
for i in range(1, 5):
    for j in range(1, 5):
        print("*", end = " ")
    print()


#Exercise 2
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j, end = " ")
    print()


#Exercise 3
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end = " ")
    print()


#Exercise 4
for ch in "ABC":
    for i in range(3):
        print(ch, end = " ")
    print()


#Exercise 5
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end = " ")
    print()


#Exercise 6
for i in range(1, 5):
    for j in range(1):
        print("*", end = " ")
    print()


#Exercise 7
for i in range(2):
    for j in range(2):
        print("*", end = " ")
    print()


#Exercise 8
for i in range(1, 5):
    for j in range(1):
        print(i, end = " ")
    print()


#Exercise 9
for i in range(1, 4):
    for j in range(1, i+1):
        print("#",end = " ")
    print()


#Exercise 10
for i in range(1, 4):
    for j in range(2):
        print(i, end = " ")
    print()


#Exercise 11
for i in range(1, 4):
    for j in range(1, 3):
        print(j, end = " ")
    print()


#Exercise 12
for i in range(1, 5):
    for j in range(1, i + 1):
        print("@" , end = " ")
    print()


#Exercise 13
for i in range(10):
    if i % 2 == 0:
        print(i)


#Exercise 14
for i in range(2):
    for j in range(5, 0, -1):
        print(j, end = " ")
    print()


#Exercise 15
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end = " ")
    print()


#Exercise 16
for i in range(5, 26, 5):
    print(i, end = " ")


#Exercise 17
for i in range(30, 20, -1):
    print(i, end = " ")


#Exercise 18
for i in range(4, 51, 4):
    print(i, end = " ")


#Exercise 19
for i in range(100, 9, -10):
    print(i)


#Exercise 20
for i in range(3, 31, 3):
    print(i)


#Exercise 21
s = "python"

for i,value in enumerate(s):
    print(i, value)


#Exercise 22
li = ["jin", "suga", "jk"]

for i, name in enumerate(li):
    print(i, name)


#Exercise 23
s = "Engineer"

for i, w in enumerate(s, start = 1):
    print(w)


#Exercise 24
li = [10, 20, 30, 40]

for i, n in enumerate(li):
    print(i, n)


#Exercise 25
s = "Data Engineer"

for i, w in enumerate(s):
    if i % 2 == 0:
        print(i, w)


#Exercise 26
li = ["jin", "suga", "jk"]
ages = [20, 22, 19]

for name, a in zip(li, ages):
    print(name, a)


#Exercise 27
s1 = "ABC"
s2 = "123"

for i, c in zip(s1, s2):
    print(i, c)


#Exercise 28
fruits = ["Apple", "Banana", "Orange"]
colors = ["Red", "Yellow", "Orange"]

for f, c in zip(fruits, colors):
    print(f, c)


#Exercise 29
names = ["jin", "suga", "jk"]
ages = [20, 22, 19]
cities = ["Berlin", "Paris", "Seoul"]

for n, a, c in zip(names, ages, cities):
    print(n, a, c)


#Exercise 30
numbers = [1, 2, 3, 4, 5]
letters = ["A", "B", "C"]

for num, let in zip(numbers, letters):
    print(num, let)


#Exercise 31
n = int(input("n: "))
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} isn't prime")


#Exercise 32
result = 1

for i in range(1, 6):
    result *= i

print(result)