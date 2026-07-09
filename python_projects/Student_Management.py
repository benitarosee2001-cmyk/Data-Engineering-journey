print("===== Student Management =====")
print("\n1.Add Student")
print("2.Show Students")
print("3.Search Student")
print("4.Delete Student")
print("5.Save to JSON")
print("6.Load from JSON")
print("7.Exit")

print()

choice = input("Choice: ")

print()

name = input("Name: ")
age = int(input("Age: "))
grade = float(input("Grade: "))

print()

if choice == "1":
    print("Student Added!\n")
    print(f"Name: {name} \nAge: {age} \nGrade: {grade}")

