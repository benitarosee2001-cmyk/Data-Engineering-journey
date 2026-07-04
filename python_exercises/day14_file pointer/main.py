#Exercise 1
with open("skill.txt", "w", encoding="utf8") as file:
    file.write("Hello world!")


#Exercise 2
with open("skill.txt", "r", encoding="utf8") as file:
    print(file.tell())


#Exercise 3
with open("skill.txt", "r", encoding="utf8") as file:
    file.seek(5)
    print(file.tell())


#Exercise 4
with open("skill.txt", "r", encodig="utf8") as file:
    print(file.tell())


#Exercise 5
with open("skill.txt", "r", encoding="utf8") as file:
    file.seek(0)
    print(file.read())


#Exercise 6
with open("skill.txt", "r", encoding="utf8") as file:
    file.tell(10)
    file.seek(0)
    print(file.readline())


#Exercise 7
with open("language.txt", "w", encoding="utf8") as file:
    file.writelines([
        "Python\n",
        "Sql\n",
        "Spark\n",
        "Pandas"
    ])


#Exercise 8
with open("language.txt", "r", encoding="utf8") as file:
    file.seek(0)
    for line in file:
        print(line.strip())


#Exercise 9
