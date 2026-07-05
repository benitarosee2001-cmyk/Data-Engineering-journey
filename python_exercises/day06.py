#Exercise 1
for i in range(20, 0, -1):
    print(i)


#Exercise 2
for i in range(1, 50):
    if i == 30:
        break
    print(i)


#Exercise 3
for i in range(1, 20):
    if i % 3 == 0:
        continue
    print(i)


#Exercise 4
for i in range(1, 11):
    print(f"5 * {i} = {5*i}")


#Exercise 5
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end= " ")
    print()


#Exercise 6
i = 1

while i <= 10:
    print(i)
    i += 1


#Exercise 7
i = 2

while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


#Exercise 8
i = 10

while i >= 1:
    print(i)
    i -= 1


#Exercise 9
i = 1
sum_ = 0

while i <= 100:
    sum_ += i
    i += 1

print(sum_)


#Exercise 10
i = 1

while i <= 20:
    print(i)
    i += 1


#Exercise 11
i = 5

while i <= 30:
    print(i)
    i += 1


#Exercise 12
i = 20

while i >= 1:
    print(i)
    i -= 1


#Exercise 13
i = 2

while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1


#Exercise 14
i = 1

while i <= 50:
    if i % 2 != 0:
        print(i)
    i += 1


#Exercise 15
i = 1
summ = 0

while i <= 50:
    summ += i
    i += 1

print(summ)


#Exercise 16
i = 2
summ = 0

while i <= 100:
    if i % 2 == 0:
        summ += i
    i += 1

print(summ)


#Exercise 17
i = 1
summ = 0

while i < 100:
    if i % 2 != 0:
        summ += i
    i += 1

print(summ)


#Exercise 18
i = 1

while i <= 50:
    if i % 3 == 0:
        print(i)
    i += 1


#Exercise 19
i = 1

while i <= 100:
    if i % 5 == 0:
        print(i)
    i += 1


#Exercise 20
i = 1

while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1


#Exercise 21
i = 1

while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1


#Exercise 22
i = 1

while i <= 20:
    if i == 13:
        break
    print(i)
    i += 1


#Exercise 23
i = 1

while i <= 15:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1


#Exercise 24
i = 1

while i <= 10:
    if i == 8:
        i += 1
        continue
    print(i)
    i += 1


#Exercise 25
i = 1

while i <= 50:
    if i % 9 == 0:
        break
    print(i)
    i += 1


#Exercise 26
i = 1

while i <= 30:
    if i % 3 == 0:
        break
    print(i)
    i += 1


#Exercise 27
i = 1

while i <= 100:
    if i == 50:
        break
    if i % 2 != 0:
        print(i)
    i += 1


#Exercise 28
i = 1

while i <= 20:
    if i % 4 == 0:
        break
    print(i)
    i += 1


#Exercise 29
i = 1

while i <= 100:
    if i == 70:
        break
    if i % 7 == 0:
        i += 1
        continue
    print(i)
    i += 1


#Exercise 30
i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Done")


#Exercise 31
i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1
else:        
    print("go")


#Exercise 32
i = 2

while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
else:
    print("Finished successfully")


#Exercise 33
i = 1

while i < 10:
    if i % 2 != 0:
        print(i)
    i += 1
else:
    print("End")


#Exercise 34
i = 1

while i <= 20:
    if i == 15:
        break
    print(i)
    i += 1
else:
    print("finished")


#Exercise 35
i = 3

while i <= 30:
    if i % 3 == 0:
        print(i)
    i += 1
else:
    print("All multiples printed")


#Exercise 36
i = 1

while i <= 10:
    if i == 7:
        i += 1
        continue
    print(i)
    i += 1
else:
    print("...")


#Exercise 37
i = 10

while i >= 1:
    print(i)
    i -= 1
else:
    print("countdown finished")


#Exercise 38
i = 1

while i <= 100:
    if i % 13 == 0:
        i += 1
        break
    print(i)
    i += 1


#Exercise 39
for i in range(1, 11):
    print(i)


#Exercise 40
summ = 0

for i in range(1, 21):
    summ += i

print(summ)


#Exercise 41
s = "python"

for ch in s:
    print(ch)


#Exercise 42
for i in range(1, 30):
    if i % 2 == 0:
        continue
    print(i)


#Exercise 43
for i in range(1, 10):
    if i == 8:
        break
    print(i)


#Exercise 44
for i in range(10, 0, -1):
    print(i)


#Exercise 45
s = "Data Engineer"
count = 0

for ch in s:
    count += 1

print(count)


#Exercise 46
summ = 0

for i in range(1, 51):
    if i % 5 == 0:
        summ += i

print(summ)


#Exercise 47
s = "python"
vowels = "aeouiAEOUI"

for ch in s:
    if ch in vowels:
        print(ch)


#Exercise 48
for i in range(1, 31):
    if i % 7 == 0:
        continue
    if i == 25:
        break
    print(i)


#Exercise 49
s = "Data Engineer"

for ch in s[::-1]:
    print(ch)


#Exercise 50
s = "python programming"
count = 0

for ch in s:
    if ch == "g":
        count += 1

print(count)


#Exercise 51
for i in range(1, 101):
    if i % 11 == 0:
        print(i)
        break


#Exercise 52
summ = 0

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        summ += i

print(summ)


#Exercise 53
s = "Data123Engineer456"
n = "abcdefghijklmnopqrstuwz" 

for ch in s:
    if ch in n.lower():
        print(ch)