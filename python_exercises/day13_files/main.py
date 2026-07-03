#Exercise 1
with open("notes.txt", "w", encoding="utf8") as file:
    file.write("Hello Python")


#Exercise 2
with open("notes.txt", "r", encoding="utf8") as file:
    print(file.read())


#Exercise 3
with open("notes.txt", "a", encoding="utf8") as file:
    file.write("\nData Engineer")


#Exercise 4
with open("notes.txt", "r", encoding="utf8") as file:
    print(file.read())


#Exercise 5
with open("skills.txt", "x", encoding="utf8") as file:
    file.write("Python\nSQL\nSpark")


#Exercise 6
with open("skills.txt", "r", encoding="utf8") as file:
    print(file.read())


#Exercise 7
with open("profile.txt", "w", encoding="utf8") as file:
    file.write("Name: Benita\nJob: Data Engineer\nCountry: Germany")


#Exercise 8
with open("profile.txt", "r", encoding="utf8") as file:
    print(file.read())


#Exercise 9
with open("fruits.txt", "w", encoding="utf8") as file:
    file.writelines([
        "Apple\n",
        "Banana\n",
        "Orange"
    ])


#Exercise 10
with open("fruits.txt", "r", encoding="utf8") as file:
    print(file.read())


#Exercise 11
with open("fruits.txt", "r", encoding="utf8") as file:
    print(file.read(5))


#Exercise 12
with open("fruits.txt", "r", encoding="utf8") as file:
    print(file.readline())


#Exercise 13
with open("fruits.txt", "r", encoding="utf8") as file:
    print(file.readline())
    print(file.readline())


#Exercise 14
with open("fruits.txt", "r", encoding="utf8") as file:
    print(file.readlines())


#Exercise 15
with open("fruits.txt", "r", encoding="utf8") as file:
    for line in file:
        print(line.strip())


#Exercise 16
with open("languages.txt", "w", encoding="utf8") as file:
    file.writelines([
        "Python\n",
        "Sql\n",
        "Spark\n",
        "Pandas\n"
    ])


#Exercise 17
with open("languages.txt", "r", encoding="utf8") as file:
    for line in file:
        print(line.strip())