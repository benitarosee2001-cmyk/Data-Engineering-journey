with open("notes.txt", "w", encoding="utf8") as file:
    file.write("Hello Python")



with open("notes.txt", "r", encoding="utf8") as file:
    print(file.read())



with open("notes.txt", "a", encoding="utf8") as file:
    file.write("\nData Engineer")


with open("notes.txt", "r", encoding="utf8") as file:
    print(file.read())



with open("skills.txt", "x", encoding="utf8") as file:
    file.write("Python\nSQL\nSpark")



with open("skills.txt", "r", encoding="utf8") as file:
    print(file.read())



with open("profile.txt", "w", encoding="utf8") as file:
    file.write("Name: Benita\nJob: Data Engineer\nCountry: Germany")



with open("profile.txt", "r", encoding="utf8") as file:
    print(file.read())
