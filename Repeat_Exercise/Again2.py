import json

library = []

def show_menu():

    print("==== Library ====")
    print("1.Add Book")
    print("2.Show Books")
    print("3.Search Book")
    print("4.Delete Book")
    print("5.Save")
    print("6.Load")
    print("7.Exit")


def add_book():

    title = input("Title: ")
    author = input("Authore: ")
    pages = int(input("Pages: "))

    book = {
        "Title" : title,
        "Author" : author,
        "Pages" : pages
    }

    library.append(book)
    print("Book added successfully.")


def show_book():

    if len(library) == 0:
        print("No books found.")
    else:
        print("===== library =====")

        for book in library:
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Pages: {book['Pages']}")
            print("*" * 50)


def search_book():

    title = input("Title: ")

    found = False

    for book in library:
        if book["Title"].lower() == title.lower():
            print("Book found successfully.")
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Pages: {book['Pages']}")
            found = True
            break

    if not found:
        print("Book not found.")


def delete_book():

    title = input("Title: ")

    found = False

    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print("Book deleted successfully.")
            found = True
            break

    if not found:
        print("Not found.")


def save_book():

    with open("library.json", "w", encoding = "utf8") as file:
        json.dump(library, file, indent=4)
    

    print("Book save successfully.")


def load_book():

    global library
    
    with open("library.json", "r", encoding= "utf8") as file:
        library = json.load(file)

    
    print("Loaded.")


def main():

    while True:

        show_menu()

        choice = input("choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            show_book()

        elif choice == "3":
            search_book()

        elif choice == "4":
            delete_book()

        elif choice == "5":
            save_book()

        elif choice == "6":
            load_book()

        elif choice == "7":
            print("Good Bye!")
            break

        else:
            print("Invalid choice.")

main()