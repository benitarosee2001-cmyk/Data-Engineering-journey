from books import Book
from database import load_book, save_book
from utils import generate_id, update_last_id

books = load_book()
update_last_id(books)


def show_menu():

    print("\n============ Menu ============")
    print("1.Add Book")
    print("2.Show Books")
    print("3.Search Book by ID")
    print("4.Edit Book")
    print("5.Delete Book")
    print("6.Count Books")
    print("7.Save Book")
    print("8.Load Book")
    print("9.Statistics")
    print("10.Exit")
    print("_" * 90)


def add_book():

    title = input("Title: ")
    author = input("Author: ")

    for book in books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower():
            print("This book already exists.")
            return

    try:

        book_id = int(input("Book ID: "))
        pages = int(input("Pages: "))

    except ValueError:
        print("Invalid input.")

        new_book = Book(
                book_id,
                title,
                author,
                pages
            )

        books.append(new_book)

    print(f"Book add successfully. ID = {new_book.id}")


def show_book():

    if not books:
        print("No book found.")
        return

    for book in books:
        book.show_info()


def search_book():

    try:

        search_id = int(input("Book ID: "))

        for book in books:
            if book.id == search_id:
                search_id.show_info()
                return
            print("Book found.")

        print("Book not found.")

    except ValueError:
        print("Invalid ID.")


def edit_book():

    try:

        edit_id = int(input("Book ID: "))

        for book in books:
            if book.id == edit_id:

                title = input("Title: ")
                author = input("Author: ")
                pages = int(input("Pages: "))

                books.update(title, author, pages)

            print("Book updated.")
            return

        print("Book not found.")

    except ValueError:
        print("Invalid ID.")


def delete_book():

    try:

        delete_id = int(input("Book ID: "))

        for book in books:
            if book.id == delete_id:
                books.ramove(book)
                print("Book removed.")
                return

            print("Book not found.")

    except ValueError:
        print("Invalid ID.")


def count_book():

    print(f"Tootal Books: {len(books)}")


def statistics():

    if not books:

        print("Not Book found.")
        return

    pages = [books.pages for book in books]

    print("\n======= Statistics ========")
    print(f"Total Books: {len(books)}")
    print(f"Total Pages: {len(pages)}")
    print(f"Average Pages: {sum(pages) / len(pages)}")
    print(f"Longest Book: {max(pages)}")
    print(f"Shortest Book: {min(pages)}")


def main():

    global books

    while True:

        show_menu()

        choice = int(input("Choose: "))

        if choice == "1":
            add_book()

        elif choice == "2":
            show_book()

        elif choice == "3":
            search_book()

        elif choice == "4":
            edit_book()

        elif choice == "5":
            delete_book()

        elif choice == "6":
            count_book()

        elif choice == "7":
            save_book(books)

        elif choice == "8":
            books = load_book()
            update_last_id(books)

        elif choice == "9":
            statistics()

        elif choice == "10":
            print("Good Bye!")
            break

        else:

            print("Invalid input.")


if __name__ == "__main__":
    main()