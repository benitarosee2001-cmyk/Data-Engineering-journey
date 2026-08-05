import json

books = []

def add_book():

    title = input("Title: ")
    author = input("Author: ")
    pages = int(input("Pages: "))

    book = {
        "Title" : title,
        "Author" : author,
        "Pages" : pages,
    }

    books.append(book)
    print("\nBook Added.")


def show_book():
        
        if len(books) == 0:
            print("No books found.")
            return
    
        for book in books:
            print("="*50)
            print("Title: ", book["Title"])
            print("Author: ", book["Author"])
            print("Pages: ", book["Pages"])


def search_book():

    title = input("Title: ")

    found = False

    for book in books:
        if book["Title"].lower() == title.lower():
            print(book)

            found = True

    if not found:
        print("Book not found.")


def delete_book():
    title = input("Title: ")

    for book in books:
        if book["Title"].lower() == title.lower():
            books.remove(book)

            print("Books deleted.")
            return
    print("Book not found")


def save_book():
    with open("library.json", "w", encoding="utf8") as file:
        json.dump(books, file, indent=4)
        print("Saved.")


def load_book():
    global books

    with open("library.json", "r", encoding="utf8") as file:
        books = json.load(file)
    
    print("Loaded.")


def main():

    while True:

        print("===== Library =====")
        print("\n1.Add Book")
        print("2.Show Book")
        print("3.Search Book")
        print("4.Delete Book")
        print("5.Save")
        print("6.Load")
        print("7.Exit")

        choice = input("Choice: ")

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
            break

        else:
            print("Invalid choice.")

main()